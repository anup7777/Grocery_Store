from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from admin.connection import MyDatabase

class Userregistrationwindow:
    # creating Tkinter Window

    def __init__(self):
        self.wn=Tk()
        self.wn.title("User Registration")
        self.wn.geometry("1370x735+0+0")
        self.wn.resizable(False,False)
        self.show_menu()

        # Importing all necessary photo
        self.background = PhotoImage(file="C:\\store\\secondbackground.png")
        self.background_lable = Label(self.wn, image=self.background,bg="white")
        self.background_lable.image = self.background
        self.background_lable.place(x=0, y=0)

        self.title0_photo = PhotoImage(file="C:\\store\\mobile.png")
        self.title0_photo_lable = Label(self.wn, image=self.title0_photo, bd=0)
        self.title0_photo_lable.image = self.title0_photo
        self.title0_photo_lable.place(x=50, y=10)

        self.title0_photo = PhotoImage(file="C:\\store\\register.png")
        self.title0_photo_lable = Label(self.wn, image=self.title0_photo, bd=0)
        self.title0_photo_lable.image = self.title0_photo
        self.title0_photo_lable.place(x=700, y=10)

        # All Frames
        self.user_frame=Frame(self.wn,bg="white")
        self.user_frame.place(x=730, y=140)

        self.user_frame1 = Frame(self.wn)
        self.user_frame1.place(x=780, y=20)

        self.user_frame2 = Frame(self.wn)
        self.user_frame2.place(x=920, y=20)


        # Major Heading
        self.lb_heading = Label(self.user_frame1, text="Customer", font=('Impact', 20, 'bold', "underline"),
                                justify="left", fg='red')
        self.lb_heading.grid(row=0, column=0, padx=10, pady=1)

        self.lb_heading2 = Label(self.user_frame2, text="Registration", font=('Impact', 20, 'bold', "underline"),
                                 justify="left", fg='blue')
        self.lb_heading2.grid(row=0, column=1, padx=25, pady=1)

        #  Picture With Label
        self.title01_photo = PhotoImage(file="C:\\store\\customer_registration_page.png")
        self.title01_photo_lable = Label(self.user_frame, image=self.title01_photo, bg="white")
        self.title01_photo_lable.image = self.title01_photo


        # All Labels
        self.lb_customername = Label(self.user_frame, bg="white", fg="Black",font=("cambria", 15, 'bold',"underline"), image=self.title01_photo, compound=TOP,justify="center")
        self.lb_customername.grid(row=1, column=0,columnspan=2, padx=7, pady=8)

        self.lb_buyername = Label(self.user_frame, text="Customer's Name:", bg="white", fg="Blue",font=("cambria", 15, 'bold'),justify="center")
        self.lb_buyername.grid(row=3, column=0, padx=7, pady=3)

        self.lb_username = Label(self.user_frame, text="Username:", bg="white",fg="Blue", font=("cambria", 15, 'bold'),justify="center")
        self.lb_username.grid(row=5, column=0, padx=7, pady=3)

        self.lb_password = Label(self.user_frame, text="Password:", bg="white", fg="Blue", font=("cambria", 15, 'bold'),justify="center")
        self.lb_password.grid(row=7, column=0, padx=7, pady=3)

        self.lb_customerage = Label(self.user_frame, text="Customer Age:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_customerage.grid(row=15, column=0, padx=7, pady=3)

        self.lb_customergender = Label(self.user_frame, text="Customer Gender:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_customergender.grid(row=20, column=0, padx=7, pady=3)

        self.lb_customeraddress = Label(self.user_frame, text="Customer Address:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_customeraddress.grid(row=25, column=0, padx=7, pady=3)

        self.lb_customeremail = Label(self.user_frame, text="Customer Email:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_customeremail.grid(row=30, column=0, padx=7, pady=3)


        #  All Entries
        self.ent_buyername=Entry(self.user_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_buyername.grid(row=3,column=1,padx=1,pady=3)

        self.ent_username = Entry(self.user_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_username.grid(row=5, column=1,padx=10, pady=3)

        self.ent_pass = Entry(self.user_frame, bg="white", fg="black", font=("arial", 15, "bold"), show="*",justify="center")
        self.ent_pass.grid(row=7, column=1, padx=10, pady=3)

        self.ent_customerage=Entry(self.user_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_customerage.grid(row=15, column=1, padx=10, pady=3)

        self.ent_customergender=Entry(self.user_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_customergender.grid(row=20, column=1, padx=10, pady=3)

        self.ent_customeraddress=Entry(self.user_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_customeraddress.grid(row=25, column=1, padx=10, pady=3)

        self.ent_email = Entry(self.user_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_email.grid(row=30, column=1, padx=10, pady=3)

        # All Buttons
        self.create_account_button_photo = PhotoImage(file="C:\\store\\signup.png")
        self.create_account_button_photo_button = Button(self.user_frame, image=self.create_account_button_photo,
                                                         bg='white', fg="#3498eb", activebackground="#73C2FB",
                                                         cursor="hand2", font=("bold", 13),
                                                         command=self.registering_doc, height=39, width=150,bd=0)
        self.create_account_button_photo_button.image = self.create_account_button_photo
        self.create_account_button_photo_button.grid(row=50, columnspan=2, padx=7, pady=20)

        self.my_database = MyDatabase()
        self.wn.mainloop()

    #  Registering the Customer
    def registering_doc(self):
        name = self.ent_buyername.get()
        username = self.ent_username.get()
        password = self.ent_pass.get()
        age = self.ent_customerage.get()
        gender = self.ent_customergender.get()
        address = self.ent_customeraddress.get()
        email = self.ent_email.get()

        if len(name) != 0 and len(username) != 0 and len(password) != 0 and len(age) != 0 and len(gender) != 0 and len(
                address) != 0 and len(
            email) != 0:
            if age.isdigit():
                qry = "INSERT INTO customer_credentials (Customer_Name,username,password,Customer_Age,Customer_Gender,Customer_Address,Customer_Email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                values = (name, username, password, age, gender, address, email)
                print("Data added")
                self.my_database.add_update_delete(qry, values)
                messagebox.showinfo("Regestration Successfull", "Please wait until \n admin approval for login")
            else:
                messagebox.showerror("Numeric Data Needed.", "Age can't be a string value")
        else:
            messagebox.showerror("Blank Space Detected", "You can't leave any entry boxes empty.")

    #  MENU Button
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="<-- Back", menu=log_out)
        log_out.add_cascade(label="<-- Back", command=self.logout)

    # Logging out
    def logout(self):
        self.wn.destroy()
        from User.user_login_interface import Userwindow
        Userwindow()
