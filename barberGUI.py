import tkinter as tk
from tkinter import messagebox
import hashlib
import json
import time 


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

def check_valid_entry(str):
    if len(str)>=8:
        return True
    else:
        return False
    
def register_user():
    username_info=username.get()
    password_info=password.get()

    status_label=tk.Label(screen1,text="")
    status_label.pack()


    if len(username_info)==0:
         status_label.config(text="Username cannot be null!",fg="red",font=("calibir",11))
         
        
    if len(password_info)==0:
         status_label.config(text="Password cannot be null!",fg="red",font=("calibir",11))
        
    elif not check_valid_entry(password_info):
         status_label.config(text="Invalid entry password must be longer then 8 characters!",fg="red",font=("calibir",11))
            
    
    elif username_info in users:
            status_label.config(text="Username already exists!",fg="red",font=("calibir",11))
    
    else:   
            
            hashed_password = hash_password(str(password_info))
            users[username_info] = {
                "password": hashed_password,
                "appointments": [],
                "time_created": time.time()
            }
            save_users()
            status_label.config(text="User registered successfully!", fg="green", font=("calibri", 11))
            screen1.after(1000,screen1.destroy)
            

    
    password_entry.delete(0,"end")
    status_label.after(1000,status_label.destroy)


    
def register():
    global screen1
    screen1 = tk.Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    
    global username
    global password
    global username_entry
    global password_entry
    
    username = tk.StringVar()
    password = tk.StringVar()
   
    
    tk.Label(screen1,text="Please enter details below").pack()
    tk.Label(screen1,text="Username* ").pack()
    username_entry=tk.Entry(screen1,textvariable=username)
    username_entry.pack()
    tk.Label(screen1,text="Password* ").pack()
    password_entry=tk.Entry(screen1,textvariable = password)
    password_entry.pack()
    tk.Label(screen1,text="").pack()
    tk.Button(screen1,text="Register",width=10,height=1,command=register_user).pack()
    tk.Label(screen1,text="").pack()
    tk.Button(screen1,text="Back",width=10,height=1,command=screen1.destroy).pack()
    

def login_user():
    
    global username_info
    global password_info
    username_info=username_entry2.get()
    password_info=password_entry2.get()
    
    hashed_password = hash_password(password_info)
    if users.get(username_info) and users[username_info]["password"] == hashed_password:   
        login_status_label.config(text="Login successful",fg="green", font=("calibri", 11))
        screen2.after(250,screen2.destroy)
        screen.after(500,screen.destroy)
        user_screen(username_info)

        
    else:
        login_status_label.config(text="Inccorect username or password",fg="red", font=("calibri", 11))
        
def login():
    global screen2
    global username_entry2
    global password_entry2
    global login_status_label
    
    screen2=tk.Toplevel()
    screen2.geometry("250x250")
    screen2.title("Loging in")
    
    username = tk.StringVar()
    password = tk.StringVar()
    
    tk.Label(screen2,text="Please enter details below").pack()
    tk.Label(screen2,text="Username* ").pack()
    username_entry2=tk.Entry(screen2,textvariable=username)
    username_entry2.pack()
    tk.Label(screen2,text="Password* ").pack()
    password_entry2=tk.Entry(screen2,textvariable = password)
    password_entry2.pack()
    password_entry2.config(show="*")
    login_status_label=tk.Label(screen2,text="")
    login_status_label.pack()
    tk.Label(screen2,text="").pack()
    tk.Button(screen2,text="Login",width=10,height=1,command=login_user).pack()
    tk.Label(screen2,text="").pack()
    tk.Button(screen2,text="Back",width=10,height=1,command=(screen2.destroy)).pack()
    
def user_screen(username_info):
    global screen3
    screen3 = tk.Tk()
    screen3.geometry("300x500")
    screen3.title(username_info + "'s User Menu")
    tk.Label(screen3,text=username_info+"'s Options", bg="red",font=("Calibri",13)).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="Account Details",height="2",width="30",command=account_details).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="Current Appointments",height="2",width="30",command=current_appointments).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="Add Barber",height="2",width="30",command=add_barber).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="List of Barbers",height="2",width="30",command=list_barbers).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="Add reviews",height="2",width="30",command=add_review).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="Logout",height="2",width="30",command=logout).pack()
    
    screen3.mainloop()
    

