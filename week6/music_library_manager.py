songs = []
genre_count = {}

"""
MANUAL INPUTS
song1 = input("")
song2 = input("")
song3 = input("")

 """
# with the use of loops

for song_inputs in range(1, 6, 1):
# range(start,stop,step) step default is 1. having stop at 6 means you're asking for 5
    song = input(f"Input song {song_inputs}: ")
    genre = input(f"What genre is this song : ")
    print()

    # putting the values into dict
    mysong_dict = {
        "song" : song,
        "genre" : genre
    }
    # append because "songs" is a list
    songs.append(mysong_dict)
    
    # using get function and defining genre as starting from 0
    genre_count[genre] = genre_count.get(genre, 0)+ 1

print(genre_count)



