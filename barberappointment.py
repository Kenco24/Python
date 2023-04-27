import hashlib
import json
import time 
import os

# Load user data from file
with open("users.json", "r") as f:
    users = json.load(f)

# Function to save user data to file
def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f)

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register():
    while True:
            
        username = input("[type 'exit' to go back, case does not matter ] Enter a username: ")
        if username.lower()== "exit":
            print("Registration canceled.")
            break
        elif username in users:
            print("\n   ***  Username already taken!  ***  \n")
        
        else:   
            password = input("Enter a password: ")
            hashed_password = hash_password(password)
            users[username] = {
                "password": hashed_password,
                "appointments": [],
                "time_created": time.time()
            }
            save_users()
            print("User registered successfully.")
            break

# Function to authenticate a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    if users.get(username) and users[username]["password"] == hashed_password:
        print("\nLogin successful.")
        return username
    else:
        print("Incorrect username or password.")
        return None

# Function to create an appointment
def create_appointment():
    date = input("Enter the date of the appointment (format: HH:MM,AM/PM,Day): ")
    return date

def display_appointments(username):
    if users[username]["appointments"]:
        print("\nYour current appointments are:\n--------------------")
        for i, appointment in enumerate(users[username]["appointments"]):
            print("{} - {}".format(i+1, appointment))
        print("--------------------")
    else:
        print("You have no appointments.")
# Main program loop

def cancel_appointment(username):
    if users[username]["appointments"]:
        print("Your current appointments are:")
        try: 
            index = int(input("Enter the index of the appointment to cancel: ")) - 1
            if 0 <= index < len(users[username]["appointments"]):
                del users[username]["appointments"][index]
                save_users()
                print("Appointment canceled.")
        except:
            print("Error")
        else:
            print("Invalid index.")
    else:
        print("You have no appointments.")
        
def show_account_details(username):
    user_data = users[username]
    print("|------------------------------------------|")
    print(" Username: {} ".format(username))
    print(" Time created: {}".format(time.ctime(user_data["time_created"])))
    print(" Number of appointments: {}".format(len(user_data["appointments"])))
    print("|------------------------------------------|")
    
while True:
    
    print("\n------------------------------")
    print("||   1. Register new user   ||")
    print("||   2. Login               ||")
    print("||   3. Exit                ||")
    print("------------------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        username = login()
        if username:
            print("Welcome, {}!\n\n".format(username))
            while True:
                print("\n-----------------------------------")
                print("||   1. Account Details          ||")
                print("||   2. Current appointments     ||")
                print("||   3. Logout                   ||")
                print("-----------------------------------")
                choice = input("Enter your choice: ")
                print("\n")
                
                if choice == "1":
                    show_account_details(username)
                elif choice == "2":
                    while True:
                        
                        display_appointments(username)
                        print("\n-----------------------------------")
                        print("||   1. Create new appointment   ||")
                        print("||   2. Cancel appointment       ||")
                        print("||   3. Back                     ||")
                        print("-----------------------------------")
                        choice = input("Enter your choice: ")
                        
                        if choice ==    "1":
                            appointment = create_appointment()
                            barber=input("What babershop do you plan to go to?")
                            users[username]["appointments"].append([appointment,barber])
                            save_users()
                            print("Appointment created:", appointment)
                            
                        elif choice == "2":
                            cancel_appointment(username)
                            
                        elif choice == "3":
                            break
                    
              
                elif choice == "3":
                    break
        
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
