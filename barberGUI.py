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
    try: 
        username_info=username.get()
        password_info=password.get()
        confirm_password_info=confirm_password_entry.get()

        status_label=tk.Label(screen1,text="")
        status_label.pack()
        space = " "
        
        
        if len(username_info)==0:
            status_label.config(text="Username cannot be null!",fg="red",font=("calibir",11))
            
        elif space in username_info:
            status_label.config(text="Username cant have empty spaces!",fg="red",font=("calibir",11))
            
        elif username_info in users:
                status_label.config(text="Username already exists!",fg="red",font=("calibir",11))
                
        elif len(password_info)==0:
            status_label.config(text="Password cannot be null!",fg="red",font=("calibir",11))
            
        elif space in password_info:
            status_label.config(text="Password cant have empty spaces!",fg="red",font=("calibir",11))
            
            
        elif not check_valid_entry(password_info):
            status_label.config(text="Invalid entry password must be longer then 8 characters!",fg="red",font=("calibir",11))
        elif not confirm_password_info == password:
            status_label.config(text="The passwords don't match!",fg = "red",font=("calibir",11))
                
        
        
        else:   
                
                hashed_password = hash_password(str(password_info))
                users[username_info] = {
                    "password": hashed_password,
                    "appointments": [],
                    "time_created": time.time(),
                    "location" : "",
                    "phone_number" : "",
                    "age" : None,
                    
                    
                }
                save_users()
                status_label.config(text="User registered successfully!", fg="green", font=("calibri", 11))
                screen1.after(1000,screen1.destroy)
            
    except:
        status_label.config(text="Error",fg = "red",font=("calibir",11))
    
            

    
    password_entry.delete(0,"end")
    confirm_password_entry.delete(0,"end")
    status_label.after(1000,status_label.destroy)


    
def register():
    global screen1
    screen1 = tk.Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x300")
    
    
    global username
    global password
    global username_entry
    global password_entry
    global confirm_password_entry
    
    username = tk.StringVar()
    password = tk.StringVar()
    cpassword = tk.StringVar()
    
    tk.Label(screen1,text="Please enter details below").pack()
    tk.Label(screen1,text="Username* ").pack()
    username_entry=tk.Entry(screen1,textvariable=username)
    username_entry.pack()
    tk.Label(screen1,text="Password* ").pack()
    password_entry=tk.Entry(screen1,textvariable = password,show="*")
    password_entry.pack()
    tk.Label(screen1,text="Confirm password* ").pack()
    confirm_password_entry=tk.Entry(screen1,textvariable = cpassword,show="*")
    confirm_password_entry.pack()
    tk.Label(screen1,text="").pack()
    tk.Button(screen1,text="Register",width=10,height=1,command=register_user).pack()
    tk.Label(screen1,text="").pack()
    tk.Button(screen1,text="Back",width=10,height=1,command=screen1.destroy).pack()
    

def login_user():
    
    global username_info
    global password_info
    
    try: 
        username_info=username_entry2.get()
        password_info=password_entry2.get()
        space=" "
        

        hashed_password = hash_password(password_info)
        if len(username_info)==0:
            login_status_label.config(text="Please enter your username and password",fg="red", font=("calibri", 10))
        elif space in username_info:
            login_status_label.config(text="Please enter a valid entry\nUsername should not have empty spaces!",fg="red", font=("calibri", 10))
        elif space in password_info:
            login_status_label.config(text="Please enter a valid entry\nUsername should not have empty spaces!",fg="red", font=("calibri", 10))
        
            
        elif users.get(username_info) and users[username_info]["password"] == hashed_password:   
            login_status_label.config(text="Login successful",fg="green", font=("calibri", 11))
            screen2.after(250,screen2.destroy)
            screen.after(500,screen.destroy)
            user_screen(username_info)

            
        else:
            login_status_label.config(text="Inccorect username or password",fg="red", font=("calibri", 11))
    except (TypeError,ValueError) as e:
        login_status_label.config(text="Error: " + e ,fg="red", font=("calibri", 11))
    
        
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
    global user_screen_status_label
    screen3 = tk.Tk()
    screen3.geometry("300x500")
    screen3.title(username_info + "'s User Menu")
    tk.Label(screen3,text=username_info+"'s Options", bg="red",font=("Calibri",13)).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="Account Details",height="2",width="30",command=account_details).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="Current Appointments",height="2",width="30",command=current_appointments).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="Add Barber",height="2",width="30",command=add_barber_screen).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="List of Barbers",height="2",width="30",command=list_barbers).pack()
    tk.Label(screen3,text="").pack()
    tk.Button(screen3,text="Logout",height="2",width="30",command=logout).pack()
    user_screen_status_label=tk.Label(screen3,text="")
    user_screen_status_label.pack()
    
    screen3.mainloop()
    

