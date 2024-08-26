#project travel agency
from datetime import datetime
from datetime import timedelta
import time
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",password="sql123",database="travel_agency")

login_password="travelpedia"
login_user_id="admin1"
print("_"*100)
print("Welcome To Travelopedia.")
print("This is a travel agency created by Nithya and Harshita")
print("It was created in September 2022")
print("We hope to make this journey of booking smooth")
print("_"*100)
print()

def check():
    global U
    if admin==True:
        u_id=int(input("Enter user id"))
    else:
        u_id=U
    return u_id

#inserting records
def insert_records_package_details():
    cur=mycon.cursor()
    p_no=int(input("Enter package number"))
    desti=input("Enter Destination name")
    length=int(input("Enter duration of travel"))
    h_name=input("enter name of the hotel")
    price=int(input("enter rate of room /night"))
    cur.execute(f'insert into package_details values({p_no},"{desti}",{length},"{h_name}",{price})')
    print("Row inserted")
    mycon.commit()
    
def insert_records_customer_details(u_id):
    while True:
        while True:
            pwd=input("Enter new Password with more than 8 characters")
            if len(pwd)>=8:
                break
            else:
                print("password less than 8 characters")
        p=False
        while True:
            password1=input("Confirm password,else click spacebar to enter new password ")
            if pwd==password1:
                print("account secured with password")
                p=True
                break
            elif password1==" ":
                break
            else:
                pass
        if p==True:
            break
    name=input("Enter your name")
    while True:
        Aadhar_no=int(input("Enter your 12 digit aadhar number"))
        if len(str(Aadhar_no))!=12:
            print("Invalid Aadhar number")
        else:
            break
    while True:
        phone_no=int(input("Enter your 10 digit  phone number"))
        if len(str(phone_no))!=10:
            print("Invalid phone number")
        else:
            break
    cur=mycon.cursor()
    cur.execute(f'insert into customer_details values({u_id},"{pwd}","{name}",{Aadhar_no},{phone_no})')
    print("Account created")
    mycon.commit()

def insert_records_travel_details(u_id):
    cur=mycon.cursor()
    print("Available packages are")
    display_packages()
    p_no=int(input("Enter package number"))
    date_in=input("Enter check in date in YYYY-MM-DD format ")
    date_in_str=datetime.strptime(date_in,"%Y-%m-%d")
    cur.execute(f'select duration,price from package_details where p_no={p_no}')
    r=cur.fetchone()
    d=int(r[0])
    date_out=date_in_str+ timedelta(days=d)
    price=int(r[1])
    qty=int(input("Enter number of people "))
    final_price=qty*d*price
    cur.execute(f'insert into travel_details values({u_id},{p_no},"{date_in}","{date_out}",{qty},{final_price})')
    print("Total tour cost = ",final_price,"proceed to payment.")
    mycon.commit()
#Calculating Final_price 
def update_final_price():
    cur=mycon.cursor()
    cur.execute(f'update travel_details,package_details set final_price=price*duration*no_of_people where package_details.p_no=travel_details.p_no')
    mycon.commit()
#Updation
def update_customer_details(u_id):
    cur=mycon.cursor()
    while True:
        print("_"*100)
        print('''
                                        1.)Password
                                        2.)Name
                                        3.)Aadhar Number
                                        4.)Phone Number
                                        5.)End
                    ''')
        print("_"*100)
        print()
        change=int(input("Enter the field you want to update"))
        print("_"*156)
        if change==1:
            while True:
                while True:
                    password=input("Enter new Password with more than 8 characters")
                    if len(password)>=8:
                        break
                    else:
                        print("password less than 8 characters")
                p=False
                while True:
                    password1=input("Confirm password,else click spacebar to enter new password ")
                    if password==password1:
                        cur.execute(f'update customer_details set password="{password}" where user_id={u_id}')
                        print("password updated")
                        p=True
                        break
                    elif password1==" ":
                        break
                    else:
                        pass
                if p==True:
                    break
        elif change==2:
            name=input("Enter new name")
            cur.execute(f'update customer_details set name="{name}" where user_id={u_id}')
        elif change==3:
            while True:
                Aadhar_no=int(input("Enter your 12 digit aadhar number"))
                if len(str(Aadhar_no))!=12:
                    print("Invalid Aadhar number")
                else:
                    break
            cur.execute(f'update customer_details set Aadhar_no="{Aadhar_no}" where user_id={u_id}')
        elif change==4:
            while True:
                phone_no=int(input("Enter your 10 digit  phone number"))
                if len(str(phone_no))!=10:
                    print("Invalid phone number")
                else:
                    break
            cur.execute(f'update customer_details set Phone_no="{phone_no}" where user_id={u_id}')
        elif change==5:
            print("Quitting")
            break
        else:
            print("Invalid Input,Enter different number.")
    mycon.commit()

