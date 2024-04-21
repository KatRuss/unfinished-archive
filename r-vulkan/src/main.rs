
use std::sync::Arc;
use image::{ImageBuffer, Rgba};
use vulkano::{
    buffer::{Buffer, BufferContents, BufferCreateInfo, BufferUsage}, command_buffer::{allocator::{StandardCommandBufferAllocator, StandardCommandBufferAllocatorCreateInfo}, AutoCommandBufferBuilder, CommandBufferUsage, CopyImageToBufferInfo, RenderPassBeginInfo, SubpassBeginInfo, SubpassContents, SubpassEndInfo}, device::{Device, DeviceCreateInfo, QueueCreateInfo, QueueFlags}, format::{ClearColorValue, Format}, image::{view::ImageView, Image, ImageCreateInfo, ImageType, ImageUsage}, instance::{Instance, InstanceCreateInfo}, memory::allocator::{AllocationCreateInfo, MemoryTypeFilter, StandardMemoryAllocator}, pipeline::{self, graphics::{color_blend::{ColorBlendAttachmentState, ColorBlendState}, input_assembly::InputAssemblyState, multisample::MultisampleState, rasterization::RasterizationState, vertex_input::{Vertex, VertexDefinition}, viewport::{Viewport, ViewportState}, GraphicsPipelineCreateInfo}, layout::PipelineDescriptorSetLayoutCreateInfo, GraphicsPipeline, PipelineLayout, PipelineShaderStageCreateInfo}, render_pass::{Framebuffer, FramebufferCreateInfo, Subpass}, sync::{self, GpuFuture}, VulkanLibrary
};

mod vs {
    vulkano_shaders::shader!{
        ty: "vertex",
        src: r"
            #version 460

            layout(location = 0) in vec2 position;

            void main() {
                gl_Position = vec4(position, 0.0, 1.0);
            }
        ",
    }
}

mod fs {
    vulkano_shaders::shader!{
        ty: "fragment",
        src: "
            #version 460

            layout(location = 0) out vec4 f_color;

            void main() {
                f_color = vec4(0.922, 0.741, 0.827, 1.0);
            }
        ",
    }
}


#[derive(BufferContents, Vertex)]
#[repr(C)]
struct VkVertex {
    #[format(R32G32_SFLOAT)]
    position: [f32;2],
}