def account_details():
    
    
    screen4=tk.Tk()
    screen4.geometry("300x250")
    screen4.title("Account Details")
    
    listbox_acc_details=tk.Listbox(screen4)
    listbox_acc_details.configure(width=50)
    listbox_acc_details.pack()
    
    tk.Label(screen4,text="").pack()
    tk.Label(screen4,text="").pack(side=tk.LEFT)
    tk.Button(screen4,text="Back",width=15,height=3,command=(screen4.destroy)).pack(side=tk.LEFT)
    tk.Label(screen4,text="").pack(side=tk.RIGHT)
    tk.Button(screen4,text="Add additional info",width=15,height=3,command=add_info).pack(side=tk.RIGHT)

    
    user_data = users[username_info]
   
    listbox_acc_details.insert(0," Username: {} ".format(username_info))
    listbox_acc_details.insert(1," Time created: {} ".format(time.ctime(user_data["time_created"])))
    listbox_acc_details.insert(2," Nubmer of appointments: {} ".format(len(user_data["appointments"])))
  

    
def add_info():
    pass
    
def current_appointments():

    screen5=tk.Tk()
    screen5.geometry("600x400")
    screen5.title("Current Appointments")
    
    
    
    listbox_curr_appointments=tk.Listbox(screen5)
    listbox_curr_appointments.configure(width=75)
    listbox_curr_appointments.place()
    tk.Label(screen5,text="").pack()
    listbox_curr_appointments.pack()
    tk.Label(screen5,text="").pack()
    

    global appointment_status
    global cancel_appointment_entry
    j=0
    if users[username_info]["appointments"]:
       
        for i, appointment in enumerate(users[username_info]["appointments"]):
            listbox_curr_appointments.insert(j,"{} - {}".format(i, appointment))
            j=j+1
    else:
        pass

    review = tk.StringVar()
    cancel_index = tk.StringVar()
    

    
    
    appointment_status=tk.Label(screen5,text="")
    appointment_status.place(x=100,y=250)
    if not users[username_info]["appointments"]:
        appointment_status.config(text="You have no appointments.", fg="red", font=("calibir", 11))
    tk.Button(screen5,text="Back",width=10,height=2,command=(screen5.destroy)).place(x=10,y=350)
    index_label= tk.Label(screen5,text="Enter the index of the appointment to cancel: ")
    index_label.place(x=10,y=210)
    cancel_appointment_entry=tk.Entry(screen5,textvariable=cancel_index)
    cancel_appointment_entry.place(x=300,y=210)
    cancel_appointment_button=tk.Button(screen5,text="Cancel \nAppointment",width=10,height=2,command=cancel_appointment)
    cancel_appointment_button.place(x=450,y=200)
    add_appointment_button=tk.Button(screen5,text="Add \nAppointment",width=10,height=2,command=add_appointment)
    add_appointment_button.place(x=10,y=300)
    tk.Label(screen5,text="<--- Want to add/create appointments? \nClick on this button!").place(x=110,y=310)

  




def add_appointment():
    pass
def cancel_appointment():

   

    try:
        index = int(cancel_appointment_entry.get())
        if 0 <= index < len(users[username_info]["appointments"]):
            del users[username_info]["appointments"][index]
            save_users()
            appointment_status.config(text="Appointment canceled", fg="green", font=("calibir", 11))
        else:
            raise ValueError("Invalid index")
    except TypeError as e:
        err = str(e)
        appointment_status.config(text="Error: " + err, fg="red", font=("calibir", 11))
    except ValueError as e:
        err = str(e)
        appointment_status.config(text="Invalid index: " + err, fg="red", font=("calibir", 11))



    
   
    
def add_barber():
    screen6=tk.Tk()
    screen6.geometry("300x350")
    screen6.title("Add a barber")
    
    
def list_barbers():
    pass
def add_review():
    pass
def openclose():
    pass
def logout():
    screen3.after(1,screen3.destroy)
    main_screen()
    

    
    
    
def main_screen():
    global screen
    screen = tk.Tk()
    screen.geometry("300x250")
    screen.title("barbershop")
    tk.Label(text="Dobrodojdovte u Mishko Berber", bg="pink",font=("Times",13,"bold italic")).pack()
    tk.Label(text="").pack()
    tk.Button(text="Login",height="2",width="30",command=login).pack()
    tk.Label(text="").pack()
    tk.Button(text="Register",height="2",width="30",command=register).pack()
    
    screen.mainloop()
    
main_screen()