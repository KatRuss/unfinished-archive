use std::{cmp::max, time::Duration};
use rand::{distributions::WeightedIndex, prelude::*};

#[derive(Eq, PartialEq, Hash, Debug)]
pub struct Song {
    pub title: String,
    pub artist: String,
    pub album: String,
    //pub duration: Duration,
}

pub struct Playlist {
    pub name: String,
    pub track_list: Vec<Song>,
}
impl Playlist {

    pub fn create_shuffled_tracklist(&self, size: i32) -> (Vec<&Song>, i32) {
        const BASE_WEIGHT: i32 = 20; // Starting Weight of all songs
        
        let mut result: Vec<&Song> = vec![];

        let mut weights = vec![BASE_WEIGHT; self.track_list.len()];
        let mut track_index = WeightedIndex::new(&weights).unwrap();
        let mut rng = thread_rng();
        let mut number_of_dupes = 0;

        for _ in 0..size {
            // Get a Song
            let index = track_index.sample(&mut rng);
            let song_to_add = &self.track_list[index];
            // Add to playlist
            if result.contains(&song_to_add){number_of_dupes+=1;}
            result.push(song_to_add);

            // Modify Index
            weights[index] = 0; // song found forced to 0 points
            for (x, song) in self.track_list.iter().enumerate() {
                if song.album == song_to_add.album{
                    weights[x] = max(weights[x] - BASE_WEIGHT, 0);
                } else if song.artist == song_to_add.artist {
                    weights[x] = max(weights[x] - BASE_WEIGHT/2, 0);
                } else if result.contains(&song) {
                    weights[x] += 1;
                } else {
                    weights[x] += BASE_WEIGHT;
                }
            }
            track_index = WeightedIndex::new(&weights).unwrap();
        }
        return (result, number_of_dupes);
    }
}
