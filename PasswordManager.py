import random
import string
import pyperclip
import sqlite3

conn = sqlite3.connect('password.db')
curr = conn.cursor()

# Check if the table already exists
curr.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='passwords'")
table_exists = curr.fetchone()

# If the table doesn't exist, create it
if not table_exists:
    curr.execute("""CREATE TABLE passwords (
                    Website text,
                    Password text
                    )""")
    conn.commit()

# Check if the settings table already exists
curr.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='settings'")
settings_table_exists = curr.fetchone()

# If the settings table doesn't exist, create it and prompt the user to set the master password
if not settings_table_exists:
    curr.execute("""CREATE TABLE settings (
                    master_password text
                    )""")
    master_password = input("Please set the master password: ")
    curr.execute("INSERT INTO settings (master_password) VALUES (?)", (master_password,))
    conn.commit()
else:
    # Retrieve the master password from the settings table
    curr.execute("SELECT master_password FROM settings")
    master_password = curr.fetchone()[0]

def generate_random_password():
    length = random.randint(15, 100) 
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
    print("Select one of the following options: ")
    print("1. Generate and Store Password\n2. View Saved Passwords\n3. Exit")
    option = input()
    
    if option == "1":
        domain = input("Please enter which website or application the password will be used for:" )
        generated_password = generate_random_password()
        curr.execute("INSERT INTO passwords VALUES (?, ?)", (domain, generated_password))
        conn.commit()
        pyperclip.copy(generated_password)
        print("Randomly generated password has been copied to clipboard.")
    elif option == "2":
        print("Please enter the master password: ")
        attempt = 0
        while attempt < 3:
            user_password = input()
            if check_password(user_password) == True:
                curr.execute("SELECT * FROM passwords")
                print(curr.fetchall())
                break
            else:
                print("Password incorrect. x attempts remaining.")
                attempt += 1
                if attempt == 3:
                    print("Maximum attempts exceeded. Terminating program.")
                    exit()
    elif option == "3":
        conn.close()
        print("Thank you for using PassVault.")
        loop = False
    else:
        print("Please enter a valid option.")
