# Make two files, cats.txt and dogs.txt. Store at least three names of cats in 
# the first file and three names of dogs in the second file. Write a program 
# that tries to read these files and print the contents of the file to the 
# screen. Wrap your code in a try-except block to catch the FileNotFound
# error, and print a friendly message if a file is missing. Move one of the
# files to a different location on your system, and make sure the code in
# the except block executes properly.

from pathlib import Path

try:
    cats_path = Path('chapter_10/cats_and_dogs/cats.txt')
    cat_names = cats_path.read_text()
except FileNotFoundError:
    print(f"Sorry, the names of the cats couldn't be found.")
else:
    print("Cats:")
    for cat_name in cat_names.splitlines():
        print(f"  -{cat_name}")

try:
    dogs_path = Path('chapter_10/cats_and_dogs/dogs.txt')
    dog_names = dogs_path.read_text()
except FileNotFoundError:
    print("Sorry, the names of the dogs couldn't be found.")
else: 
    print("Dogs:")
    for dog_name in dog_names.splitlines():
        print(f"  -{dog_name}")