def account_details():
    global screen4
    screen4=tk.Toplevel(screen3)
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
    listbox_acc_details.insert(1," Age: {} ".format(user_data["age"]))
    listbox_acc_details.insert(2," Location: {} ".format(user_data["location"]))
    listbox_acc_details.insert(3," Phone Number: {} ".format(user_data["phone_number"]))
    listbox_acc_details.insert(4," Time created: {} ".format(time.ctime(user_data["time_created"])))
    listbox_acc_details.insert(5," Nubmer of appointments: {} ".format(len(user_data["appointments"])))
    
    
  
def add_infouser():
    
    try:
    
        location_info=location_entry.get()
        age_info=int(age_entry.get())
        phone_info=phone_number_entry.get() 
        
        if age_info>100 or age_info<10:
            addinfo_status_label.config(text="Age must be between 10-100",fg="Red",font=("calibir",10))
    
           
        elif not len(phone_info)==9:
            addinfo_status_label.config(text="Phone number must be 9 digits as the format says\nOnly numbers!",fg="red",font=("calibir",10))
            
        else:   
            char='-'
            phone_info=char.join(phone_info[i:i+3] for i in range(0, len(phone_info), 3))
            users[username_info]["location"]=location_info
            users[username_info]["phone_number"]=phone_info
            users[username_info]["age"]=age_info
                    
                
            save_users()
            addinfo_status_label.config(text="Additional information registered sucessfully!", fg="green", font=("calibri", 10))
            screen4.destroy()
            account_details()
            screen7.after(1000,screen7.destroy)
                

        
      
    except (ValueError,TypeError) as e:
        addinfo_status_label.config(text="Error " + str(e),fg="Red",font=("calibir",10))

        

    
def add_info():
    global screen7
    screen7=tk.Toplevel(screen4)
    screen7.geometry("300x250")
    screen7.title("Additional info")
    
    location=""
    age=int
    phone=""
    
    global location_entry
    global age_entry
    global phone_number_entry
    global addinfo_status_label
    
    tk.Label(screen7,text="Enter location: ").place(x=20,y=20)
    location_entry=tk.Entry(screen7,textvariable=location)
    location_entry.place(x=160,y=20)
    tk.Label(screen7,text="Enter age: ").place(x=20,y=50)
    age_entry=tk.Entry(screen7,textvariable=age)
    age_entry.place(x=160,y=50)
    tk.Label(screen7,text="Enter phone number \n(format - ex 071845218)").place(x=20,y=80)
    phone_number_entry=tk.Entry(screen7,textvariable=phone)
    phone_number_entry.place(x=160,y=80)
    addinfo_status_label=tk.Label(screen7,text="")
    addinfo_status_label.place(x=10,y=150)
    addinfo_button=tk.Button(screen7,text="Add info",width=15,height=3,command=add_infouser).place(x=150,y=180)
    
    tk.Button(screen7,text="Back",width=15,height=3,command=(screen7.destroy)).place(x=10,y=180)
    
    
    
def current_appointments():

    global screen5

    
    screen5=tk.Toplevel(screen3)
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

    review = ""
    cancel_index = int
    

    
    
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
    tk.Label(screen5,text="<--- Want to add/create appointments? \nClick on this button!",font=("calibir", 11)).place(x=110,y=310)

  


def add_appointment_user():
 
   
    try:
       
            
        barber=barbershop_entry.get()
        if len(username_info)==0:
            add_appointment_status.config(text="Barber cannot be null!",fg="red",font=("calibir",11))
            
        if barber in barbers:
            appointment=appointment_entry.get()
            if len(appointment)==0:
                add_appointment_status.config(text="Date cannot be null!",fg="red",font=("calibir",11))
            else:
                users[username_info]["appointments"].append([appointment,barber])
                save_users()
                screen5.destroy()
                current_appointments()
                appointment_status.config(text="Appointment added!", fg="green", font=("calibir", 11))
            
        else:
             add_appointment_status.config(text="Barber ' " + barber +" '  does not exist!", fg="red", font=("calibir", 11))
    except (Exception,TypeError,ValueError) as e:
        add_appointment_status.config(text="Error:" + str(e),fg="red",font=("calibir",11))
        
        
       
        

