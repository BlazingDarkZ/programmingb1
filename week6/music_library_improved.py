music_library = []
favorite_library = []

def initial_menu():
    print("Welcome to Music Library Manager!" + "")
    if len(music_library) == 0:
       initial_songs()
       library_menu()
    else:
       print("u alr have songs :3")
       library_menu()

def library_menu():
   print("Would you like to add more songs?")
   while True: 
    yes_add_song = input("yes/no")
    if yes_add_song == "yes":
       add_library()
    else:
       print("try again")
       

def initial_songs():
     print("u dont have songs! lets add some..." + "\n")
     for i in range(1,3,1):
      add_library(music_library)
    

def add_library(library): 
    title = input("Title: ") 
    artist = input("Artist: ") 
    genre = input("Genre: ") 
     
    library.append({ "title": title, "artist": artist, "genre": genre})

initial_menu()
"""
initial_menu()
print(music_library)
print("=" * 20)
print(favorite_library)

def menu():

    answer = input("what")
    if answer == "a":
        add_library(favorite_library)
    else:
        print("bruh")"""