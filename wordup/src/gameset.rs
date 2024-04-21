use std::char;
use chrono::prelude::*;
use crate::score_calculator::calculate_list_score;

// Holds the information of the individual puzzles made in the game. 
pub struct Gameset {
    pub theme: String,
    pub word_set: Vec<String>,
    pub point_target: i32,
    pub date: DateTime<Utc>,
    pub character_list: Vec<char>,
}
impl Gameset {
    pub fn new_from_wordset(theme: String, word_set: Vec<String>) -> Self {
        Self { 
            theme: theme, 
            word_set: word_set.clone(), 
            point_target: calculate_list_score(&word_set), 
            date: Utc::now(),
            character_list: Gameset::get_characters_from_set(&word_set),
        }
    }

    fn get_characters_from_set(word_set: &Vec<String>) -> Vec<char> {
        let mut chars = Vec::new();
        for word in word_set {
            for char in word.to_lowercase().chars() {
                if !chars.contains(&char) {
                    chars.push(char);
                }
            }
        }
        chars
    }
}