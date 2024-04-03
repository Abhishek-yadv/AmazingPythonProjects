import lyricsgenius as lg
# Function to fetch lyrics and write them to a file
def get_lyrics(arr, max_song, file):
    """
    Returns: Number of songs grabbed by Function
    Saves : Text File with Lyrics
    Parameters :
    arr : Artist
    max_song : Number of maximum songs to be grabbed
    """
    # Acquire a Access Token to connect with Genius API
    genius = lg.Genius(
        '6_RDOwOGyAk1t_VyEB_UuWfIQKpatD2r65O1lpslCxSZ_CEf3XvGEBAg44uiX7rR',
        # Skip song listing
        skip_non_songs=True,
        # Terms that are redundant song names with same lyrics, e.g. Old Town Road and Old Town Road Remix have same lyrics
        excluded_terms=["(Remix)", "(Live)"],
        # In order to keep headers like [Chorus], [Bridge] etc.
        remove_section_headers=True
    )

    # Write lyrics of k songs by each artist in arr
    c = 0
    # A counter
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=max_song, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            # customised delimiter
            file.write("\n \n  \n \n".join(s))
            c += 1
            print(f"Songs grabbed: {len(s)}")
        except Exception as e:
            print(f"Some exception at {name}: {e}")

    return c


# File for writing the Lyrics
filename = input('Enter a filename: ').strip() or 'Lyrics.txt'
file = open(filename, "w+", encoding="utf-8")

# List of Artist and Maximum Songs
input_string = input("Enter name of Artists separated by spaces: ")
artists = input_string.split()

# Call the function to fetch lyrics and save them to the file
num_songs_grabbed = get_lyrics(artists, 3, file)
file.close()

print(f"Total songs grabbed: {num_songs_grabbed}")
print("Lyrics saved successfully!")
