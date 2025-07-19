# Make a class called User. Create two attributes called first_name and 
# last_name, and then create several other attributes that are typically 
# stored in a user profile. Make a method called describe_user() that prints a 
# summary of the user’s information. Make another method called greet_user() 
# that prints a personalized greeting to the user. 
class User:
    """A class User:simple attempt to model a user."""


    def __init__(self, first_name, last_name, age, gender, birth_date):
        """Define the user based on first and last name, age, gender, and
        birth date."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.birth_date = birth_date
    

    def describe_user(self):
        """Describe the user based on their personal info."""
        print(f"\nFirst name: {self.first_name}\nLast name: {self.last_name}"
              f"\nAge: {self.age}\nGender: {self.gender.title()}\nBirth date: "
              f"{self.birth_date}")
    

    
    def greet_user(self):
        """Greet the user by their first and last name."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nHello, {full_name}!")
    

user_1 = User("dom", "parra", 20, "man", "8/10/2004")
user_1.describe_user()
user_1.greet_user()

user_2  = User("bernie", "anderson", 65, "man", "6/15/1960")
user_2.describe_user()
user_2.greet_user()

user_3 = User("cinthy", "margot", 12, "woman", "4/24/2013")
user_3.describe_user()
user_3.greet_user()

user_4 = User("laura", "pierce", 100, "woman", "7/07/2025")
user_4.describe_user()
user_4.greet_user()
