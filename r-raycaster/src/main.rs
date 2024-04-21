mod vec3;
mod colour;
mod ray;

use std::fs;
use colour::Colour;
use ray::Ray;
use vec3::{calculate_dot, Vec3};

fn hit_sphere(center: Vec3, radius: f64, r: &Ray) -> f64{
    let oc = r.origin - center;
    let a = r.direction.length_squared();
    let half_b = calculate_dot(&oc, &r.direction);
    let c = oc.length_squared() - radius*radius;
    let discriminant = half_b*half_b - a*c;

    if discriminant < 0.0 {
        return -1.0;
    } else {
        return (-half_b - discriminant.sqrt()) / a;
    }

}

fn ray_colour(r: Ray) -> Colour{
    let t = hit_sphere(Vec3{x:0.0,y:0.0,z:-1.0}, 0.5, &r);
    if t > 0.0 {
        let n = (r.at(t) - Vec3{x: 0.0, y: 0.0, z: -1.0}).unit_vector();
        let normal_colour = Colour{value:Vec3{x: n.x+1.0, y: n.y+1.0, z: n.z+1.0}*0.5};
        return normal_colour;

    }

    let unit_direction = r.direction.unit_vector();
    let a = 0.5*(unit_direction.y + 1.0);

    let light_colour = Colour{value: Vec3 { x: 1.0, y: 1.0, z: 1.0 }};
    let dark_colour = Colour{value: Vec3 { x: 0.5, y: 0.7, z: 1.0 }};

    return Colour{value: (light_colour.value*(1.0-a)) + (dark_colour.value*a)};
}

fn main() {
    // Image
    let aspect_ratio = 16.0 / 9.0;
    let image_width = 400;
    let image_height = ((image_width as f64 / aspect_ratio) as i32).max(1);

    let data = render(image_width, image_height).unwrap();
    create_file(data);
    println!(" | Done :3")

}

fn render(image_width: i32, image_height: i32) -> Result<String,u8> {
    let mut data_string = String::new(); // String the ppm data will be passed to

    let focal_length = 1.0;
    let viewport_height = 2.0;
    let viewport_witdth = viewport_height * (image_width as f64 / image_height as f64);
    let camera_center = Vec3{x: 0.0, y: 0.0, z: 0.0};

    // Calculate the vectors across the horizontal and down the vertical viewport edges.
    let viewport_u = Vec3{x: viewport_witdth, y: 0.0, z: 0.0};
    let viewport_v = Vec3{x: 0.0, y: -viewport_height, z: 0.0};

    // Calculate the horizontal and vertical delta vectors from pixel to pixel.
    let pixel_delta_u = viewport_u / image_width as f64;
    let pixel_delta_v = viewport_v / image_height as f64;

    // Calculate the location of the upper left pixel.
    let viewport_upper_left = camera_center - Vec3{x:0.0,y:0.0,z: focal_length} - viewport_u/2.0 - viewport_v/2.0;
    let pixel00 = viewport_upper_left + (pixel_delta_u + pixel_delta_v) * 0.5;


    // Render
    data_string.push_str(&format!("P3\n{} {}\n255\n", image_width, image_height));
    for j in 0..image_height {
        println!(" | Scanlines Remaining: {}", image_height - j);
        for i in 0..image_width {
            let pixel_center = pixel00 + (pixel_delta_u * i as f64) + (pixel_delta_v * j as f64);
            let ray_direction = pixel_center - camera_center;
            let r = Ray{origin: camera_center, direction: ray_direction};
            ray_colour(r).write(&mut data_string);
        }
    }

    return Ok(data_string);
}

fn create_file(data: String) {
    println!(" | Writing to file...");
    fs::write("image.ppm", data).unwrap();
}