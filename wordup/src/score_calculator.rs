

pub fn calculate_list_score(word_list: &Vec<String>) -> i32{
    let mut result = 0;
    for word in word_list.into_iter() {
        result += calculate_word_score(word)
    }
    result
}

pub fn calculate_word_score(word: &String) -> i32 {
    let test_word = word.to_lowercase();
    let mut result = 0;
    for char in test_word.chars() {
        let mut score = 0;
        match char {
            'z' | 'q' => score += 10,
            'j' | 'x' => score += 8,
            'k' => score += 5,
            'f' | 'h' | 'v' | 'w' | 'y'  => score += 4,
            'b' | 'c' | 'm' | 'p' => score += 3,
            'd' | 'g' => score += 2,
             _  => score += 1,
        }
        // TODO: IF char is in the same position as it was in the previous word.
        // It's worth negative points.
        // e.g. v in 'driVe'. If it was played after leaVe, is worth -4 instaed of 4.
        result += score;
    }
    result
}