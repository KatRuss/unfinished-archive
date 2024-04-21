use std::ops::{Add, Div, Mul, Neg, Sub};

#[derive(Debug, Clone, Copy)]
pub struct Vec3{
    pub x: f64,
    pub y: f64,
    pub z: f64
}
impl Vec3 {
    pub fn length_squared(self) -> f64 {
        self.x*self.x + self.y*self.y + self.z*self.z
    }

    pub fn length(self) -> f64 {
        self.length_squared().sqrt()
    }

    pub fn unit_vector(self) -> Vec3 {
        self / self.length()
    }
}
impl Add for Vec3 {
    type Output = Vec3;
    fn add(self, other: Vec3 ) -> Self::Output {
        Vec3{
            x: self.x + other.x,
            y: self.y + other.y,
            z: self.z + other.z
        }
    }
}
impl Add<f64> for Vec3 {
    type Output = Vec3;
    fn add(self, other: f64 ) -> Self::Output {
        Vec3{
            x: self.x + other,
            y: self.y + other,
            z: self.z + other
        }
    }
}
impl Sub for Vec3 {
    type Output = Vec3;
    fn sub(self, other: Vec3 ) -> Self::Output {
        self + -other
    }
}
impl Sub<f64> for Vec3 {
    type Output = Vec3;
    fn sub(self, other: f64 ) -> Self::Output {
        self + -other
    }
}
impl Neg for Vec3 {
    type Output = Vec3;
    fn neg(self) -> Self::Output {
        Vec3{
            x: -self.x,
            y: -self.y,
            z: -self.z
        }
    }
}
impl Mul<f64> for Vec3 {
    type Output = Vec3;
    fn mul(self, other: f64 ) -> Self::Output {
        Vec3{
            x: self.x * other,
            y: self.y * other,
            z: self.z * other
        }
    }
}
impl Div<f64> for Vec3 {
    type Output = Vec3;
    fn div(self, other: f64 ) -> Self::Output {
        self * (1.0/other)
    }
}

// ======================
// == HELPER FUNCTIONS ==
// ======================
pub fn calculate_dot(u : &Vec3, v: &Vec3) -> f64 {
   (u.x * v.x) + (u.y * v.y) + (u.z * v.z)
}
