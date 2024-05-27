# Required libraries
import random
import string
import pyperclip
import sqlite3

# Global constant variables
MAX_ATTEMPTS = 3

# Functions
def generate_random_password():
    length = random.randint(15, 25) 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))        # make sure this satisfies most password criteria, e.g. 2 captial letters, special character, etc.
    return password

def store_password():
    domain = input("Please enter which website or application the password will be used for: " )
    # generate a random password and store into database under domain name
    generated_password = generate_random_password()
    curr.execute("INSERT INTO passwords VALUES (?, ?)", (domain, generated_password))
    conn.commit()
    # copy to clipboard so it can immediately be pasted
    pyperclip.copy(generated_password)
    print("Randomly generated password has been copied to clipboard.")
#
#   create a check to make sure that a password for application does not already exist
#

def update_password():
    domain = input("Please enter the website that you wish to update the password for: ")
    
    # Check if the domain exists in the database
    curr.execute("SELECT * FROM passwords WHERE Website=?", (domain,))
    result = curr.fetchone()
    
    if result:
        # Generate a new random password
        new_password = generate_random_password()
        
        # Update the password in the database
        curr.execute("UPDATE passwords SET Password=? WHERE Website=?", (new_password, domain))
        conn.commit()
        
        # Copy the new password to the clipboard
        pyperclip.copy(new_password)
        print("Password updated successfully. The new password has been copied to the clipboard.")
    else:
        print("No entry found for the specified website.")

def delete_password():
    domain = input("Please enter the website that you wish to delete the password for: ")
    
    # Check if the domain exists in the database
    curr.execute("SELECT * FROM passwords WHERE Website=?", (domain,))
    result = curr.fetchone()
    
    if result:
        # Delete the password entry from the database
        curr.execute("DELETE FROM passwords WHERE Website=?", (domain,))
        conn.commit()
        print("Password for '{}' has been deleted.".format(domain))
    else:
        print("No entry found for the specified website.")




def check_password(user_password):
    if user_password == master_password:
        return True
    else:
        return False


def view_password():
    attempt = 0

    while attempt < MAX_ATTEMPTS:
        user_password = input("Please enter the master password: ")
        if check_password(user_password) == True: # if empty return 
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
                
# Start of program
print(r"""
  _  __                  ____                             _ 
 | |/ /   ___   _   _   / ___|  _   _    __ _   _ __   __| |
 | ' /   / _ \ | | | | | |  _  | | | |  / _` | | '__| / _` |
 | . \  |  __/ | |_| | | |_| | | |_| | | (_| | | |   | (_| |
 |_|\_\  \___|  \__, |  \____|  \__,_|  \__,_| |_|    \__,_|
                |___/  
""")

# Create database using sqlite3
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
    # Print menu with options for user
    print("Select one of the following options: ")
    option = input("1. Generate and Store Password\n2. View Passwords\n3. Exit\n")
    
    if option == "1":
        store_password()
        

    elif option == "2":
        sub_option = input("Select one of the following options:\n1. View Passwords\n2. Change Password\n3. Delete Password\n4. Back...\n")
        
        # Sub-menu of options
        if sub_option == "1":
            view_password()
        elif sub_option == "2":
            update_password()
        elif sub_option == "3":
            delete_password()
        elif sub_option == "4":
            continue

    elif option == "3":
        conn.close()
        print("Thank you for using KeyGuard.")
        loop = False

    else:
        print("Please enter a valid option.")