def add_appointment():
    global screen8
    screen8=tk.Toplevel(screen5)
    screen8.geometry("350x200")
    screen8.title("Creating appointment")
    
    global barbershop_entry
    global appointment_entry
    global add_appointment_status
    
    barbershop_info=""
    appointment_info=""

    tk.Label(screen8,text="Enter the barbershop you plan to visit: ").place(x=0,y=50,)
    tk.Label(screen8,text="Enter the date of the appointment: \n(format: HH:MM,AM/PM,Day) ").place(x=0,y=100)
    barbershop_entry=tk.Entry(screen8,textvariable=barbershop_info)
    barbershop_entry.place(x=220,y=50)
    appointment_entry=tk.Entry(screen8,textvariable=appointment_info)
    appointment_entry.place(x=220,y=100)
    tk.Button(screen8,text="Add Appointment", width=15,height=2,command=add_appointment_user).place(x=100,y=150)
    add_appointment_status=tk.Label(screen8,text="")
    add_appointment_status.place(x=120,y=20)
    tk.Button(screen8,text="Back",width=10,height=2,command=screen8.destroy).place(x=10,y=150)
    
    
    
def cancel_appointment():

   

    try:
        index = int(cancel_appointment_entry.get())
        if 0 <= index < len(users[username_info]["appointments"]):
            del users[username_info]["appointments"][index]
            save_users()
            screen5.destroy()
            current_appointments()
            appointment_status.config(text="Appointment canceled", fg="green", font=("calibir", 11))
        else:
            raise ValueError("Invalid index")
    except TypeError as e:
        err = str(e)
        appointment_status.config(text="Error: " + err, fg="red", font=("calibir", 11))
    except (TypeError,ValueError) as e:
        appointment_status.config(text="Invalid index: " + str(e), fg="red", font=("calibir", 11))



    
def add_barber():
    try:
    
        name = barbername_entry.get()
        location= barber_location_entry.get()
        services = barber_services_entry.get()
        rating = float
        reviews = [] 
        if name in barbers:
            addbarber_status_label.config(text="Barber already exists",fg="red",font=("calibir",11))
        elif len(name)==0:
            addbarber_status_label.config(text="Please enter a name",fg="red",font=("calibir",11))
        elif len(location)==0:
            addbarber_status_label.config(text="Please enter a location",fg="red",font=("calibir",11))
        elif len(services)==0:
            addbarber_status_label.config(text="Please enter the services",fg="red",font=("calibir",11))
        else:
            
            barbers[name] = {
                        "location" : location,
                        "services": services,
                        "rating": rating,
                        "reviews": []
                    }
            user_screen_status_label.config(text="Barber added succesfully!",fg="green",font=("calibir",11) )
            save_barbers()
            screen6.destroy()
            
    except (Exception,TypeError)as e:
        addbarber_status_label.config(text="Error " + str(e),fg="red",font=("calibir",11))
    
    
def add_barber_screen():
    global screen6
    screen6=tk.Toplevel(screen3)
    screen6.geometry("300x350")
    screen6.title("Add a barber")
    barbname=""
    location=""
    services=""
    
    
    global addbarber_status_label
    global barber_location_entry
    global barbername_entry
    global barber_services_entry
    
    tk.Label(screen6,text="Enter Barber name: ").place(x=20,y=20)
    barbername_entry=tk.Entry(screen6,textvariable=barbname)
    barbername_entry.place(x=160,y=20)
    tk.Label(screen6,text="Enter Location: ").place(x=20,y=50)
    barber_location_entry=tk.Entry(screen6,textvariable=location)
    barber_location_entry.place(x=160,y=50)
    tk.Label(screen6,text="Enter services ").place(x=20,y=80)
    barber_services_entry=tk.Entry(screen6,textvariable=services)
    barber_services_entry.place(x=160,y=80)
    addbarber_status_label=tk.Label(screen6,text="")
    addbarber_status_label.place(x=10,y=150)
    addbarber_button=tk.Button(screen6,text="Add",width=15,height=3,command=add_barber).place(x=150,y=180)
    
    tk.Button(screen6,text="Back",width=15,height=3,command=(screen6.destroy)).place(x=10,y=180)
    
    
def list_barbers():
    global screen9
    screen9=tk.Toplevel(screen3)
    screen9.geometry("500x400")
    screen9.title("List of barbers")
    
    
    barbername=""
    global barber_name_entry
    global barber_review_status
    
    listbox_barbers=tk.Listbox(screen9)
    listbox_barbers.configure(width=75)
    listbox_barbers.pack()
    tk.Label(screen9,text="To see barbers review, Enter the barbers name and click the 'View'button\nIf you want to add a review enter barbers name and click 'Add review' button").pack()
    barber_name_entry=tk.Entry(screen9,textvariable=barbername)
    barber_name_entry.pack()
    tk.Button(screen9,text="View",width=15,height=3,command=view_barber_review).place(x=190,y=230)
    barber_review_status=tk.Label(screen9,text="")
    barber_review_status.place(x=160,y=300)
    tk.Button(screen9,text="Back",width=15,height=3,command=(screen9.destroy)).place(x=50,y=230)
    tk.Button(screen9,text="Add review",width=15,height=3,command=add_review_screen).place(x=330,y=230)
   
    
    
    
    i=1
    for b in barbers:
        barber = barbers[b]
       
        info_str = "Name: {} || Location: {} || Services: {} || Rating: {:.1f} ".format(b, barber["location"], barber["services"], barber["rating"])
        listbox_barbers.insert(i,info_str)
        i=i+1
          
          
