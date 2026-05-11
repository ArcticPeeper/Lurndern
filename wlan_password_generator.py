import random
import string

length = 9
chars = ['@', '!', '#', '$', '%', '*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
year = [2025, 2026]

with open("usernames.txt", "r") as usernames_file:
    usernames = usernames_file.read().splitlines()
    for i in range(len(usernames)):
        #print(usernames[i], random.choice(chars), random.choice(year))
        for j in range(100):
            ### print(usernames[i].replace(random.choice(usernames[i]), random.choice(chars)), random.choice(year))
            random_password_with_username = f'{usernames[i].replace(random.choice(usernames[i]), random.choice(chars))}' + f'{random.choice(year)}'
            print(random_password_with_username)

            random_password = ''.join(random.choice(chars) for i in range(length))
            ###print(random_password)