#updatation in tables
    
def update_package_details(u_id):
    cur=mycon.cursor()
    while True:
        print("_"*100)
        print('''
                                        1.)Destination
                                        2.)Duration
                                        3.)Hotel
                                        4.)Price
                                        5.)Exit ''')
        print("_"*100)
        change=int(input("Enter the field you want to update:  "))
        if change==1:
            dest=input("Enter new destination")
            cur.execute(f'update package_details set Destination="{dest}" where user_id={u_id}')
        elif change==2:
            dur=int(input("Enter new duration of travel"))
            cur.execute(f'update package_details set duration={dur} where user_id={u_id}');
        elif change==3:
            h_name=input("Enter new hotel name")
            cur.execute(f'update package_details set hotel_name="{h_name}" where user_id={u_id}');
        elif change==4:
            price=int(input("Enter new price"))
            cur.execute(f'update package_details set price={price} where user_id={u_id}');
        elif change==5:
            print("Exit, changes saved")
            break
        else:
            print("Enter valid number")
    mycon.commit()
def update_travel_details(u_id):
    cur=mycon.cursor()
    while True:
        print("_"*100)
        print('''
                                            1.)Check in Date
                                            2.)Number of people
                                            3.)Exit''')
        print("_"*100)
        change=int(input("Enter the field you want to update"))
        if change==1:
            p_no=int(input("Enter package number"))
            date_in=input("Enter check in date in YYYY-MM-DD format ")
            date_in_str=datetime.strptime(date_in,"%Y-%m-%d")
            cur.execute(f'select duration from package_details where p_no={p_no}')
            r=cur.fetchone()
            d=int(r[0])
            date_out=date_in_str+ timedelta(days=d)
            cur.execute(f'update travel_details set date_in="{date_in}" where user_id={u_id} and p_no={p_no}')
            cur.execute(f'update travel_details set date_out="{date_out}" where user_id={u_id} and p_no={p_no}')
        elif change==2:
            p_no=int(input("Enter package number"))
            num=int(input("Enter number of people"))
            cur.execute(f'update travel_details set no_of_people={num} where user_id={u_id} and p_no={p_no}')
        elif change==3:
            print("Exit,changes saved")
            break
        else:
            print("Enter different number")
    mycon.commit()

# Deletion
def delete_package():
    p_no=int(input("Enter package number"))
    cur=mycon.cursor()
    cur.execute(f'select * from package_details where P_no={p_no}')
    d=cur.fecthall()
    r=cur.rowcount
    if r==0:
        print("Enter valid package number")
    else:
        cur.execute(f'delete from package_details where P_no={p_no}')
        print("Row deleted")
    mycon.commit()
    
def delete_travel(u_id):
    cur=mycon.cursor()
    while True:
        p_no=int(input('Enter package number'))
        cur.execute(f'select * from travel_details where P_no={p_no} and user_id={u_id}')
        dataset=cur.fetchall()
        r=cur.rowcount
        c=input("Are you sure you want to cancel your booking y/n")
        if c=="y":
            if r==0:
                print("Enter valid package number and user id")
            else:
                cur.execute(f'delete from travel_details where P_no={p_no} and user_id={u_id}')
                print("booking cancelled")
                break
                

    mycon.commit()
    
def delete_customer(u_id):
    cur=mycon.cursor()
    cur.execute(f'select * from customer_details where user_id={u_id}')
    d=cur.fetchall()
    r=cur.rowcount
    if r==0:
        print("Enter valid user id and package number")
    else:
        cur.execute(f'delete from customer_details where user_id={u_id}')
        print("Account Deleted")
    mycon.commit()

    

#Customer login
def login_customer():
    print("_"*100)
    while True:
        u_id=int(input("enter your user id"))
        while True:
            pwd=input("Enter new Password with more than 8 characters")
            if len(pwd)>=8:
                break
            else:
                print("password less than 8 characters")
        cur=mycon.cursor()
        cur.execute(f'select * from customer_details where user_id={u_id}')
        dataset=cur.fetchall()
        r=cur.rowcount
        if r==0:
                print("Enter valid user_id")
        else:
            if dataset[0][1]==pwd:
                print("Login succesful")
                return u_id
                
                break
            else:
                print("incorrect password")
    print("_"*100)
        

