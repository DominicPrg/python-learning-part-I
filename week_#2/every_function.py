#The goal of this program is to practice every function mentioned in this chapter involving lists.
#List of functions: append(), insert(), del, pop(), remove(), sort(), sort(reverse=True), sorted(), 
#                   sorted(value, reverse=True), reverse(), len()

romance_languages = ['Spanish', 'French', 'Italian', 'Portuguese', 'Romanian']

#Print the list in its original order.
print(f"{romance_languages}\n")

#Print the list in reverse order. I have to reverse the list prior to printing as opposed to reversing it
#in the f-string. Otherwise, it returns a value of 'None'.
romance_languages.reverse()
print(f"{romance_languages}\n")

#Temporarily sort the list (without changing the value)
print(f"{sorted(romance_languages)}\n")

#Temporarily sort the list in reverse (without altering the list)
print(f"{sorted(romance_languages, reverse=True)}\n")

#Print the list again normally to confirm it hasn't been altered (original is in reverse from earlier).
print(f"{romance_languages}\n")

#Append a language and print the list.
romance_languages.append('Latin')
print(f"{romance_languages}\n")

#Insert a language into the list and print the list.
romance_languages.insert(1, 'Catalan')
print(f"{romance_languages}\n")

#Print the length of the list.
print(f"There are at least {len(romance_languages)} romance languages that exist.\n")

#Pop an element from the list and print it. Print the list to confirm that the element has been removed.
popped_lan = romance_languages.pop()
print(f"{popped_lan} is the oldest of the romance languages, and is considered dead.")
print(f"{romance_languages}\n")

#Delete a random language from the list. Print the list to confirm it's been deleted. 
#Save the element in a variable to insert it back later.
lan_to_be_appended_1 = romance_languages[2]
del romance_languages[2]
print(f"{romance_languages}\n")

#Remove a specific language from the list. Save the element in a variable to insert it back later.
#Print the list to confirm it's been removed.
lan_to_be_appended_2 = 'Romanian'
romance_languages.remove('Romanian')
print(f"{romance_languages}\n")

#Append popped_lan, lan_to_be_appended_1, and lan_to_be_appended_2.
#Print the list to confirm that they've been appended.
romance_languages.append(popped_lan)
romance_languages.append(lan_to_be_appended_1)
romance_languages.append(lan_to_be_appended_2)
print(f"{romance_languages}\n")

#Sort the list in reverse alphabetical order. Print the list to confirm it's been sorted 
#in reversed alphabetical order.
romance_languages.sort(reverse=True)
print(f"{romance_languages}\n")

#Sort the list in alphabetical order. Print the list to confirm it's been sorted alphhabetically.
romance_languages.sort()
print(f"{romance_languages}")
