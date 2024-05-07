import random
import string

def generate_random_password():
    length = random.randint(8, 100) 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("PASSWORD MANAGER")

loop = True

while loop:
    # display options for user

    print("Select one of the following options: ")
    print("1. Generate and Store Password\n2. View Saved Passwords\n3. Exit")
    # user input one of follwing options
    option = input()
    if option == "1":
        password = generate_random_password()
        print(password)
    elif option == "2":
        print("2")
    elif option == "3":
        loop = False
    else:
        print("Please enter a valid option.")
        
