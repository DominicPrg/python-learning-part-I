# Ask the user for a number, and then report whether the number is a multiple 
# of 10 or not.

num = input("Enter a number: ")
num = int(num)

if num % 10 == 0:
    print(f"\n{num} is a multiple of 10!")
else:
    print(f"\n{num} is NOT a multiple of 10.")
