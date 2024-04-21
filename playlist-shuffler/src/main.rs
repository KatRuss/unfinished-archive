mod song;
use song::{Song, Playlist};

fn main() {
    let p = Playlist{name: "My Playlist".to_string(), track_list: vec![
        Song{title: "all-american bitch".to_string(),           artist: "Olivia Rodrigo".to_string(),           album: "GUTS".to_string()},
        Song{title: "bad idea right?".to_string(),              artist: "Olivia Rodrigo".to_string(),           album: "GUTS".to_string()},
        Song{title: "brutal".to_string(),                       artist: "Olivia Rodrigo".to_string(),           album: "SOUR".to_string()},
        Song{title: "good 4 u".to_string(),                     artist: "Olivia Rodrigo".to_string(),           album: "SOUR".to_string()},
        Song{title: "Dissocia".to_string(),                     artist: "Glytsh".to_string(),                   album: "Dissocia".to_string()},
        Song{title: "HOAX".to_string(),                         artist: "Glytsh".to_string(),                   album: "HOAX".to_string()},
        Song{title: "V.H.S (Vulgar Holy Spirit".to_string(),    artist: "Glytsh".to_string(),                   album: "VHS".to_string()},
        Song{title: "Six Shooter".to_string(),                  artist: "Queens of the Stone Age".to_string(),  album: "Songs for the Deaf".to_string()},
        Song{title: "Buddy Holly".to_string(),                  artist: "Weezer".to_string(),                   album: "Weezer (Blue Album)".to_string()},
        Song{title: "10".to_string(), artist: "e".to_string(), album: "e1".to_string()},
        Song{title: "11".to_string(), artist: "e".to_string(), album: "e1".to_string()},
        Song{title: "12".to_string(), artist: "e".to_string(), album: "e2".to_string()},
        Song{title: "13".to_string(), artist: "e".to_string(), album: "e3".to_string()},
        Song{title: "14".to_string(), artist: "f".to_string(), album: "f1".to_string()},
        Song{title: "15".to_string(), artist: "f".to_string(), album: "f1".to_string()},
        Song{title: "16".to_string(), artist: "g".to_string(), album: "g1".to_string()},
        Song{title: "17".to_string(), artist: "g".to_string(), album: "g1".to_string()},
        Song{title: "18".to_string(), artist: "h".to_string(), album: "h1".to_string()},
        Song{title: "19".to_string(), artist: "i".to_string(), album: "i1".to_string()},
        Song{title: "20".to_string(), artist: "j".to_string(), album: "j1".to_string()},
        ]};
    let shuffle = p.create_shuffled_tracklist(20);
    println!("{} shuffle:",p.name);
    for (x,song) in shuffle.0.iter().enumerate(){
        println!("{}: {} by {} (album: {})",x+1,song.title, song.artist, song.album);
    }
    println!("Number of dupes: {}", shuffle.1);
}
