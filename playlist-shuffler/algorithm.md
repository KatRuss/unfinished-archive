# Algorithm concept
    1. All songs in the playlist are given an equal bias rating.
    2. Choose a song at random with those biases
    3. All songs from the same artists has their bias rating knocked down slightly (double if it's from the same album)
    4. Songs that have not been played yet gets a minor bonus.
    5. Choose a new song at random from the updated biases.
    6. If all songs played (or user presses 'reshuffle' button), reset biases.

# Song Struct
    - Name
    - Artist
    - Album
    - Song Length (seconds)
    - mp4 file location