fn main() {
    // Vulkan Setup
    let library = VulkanLibrary::new().unwrap();
    let instance = Instance::new(library, InstanceCreateInfo::default()).expect("Failed to create instance");

    let physical_device = instance.enumerate_physical_devices()
    .expect("could not enumerate devices").next()
    .expect("no devices available");

    // Queues
    for family in physical_device.queue_family_properties() {
        println!("Found a queue family with {:?} queue(s)", family.queue_count);
    }

    let queue_family_index = physical_device
    .queue_family_properties().iter().enumerate()
    .position(|(_queue_family_index, queue_family_properties)| {
        queue_family_properties.queue_flags.contains(QueueFlags::GRAPHICS)
    })
    .expect("couldn't find a graphical queue family") as u32;

    // Create Device
    let (device, mut queues) = Device::new(
        physical_device,
        DeviceCreateInfo {
            // here we pass the desired queue family to use by index
            queue_create_infos: vec![QueueCreateInfo {
                queue_family_index,
                ..Default::default()
            }],
            ..Default::default()
        },
    )
    .expect("failed to create device");
    println!("Device in Use: {:?}", device);

    //get Queue
    let queue = queues.next().unwrap(); //TODO: Should be changed to find the best queue somehow.

    // Memory Allocator
    let memory_allocator = Arc::new(StandardMemoryAllocator::new_default(device.clone()));

    // Creating Buffers
    // Vertex Buffer
        // Vertex Data
    let vertex1 = VkVertex {position : [-0.5, -0.5]};
    let vertex2 = VkVertex {position : [ 0.0,  0.5]};
    let vertex3 = VkVertex {position : [ 0.5, -0.25]};

    let vertex_buffer = Buffer::from_iter(
        memory_allocator.clone(),
        BufferCreateInfo{
            usage: BufferUsage::VERTEX_BUFFER,
            ..Default::default()
        },
        AllocationCreateInfo{
            memory_type_filter: MemoryTypeFilter::PREFER_DEVICE | MemoryTypeFilter::HOST_SEQUENTIAL_WRITE,
            ..Default::default()
        },
        vec![vertex1,vertex2,vertex3],
    ).unwrap();

    // Create the image
    let image = Image::new(
        memory_allocator.clone(),
        ImageCreateInfo{
            image_type: ImageType::Dim2d,
            format: Format::R8G8B8A8_UNORM,
            extent: [1024,1024,1],
            usage: ImageUsage::TRANSFER_DST | ImageUsage::TRANSFER_SRC | ImageUsage::COLOR_ATTACHMENT,
            ..Default::default()
        },
    AllocationCreateInfo{
            memory_type_filter: MemoryTypeFilter::PREFER_DEVICE,
            ..Default::default()
        }
    ).unwrap();

    // Render Pass
    let render_pass = vulkano::single_pass_renderpass!(
        device.clone(),
        attachments: {
            color: {
                format: Format::R8G8B8A8_UNORM,
                samples: 1,
                load_op: Clear,
                store_op: Store,
            },
        },
        pass: {
            color: [color],
            depth_stencil: {},
        },
    ).unwrap();

    // Enter the render pass
    let view = ImageView::new_default(image.clone()).unwrap();
    let framebuffer = Framebuffer::new(render_pass.clone(),
        FramebufferCreateInfo{
            attachments:vec![view],
            ..Default::default()
        }).unwrap();


    // Graphics Pipeline
    let vs = vs::load(device.clone()).expect("Failed to create shader module");
    let fs = fs::load(device.clone()).expect("Failed to create shader module");

    let viewport = Viewport{
        offset: [0.0,0.0],
        extent: [1024.0,1024.0],
        depth_range: 0.0..=1.0,
    };

    let pipeline = {
        let vs = vs.entry_point("main").unwrap();
        let fs = fs.entry_point("main").unwrap();

        let vertex_input = VkVertex::per_vertex().definition(&vs.info().input_interface).unwrap();

        let stages = [
            PipelineShaderStageCreateInfo::new(vs),
            PipelineShaderStageCreateInfo::new(fs),
        ];

        let layout = PipelineLayout::new(
            device.clone(),
        PipelineDescriptorSetLayoutCreateInfo::from_stages(&stages)
                .into_pipeline_layout_create_info(device.clone()).unwrap()
            ).unwrap();

        let subpass = Subpass::from(render_pass.clone(), 0).unwrap();

        GraphicsPipeline::new(device.clone(), None,
            GraphicsPipelineCreateInfo{
                stages: stages.into_iter().collect(),
                vertex_input_state: Some(vertex_input),
                input_assembly_state: Some(InputAssemblyState::default()),
                viewport_state: Some(ViewportState{
                    viewports: [viewport].into_iter().collect(),
                    ..Default::default()
                }),
                rasterization_state: Some(RasterizationState::default()),
                multisample_state: Some(MultisampleState::default()),
                color_blend_state: Some(ColorBlendState::with_attachment_states(
                    subpass.num_color_attachments(),
                    ColorBlendAttachmentState::default(),
                )),
                subpass: Some(subpass.into()),
                ..GraphicsPipelineCreateInfo::layout(layout)
            }).unwrap()
    };

    //Command Buffer
    let command_buffer_allocator = StandardCommandBufferAllocator::new(
        device.clone(),
        StandardCommandBufferAllocatorCreateInfo::default());

    let mut builder = AutoCommandBufferBuilder::primary(
        &command_buffer_allocator,
        queue.queue_family_index(),
        CommandBufferUsage::OneTimeSubmit,
    )
    .unwrap();

    let buf = Buffer::from_iter(memory_allocator.clone(),
    BufferCreateInfo{
        usage: BufferUsage::TRANSFER_DST,
        ..Default::default()
    },
    AllocationCreateInfo {
        memory_type_filter: MemoryTypeFilter::PREFER_HOST | MemoryTypeFilter::HOST_RANDOM_ACCESS,
        ..Default::default()
    },
    (0..1024 * 1024 * 4).map(|_| 0u8)).expect("Failed to create buffer");


    // Draw Mode!
    builder.begin_render_pass(
        RenderPassBeginInfo{
            clear_values: vec![Some([0.929,0.929,0.886,1.0].into())],
            ..RenderPassBeginInfo::framebuffer(framebuffer.clone())
        },
        SubpassBeginInfo{
            contents: SubpassContents::Inline,
            ..Default::default()
        })
        .unwrap()
        .bind_pipeline_graphics(pipeline.clone()).unwrap()
        .bind_vertex_buffers(0, vertex_buffer.clone()).unwrap()
        .draw(3, 1, 0, 0).unwrap()
        .end_render_pass(SubpassEndInfo::default()).unwrap()
        .copy_image_to_buffer(CopyImageToBufferInfo::image_buffer(image, buf.clone())).unwrap();

    let command_buffer = builder.build().unwrap();

    let future = sync::now(device.clone()).then_execute(queue.clone(), command_buffer).unwrap()
        .then_signal_fence_and_flush().unwrap();
    future.wait(None).unwrap();

    let buffer_content = buf.read().unwrap();
    let image = ImageBuffer::<Rgba<u8>, _>::from_raw(1024, 1024, &buffer_content[..]).unwrap();
    image.save("image.png").unwrap();




}