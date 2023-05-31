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
        
# Load barber data from file
with open("barbers.json", "r") as f:
    barbers = json.load(f)
        
# Function to save barber data to file
def save_barbers():
    with open("barbers.json", "w") as f:
        json.dump(barbers, f)

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
                    "time_created": time.time(),
                    "location" : "",
                    "phone_number" : "",
                    "age" : None,
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
def create_appointment(username):
    choice=input("To go back type 'back' , else type something random to continue with creating an appointment: ")
    if choice=="back".lower():
        return
    appointment = input("Enter the date of the appointment (format: HH:MM,AM/PM,Day): ")
    barber=input("What baber do you plan to go to?: ")
    
    users[username]["appointments"].append([appointment,barber])
    save_users()
    print("Appointment created:", appointment)
    

def display_appointments(username):
    if users[username]["appointments"]:
        print("\nYour current appointments are:\n----------------------------------------------------------")
        for i, appointment in enumerate(users[username]["appointments"]):
            print("{} - {}".format(i+1, appointment))
        print("-----------------------------------------------------------")
    else:
        print("You have no appointments.")


#Function to cancel appointments
def cancel_appointment(username):
    if users[username]["appointments"]:
        
        choice=input("To go back type 'back' , else type something random to continue with canceling appointments ")
        if choice=="back".lower():
                return
       
        try: 
            index = int(input("Enter the index of the appointment to cancel: ")) - 1
            if 0 <= index < len(users[username]["appointments"]):
                del users[username]["appointments"][index]
                save_users()
                print("Appointment canceled.")
        except TypeError as err:
            print(err)
        else:
            print("Invalid index.")
    else:
        print("You have no appointments.")
        
# Function to display account details /username/no. of appointments/ when the account was created
def show_account_details(username):
    user_data = users[username]
    print("|------------------------------------------|")
    print(" Username: {} ".format(username))
    print(" Time created: {}".format(time.ctime(user_data["time_created"])))
    print(" Number of appointments: {}".format(len(user_data["appointments"])))
    print("|------------------------------------------|")
    

# Function to add a review for a barber
def add_review(username):
    choice=input("To go back type 'back' , else type something random to continue with adding a review: ")
    if choice=="back".lower():
        return

    barber_name=input("What is the name of the barber?: ")
    
    for b in barbers:
         barber = barbers[b]
         if b == barber_name:
            
            rating = float(input("Enter your rating (0-5): "))
            review = input("Enter your review: ")
            barber["reviews"].append({
                "client": username,
                "rating": rating,
                "review": review
            })
            barber["rating"] = sum([r["rating"] for r in barber["reviews"]])/len(barber["reviews"])
            with open('barbers.json', 'w') as f:
                json.dump(barbers, f, indent=2)
            print("Review added!")
            return
    else:
        print("Barber not found.")



# Function to add Barbers
def add_barber():
    choice=input("To go back type 'back' , else type something random to continue with the barber registration: ")
    if choice=="back".lower():
        return
    name = input("Enter the name of the new barber: ")
    location= input("Enter the location of the new barer: ")
    services = input("Enter the services of the new barber: ")
    rating = float(input("Enter the rating of the new barber: "))
    reviews = [] # Empty list of reviews for the new barber
    barbers[name] = {
                "location" : location,
                "services": services,
                "rating": rating,
                "reviews": []
            }
    save_barbers()
    print("New barber added successfully.")

# Function to list barbers
def list_barbers():
    print("|-+-+-+-List of barbers-+-+-+-|\n")
    i=1
    for b in barbers:
        barber = barbers[b]
        print("|--+--+--Barber #" + str(i) + "--+--+--|")
        i=i+1
        print("Name: " + b)
        print("Location: {}".format(barber["location"]))
        print("Services: {}".format(barber["services"]))
        print("Rating: {:.1f}".format(barber["rating"]))
        if len(barber["reviews"]) > 0:
            print("Reviews:")
            
            for review in barber["reviews"]:
                print("-- Client: {}".format(review["client"]) + " -- Rating: {}".format(review["rating"]) + " -- Review: '{}'".format(review["review"]) )
                
        else:
            print("No reviews yet.")
        print("|--+--+--+---+---+--+--+--|")
        print()


def barber_schedule():
    #Task : Update the create_appointmnet to check wheter the barber is avaliable
    pass

#print main menu
def print_mainmenu ():
    print("\n------------------------------")
    print("||   1. Register new user   ||")
    print("||   2. Login               ||")
    print("||   3. List of barbers     ||")
    print("||   4. Exit                ||")
    print("------------------------------")    
    
#print user menu 
def print_usermenu():
    print("\n-----------------------------------")
    print("||   1. Account Details          ||")
    print("||   2. Current appointments     ||")
    print("||   3. Add Barber               ||")
    print("||   4. List of Barbers          ||")
    print("||   5. Add Reviews              ||")
    print("||   6. Logout                   ||")
    print("-----------------------------------")

def  print_appointmentmenu():
     print("\n-----------------------------------")
     print("||   1. Create new appointment   ||")
     print("||   2. Cancel appointment       ||")
     print("||   3. Back                     ||")
     print("||   4. Back                     ||")
     print("-----------------------------------")
     
     
# Main program loop
while True:
    
    print_mainmenu()
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        username = login()
        if username:
            print("Welcome, {}!\n\n".format(username))
            while True:
                print_usermenu()
                choice = input("Enter your choice: ")
                print("\n")
                
                if choice == "1":
                    show_account_details(username)
                elif choice == "2":
                    while True:
                        
                        display_appointments(username)
                        print_appointmentmenu()
                        choice = input("Enter your choice: ")
                        
                        if choice ==    "1":
                            create_appointment(username)
                            
                        elif choice == "2":
                            cancel_appointment(username)
                        
                        elif choice == "3":
                            break
                            
                        elif choice == "4":
                            break
                    
              
                elif choice == "3":
                    add_barber()
                elif choice =="4":
                    list_barbers()
                elif choice =="5":
                    add_review(username)
                elif choice =="6":
                    break
        
    elif choice == "3":
        list_barbers()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
