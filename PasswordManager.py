import random
import string
import pyperclip

master_password = "12345"

def generate_random_password():
    length = random.randint(8, 100) 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password(user_password):
    if user_password == master_password:
        return True
    else:
        return False

print("PASSWORD MANAGER")

loop = True

while loop:
    # display options for user

    print("Select one of the following options: ")
    print("1. Generate and Store Password\n2. View Saved Passwords\n3. Exit")
    # user input one of follwing options
    option = input()
    
    if option == "1":
        
        print("Please enter which website or application the password will be used for:")
        domain = input()
        generated_password = generate_random_password()
        # copys generated password to clipboard
        pyperclip.copy(generated_password)
        
        print("Randomly generated password has been copied to clipboard.")
    elif option == "2":
        print("Please enter the master password: ")
        
        attempt = 0
        while attempt < 3:
            user_password = input()
            if check_password(user_password) == True:
                print("Password matches.")
                break
            else:
                print("Password incorrect. x attempts remaining.")
                attempt += 1
                if attempt == 3:
                    print("Maximum attempts exceeded. Terminating program.")
                    exit()
        
    elif option == "3":
        loop = False
    else:
        print("Please enter a valid option.")
        
