current_users = ['Ronald','Lemon','Shark','Devon','Ziggy']
current_users_lowered = []
new_users = ['Hannibal', 'ZIGGY', 'Steel','Amber','ronald']

for current_user in current_users:
    current_users_lowered.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lowered:
        print(f"{new_user} is already taken. Please enter another name.")
    else:
        print(f"{new_user} is available!")
