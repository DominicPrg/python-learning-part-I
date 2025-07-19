# Write a function called make_shirt() that accepts a size and the text of a 
# message that should be printed on the shirt. The function should print a 
# sentence summarizing the size of the shirt and the message printed on it.

def make_shirt(size, message):
    print(f"\nSize: {size}")
    print(f"Message: {message}")

shirt_size = 'Medium'
shirt_message = "This shirt is highly antique. I love it!"

make_shirt(shirt_size,shirt_message)
make_shirt(message=shirt_message,size=shirt_size)
