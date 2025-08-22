# The remember_me.py example only stores one piece of information, the 
# username. Expand this example by asking for two more pieces of information 
# about the user, then store all the information you collect in a dictionary. 
# Write this dictionary to a file using json.dumps(), and read it back in using
# json.loads(). Print a summary showing exactly what your program remembers 
# about the user.

from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user information if possible."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None
    

def get_new_user_info(path):
    """Prompt for new user info."""
    user_info = {}
    user_info['username'] = input("What is your name?")
    user_info['age'] = int(input("What is your age?"))
    user_info['gender'] = input("What gender do you identify as?")
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Greet the user by name, and share their age and gender."""
    path = Path('chapter_10/user_dictionary/user_dictionary.json')
    user_info = get_stored_user_info(path)
    if user_info:
        print(f"Welcome back, {user_info['username']}!")
        print(f"You are {user_info['age']} year(s) old and identify as a "
              f"{user_info['gender'].lower()}.")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember when you return, {user_info['username']}!")

greet_user()
