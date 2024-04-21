mod gameset;
mod score_calculator;

use std::io;
use gameset::Gameset;

use crate::score_calculator::calculate_word_score;

fn main() {
    let stdin = io::stdin();
    let mut answer = String::new();
    let puzzle = Gameset::new_from_wordset(
        String::from("Going up!"), 
        vec![
            "Lift".to_string(),
            "Balloon".to_string(),
            "Stocks".to_string(),
            "Plane".to_string()
        ]
    );
    let mut guesses = puzzle.word_set.len();
    let mut score = 0;
    loop {
        if guesses <= 0 {
            //Game Over
            break;
        }
        // Draw Screen
        std::process::Command::new("clear").status().unwrap(); // Clear Screen
        println!("************************************");
        println!("**        Today's Theme:          **");
        println!("**            {}           **", puzzle.theme);
        println!("**        Points Target:          **");
        println!("**            {}                  **", puzzle.point_target);
        println!("************************************");
        println!("Avaliable Characters: {:?}", puzzle.character_list);
        println!("------------------------------------");
        println!("Guesses: {}    |   Current Score: {}", guesses, score);
        println!("------------------------------------");
        
        // Input
        answer.clear();
        println!("Write a word!"); 
        stdin.read_line(&mut answer).unwrap();
        println!("{:?}", answer.chars());
        // Check if input is valid
        if answer.chars().all(|x| x.is_alphabetic()) {
            let mut valid = true;
            for char in answer.to_lowercase().chars() {
                if !puzzle.character_list.contains(&char) {
                    valid = false;
                }
            }
            if valid {
                let points = calculate_word_score(&answer);
                score += points;
                println!("You got {} points!", points);
                guesses -= 1;
            } else {
                println!("Word contains invalid letter")
            }
        } else {
            println!("Answers can only contain letters.")
        }
        stdin.read_line(&mut answer).unwrap(); // Pause
    }

}