def view_barber_review():
     
    
     try:
        barbname=barber_name_entry.get()
        if len(barbname)==0:
            barber_review_status.config(text="Please enter a name into the box",fg="red",font=("calibir",11))
        elif barbname in barbers:
            if barbers[barbname]["reviews"]:
                screen10=tk.Tk()
                screen10.geometry("750x300")
                screen10.title("Barbers reviews")
                
                tk.Label(screen10,text="Barber "+ barbname+"'s reviews").pack()
                listbox_barber_reviews=tk.Listbox(screen10)
                listbox_barber_reviews.configure(width=150)
                listbox_barber_reviews.pack()
                tk.Button(screen10,text="Back",width=10,height=2,command=(screen10.destroy)).pack()
                i=0
                for review in barbers[barbname]["reviews"]:
                    listbox_barber_reviews.insert(i,"-- Client: {}".format(review["client"]) + " -- Rating: {}".format(review["rating"]) + " -- Review: '{}'".format(review["review"]) )
                    i=i+1
            
            else:
                barber_review_status.config(text="Barber ' " + barbname + " ' has no reviews!",fg="red",font=("calibir",11))
                
            
        else:
            barber_review_status.config(text="Barber ' " + barbname + " ' does not exist",fg="red",font=("calibir",11))
            
            
     except TypeError as e:
         barber_review_status.config(text="Error: " + e,fg="red",font=("calibir",11))
         
         
     
     
              
def add_review():
    rating=rating_entry.get()
    
    try:
        barbname_info=barber_name_entry.get()
        review= review_text.get("1.0", tk.END).replace('\n', ' ')
        rating=float(rating_entry.get())

        if len(review)==0:
            add_review_label.config(text="Text should not be empty!",fg="red",font=("calibir",11))
        elif len(review)>100 or len(review)<10:
            add_review_label.config(text="The review must be between 10 and 100 characters",fg="red",font=("calibir",11))
        elif not isinstance(rating, float):
            add_review_label.config(text="Rating must be a float/integer",fg="red",font=("calibir",11))
        elif rating >5.0 or rating <1.0:
            add_review_label.config(text="Rating should be between 1.0 and 5.0",fg="red",font=("calibir",11))
        else:
            for b in barbers:
                barber = barbers[b]
                if b == barbname_info:

                    barber["reviews"].append({
                        "client": username_info,
                        "rating": rating,
                        "review": review
                    })
                    barber["rating"] = sum([r["rating"] for r in barber["reviews"]])/len(barber["reviews"])
                    save_barbers()
                    add_review_label.config(text="Review added!",fg="green",font=("calibir",11))
    except (Exception,TypeError,ValueError) as e:
        add_review_label.config(text = "Error: " + str(e),fg="red",font=("calibir",11))

        
    
def add_review_screen():
    
    try:
        global review_text
        global add_review_label
        global rating_entry
        barbname=barber_name_entry.get()
        if len(barbname)==0:
            barber_review_status.config(text="Please enter a name into the box",fg="red",font=("calibir",11))
           
        elif barbname in barbers:
            screen11=tk.Toplevel(screen9)
            screen11.geometry("300x300")
            screen11.title("Adding review to " + barbname) 
            rate=float 
                
            review_text = tk.Text(screen11, height=10, width=50)
            review_text.pack()
            add_review_label=tk.Label(screen11,text="")
            add_review_label.pack()
            tk.Label(screen11,text="Rating :").pack()
            rating_entry=tk.Entry(screen11,textvariable=rate)
            rating_entry.pack()
            
            tk.Button(screen11,text="Add",command=add_review).pack()
            tk.Button(screen11,text="Back",width=10,height=2,command=(screen11.destroy)).pack()
        
            
        else:
            barber_review_status.config(text="Barber ' " + barbname + " ' does not exist",fg="red",font=("calibir",11))
            
    except:
        barber_review_status.config(text = "Error: " ,fg="red",font=("calibir",11))

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