#Admin Login
def login_admin():
    global admin
    print("_"*100)
    while True:
        u_id=input("enter your admin id") 
        pwd=input("Enter your password ")
        if u_id==login_user_id and pwd==login_password:
            print("login successful")
            admin=True
            
            break
        else:
            print("Password /admin id doesnt match")
    print("_"*100)
# Auto generated user id using max(u_id)
def create_account():
    cur=mycon.cursor()
    cur.execute(f'select max(user_id) from customer_details')
    dataset=cur.fetchall()
    num=int(dataset[0][0])
    num+=1
    print("Your user id is",num,"Please save it for further login")
    insert_records_customer_details(num)

#Displaying data using traditional algorithm
def display_booking_user(u_id):
    cur=mycon.cursor()
    cur.execute(f'select * from travel_details where user_id={u_id}')
    d=cur.fetchall()
    r=cur.rowcount
    cur.execute(f'select customer_details.user_id,name,Aadhar_no,Phone_no,Package_details.P_no,date_in,date_out,no_of_people,final_price from customer_details natural join travel_details natural join package_details where customer_details.user_id=travel_details.user_id and package_details.P_no=travel_details.P_no and user_id={u_id}') 
    dataset=cur.fetchall()
    L=["User_id","Name","Aadhar_no","Phone_no","Package_no","Date_in","date_out","no of ppl","final price"]
    S=[8,20,13,11,12,10,10,10,7]
    print("_"*156)
    if r==0:
        print("No bookings")
    else:
        for i in range(len(L)):
            print(L[i],(S[i]-len(L[i]))*" ",end="|")
        print()
        for i in dataset:
            for j in range(len(i)):
                print(i[j],(S[j]-len(str(i[j])))*' ',end="|")

            print()
    print("_"*100)
def display_packages():
    print("Displaying all package details")
    print("_"*156)
    cur=mycon.cursor()
    cur.execute(f'select * from package_details')
    dataset=cur.fetchall()
    L=["Package no","destination","duration","hotel_name","price"]
    S=[11,20,15,25,10]
    for i in range(len(L)):
        print(L[i],(S[i]-len(L[i]))*" ",end="|")
    print()
    for i in dataset:
        for j in range(len(i)):
            print(i[j],(S[j]-len(str(i[j])))*' ',end="|")
        print()
    print("_"*100)
def display_bookings_admin():
    print("_"*100)
    cur=mycon.cursor()
    cur.execute(f'select customer_details.user_id,name,Aadhar_no,Phone_no,Package_details.P_no,date_in,date_out,no_of_people,final_price from customer_details natural join travel_details natural join package_details where customer_details.user_id=travel_details.user_id and package_details.P_no=travel_details.P_no ')
    dataset=cur.fetchall()
    L=["User_id","Name","Aadhar_no","Phone_no","Package_no","Date_in","date_out","no of ppl","final price"]
    S=[8,20,13,11,12,10,10,10,7]
    r=cur.rowcount
    if r!=0:
        for i in range(len(L)):
            print(L[i],(S[i]-len(L[i]))*" ",end="|")
        print()
        for i in dataset:
            for j in range(len(i)):
                print(i[j],(S[j]-len(str(i[j])))*' ',end="|")
            print()
    print("_"*100)
def display_customer_admin():
    print("_"*100)
    cur=mycon.cursor()
    cur.execute(f'select user_id,name,Aadhar_no,phone_no from customer_details')
    dataset=cur.fetchall()
    r=cur.rowcount
    L=["user_id","Name","Aadhar_no","Phone_no"]
    S=[8,20,13,11]
    if r!=0:
        for i in range(len(L)):
            print(L[i],(S[i]-len(L[i]))*" ",end="|")
        print()
        for i in dataset:
            for j in range(len(i)):
                print(i[j],(S[j]-len(str(i[j])))*' ',end="|")
            print()
    print("_"*100)
def display_customer_user():
    print("_"*100)
    u_id=int(input("Enter user id"))
    cur=mycon.cursor()
    cur.execute(f'select user_id,name,Aadhar_no,phone_no from customer_details where user_id={u_id}')
    dataset=cur.fetchall()
    r=cur.rowcount
    L=["user_id","Name","Aadhar_no","Phone_no"]
    S=[8,20,13,11]
    if r==0:
        print("Account doesnt exist")
    else:
            for i in range(len(L)):
                print(L[i],(S[i]-len(L[i]))*" ",end="|")
            print()
            for i in dataset:
                for j in range(len(i)):
                    print(i[j],(S[j]-len(str(i[j])))*' ',end="|")
            print()
    print("_"*100)
