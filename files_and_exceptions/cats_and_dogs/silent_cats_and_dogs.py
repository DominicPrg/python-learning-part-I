# Modify your except block in Exercise 10-8 to fail silently if either file is 
# missing.

from pathlib import Path

try:
    cats_path = Path('chapter_10/cats_and_dogs/cats.txt')
    cat_names = cats_path.read_text()
except FileNotFoundError:
    pass
else:
    print("Cats:")
    for cat_name in cat_names.splitlines():
        print(f"  -{cat_name}")

try:
    dogs_path = Path('chapter_10/cats_and_dogs/dogs.txt')
    dog_names = dogs_path.read_text()
except FileNotFoundError:
    pass
else: 
    print("Dogs:")
    for dog_name in dog_names.splitlines():
        print(f"  -{dog_name}")
