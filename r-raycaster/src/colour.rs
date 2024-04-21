use crate::vec3::Vec3;


#[derive(Debug)]
pub struct Colour {
    pub value: Vec3 // x = red, y = green, z = blue
}
impl Colour {
    pub fn write(self,data_string: &mut String) {

        let ir = (255.99 * self.value.x) as i32;
        let ig = (255.99 * self.value.y) as i32;
        let ib = (255.99 * self.value.z) as i32;

        data_string.push_str(&format!("{} {} {}\n", ir, ig, ib));
    }
}