# Customer Roles like updating their data, making booking and deleting their account/booking
def cust_role():
    global admin
    admin=False
    
    while True:
        y=input("Do you already have an account?y/n")
        if y=="y" or y=="Y":
            U=login_customer()
            break
        elif y=='N' or y=='n':
            create_account()
            print("Your account is ready.Please login to continue booking for your tour")
            U=login_customer()
            break
        else:
            print("Invalid input")
    while True:
        print("_"*100)
        print('''
                                                        1)View your bookings
                                                        2)Book your next tour
                                                        3)Update customer details
                                                        4)View available packages
                                                        5)Update your tour details
                                                        6)Cancel your booking
                                                        7) Delete account
                                                        8)Logout and exit''')
        print("_"*100)
        
        c=int(input("                               Enter your choice:            "))
        if c==1:
            display_booking_user(U)
        elif c==2:
            insert_records_travel_details(U)
        elif c==3:
            update_customer_details(U)
        elif c==4:
            display_packages()
        elif c==5:
            update_travel_details(U)
        elif c==6:
            delete_travel(U)
        elif c==7:
            delete_customer(U)
        elif c==8:
            print("Thank you!logging out")
            break
        else:
            print("Invalid input")

#Admin roles like looking over all customers data and making changes to their liking
def admin_role():
    login_admin()
    global admin
    admin=True
    while True:
        print("_"*100)
        print('''
                                        1)View all bookings, packages and Customer details
                                        2)Book tour for customer
                                        3)Update, Create or View particular Customer's details
                                        4)Update Customer's Tour details
                                        5)Delete customer account
                                        6)Logout and exit''')
        print("_"*100)
        c=int(input("                               Enter your choice:                                                         "))
        if c==1:
            while True:
                print()
                print("_"*100)
                k=int(input('''Enter the number for the following function:\n1)View all booking\n2)view all packages\n3)view all customers\n4)return to main menu'''))
                if k==1:
                    display_bookings_admin()
                elif k==2:
                    display_packages()
                elif k==3:
                    display_customer_admin()
                    pass
                
                elif k==4:
                    print("Returning to main menu.")
                    break
                else:
                    print("Invalid input.")
        elif c==2:
             while True:
                    u_id=int(input("Enter user id "))
                    cur=mycon.cursor()
                    cur.execute(f'select * from customer_details where user_id={u_id}')
                    dataset=cur.fetchall()
                    r=cur.rowcount
                    if r==0:
                            print("Enter valid user_id")
                    else:
                        break
             insert_records_travel_details(u_id)
        elif c==3:
            while True:
                print()
                print("*"*100)
                print('''
                                    1.)update customer details
                                    2.)create customer account
                                    3.)view customer account
                                    4.)Return to main menu''')
                print("*"*100)
                k=int(input("                       Enter your choice:          "))
                while True:
                        x=int(input("Enter user id "))
                        cur=mycon.cursor()
                        cur.execute(f'select * from customer_details where user_id={x}')
                        dataset=cur.fetchall()
                        r=cur.rowcount
                        if r==0:
                                print("Enter valid user_id")
                        else:
                            break
                if k==2:
                    create_account(x)
                elif k==1:
                    update_customer_details(x)
                elif k==3:
                    display_booking_user(x)
                    pass
                elif k==4:
                    print("Returning to main menu")
                    break
                else:
                    print("Invalid input")
        
        elif c==4:
            while True:
                u_id=int(input("Enter user id "))
                cur=mycon.cursor()
                cur.execute(f'select * from customer_details where user_id={u_id}')
                dataset=cur.fetchall()
                r=cur.rowcount
                if r==0:
                        print("Enter valid user_id")
                else:
                    break
            update_travel_details(u_id)
        elif c==5:
            while True:
                u_id=int(input("Enter user id "))
                cur=mycon.cursor()
                cur.execute(f'select * from customer_details where user_id={u_id}')
                dataset=cur.fetchall()
                r=cur.rowcount
                if r==0:
                        print("Enter valid user_id")
                else:
                    break
            delete_customer(u_id)
        elif c==6:
            print("Thank you!logging out")
            admin=False
            break
        else:
            print("Invalid input")
Login=False
#menu
while True:
    print("_"*100,'''
                                    Select Login/Signup :
                                    1.)Admin
                                    2.)Customer
                                    3.)Exit
''' ,"_"*100
          )

    c=int(input("                                   Enter your choice:"))
    if c==1:
        admin_role()
    elif c==2:
        cust_role()
    elif c==3:
        print("Thank you for visiting travelopedia!")
        break
    else:
        print("Invalid choice input ,enter your choice again.")

