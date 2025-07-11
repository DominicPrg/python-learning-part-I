# Start with your program from Exercise 8-7. Write a while loop that allows 
# users to enter an album’s artist and title. Once you have that information, 
# call make_album() with the user’s input and print the dictionary that’s 
# created. Be sure to include a quit value in the while loop. 

def make_album(artist, album_title, num_songs = None):
    album = {
        'Title':album_title.title(),
        'Artist':artist.title(),
    }

    if num_songs:
        album['Number of Songs'] = num_songs

    return album

prompt = "Enter the title, artist, and (optionally) the number of songs in" \
         " the album.\nEnter 'q' at anytime to quit the program."

while True:
    print(f"\n{prompt}")

    album_name = input("Enter the name of the album: ")
    if (album_name == 'q'):
        break

    album_artist = input("Enter the artist of the album: ")
    if (album_artist == 'q'):
        break

    add_song_count = input("Would you like to enter the number of songs in " \
                           "the album? (y/n/q): ")
    if add_song_count == 'y':
        song_count = input("Enter number of songs: ")
        song_count = int(song_count)
        album = make_album(artist = album_artist, album_title = album_name,
                           num_songs = song_count)
    elif add_song_count == 'n':
        album = make_album(artist = album_artist, album_title = album_name)
    elif add_song_count == 'q':
        break

    print(f"\n{album}")
