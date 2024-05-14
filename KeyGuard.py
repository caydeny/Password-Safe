import random
import string
import pyperclip
import sqlite3

MAX_ATTEMPTS = 3

def generate_random_password():
    length = random.randint(15, 25) 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password(user_password):
    if user_password == master_password:
        return True
    else:
        return False
    
print(r"""
  _  __                  ____                             _ 
 | |/ /   ___   _   _   / ___|  _   _    __ _   _ __   __| |
 | ' /   / _ \ | | | | | |  _  | | | |  / _` | | '__| / _` |
 | . \  |  __/ | |_| | | |_| | | |_| | | (_| | | |   | (_| |
 |_|\_\  \___|  \__, |  \____|  \__,_|  \__,_| |_|    \__,_|
                |___/  
""")

# create database using sqlite3
conn = sqlite3.connect('password.db')
curr = conn.cursor()

# check if the table already exists
curr.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='passwords'")
table_exists = curr.fetchone()

# create table if it does not already exist
if not table_exists:
    curr.execute("""CREATE TABLE passwords (
                    Website text,
                    Password text
                    )""")
    conn.commit()

# check if the settings table already exists
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









loop = True

while loop:
    print("Select one of the following options: ")
    print("1. Generate and Store Password\n2. View Saved Passwords\n3. Exit")
    option = input()
    
    if option == "1":

        domain = input("Please enter which website or application the password will be used for: " )
        # generate a random password and store into database under domain name
        generated_password = generate_random_password()
        curr.execute("INSERT INTO passwords VALUES (?, ?)", (domain, generated_password))
        conn.commit()
        # copy to clipboard so it can immediately be pasted
        pyperclip.copy(generated_password)
        print("Randomly generated password has been copied to clipboard.")

    elif option == "2":

        attempt = 0

        while attempt < MAX_ATTEMPTS:
            user_password = input("Please enter the master password: ")
            if check_password(user_password) == True:
                # fetch all passwords saved and print
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
        print("Thank you for using KeyGuard.")
        loop = False
    else:
        print("Please enter a valid option.")
