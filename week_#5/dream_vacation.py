# Write a program that polls users about their dream vacation. Write a prompt 
# similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

dream_vacations = {}
prompt_name = "\nWhat is your name?"
prompt_destination = "\nIf you could visit one place in the world, where " \
                     "would you go?" 
poll_active = True

while poll_active:
    name = input(prompt_name)
    dream_destination = input(prompt_destination)
    dream_vacations[name] = dream_destination

    proceed = input("\nWould you like to ask another person to take the poll?"\
                    " (yes/no): ")
    if proceed == "no":
        poll_active = False

print("\n--- Poll Results ---")
for name, destination in dream_vacations.items():
    print(f"\n{name} would like to visit {destination}!")
