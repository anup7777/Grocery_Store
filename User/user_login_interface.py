from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from admin.connection import MyDatabase
from User.user_interface import Customer_interface
from User.user_registration import Userregistrationwindow

class Userwindow:
    # Generating windows

    def __init__(self):
        self.wn=Tk()
        self.wn.title("Customer Login")

        # adding icon image
        self.img = (Image.open("C:\\store\\user_i.ico"))
        self.icoimg = ImageTk.PhotoImage(self.img)
        self.wn.iconphoto(False, self.icoimg)
        self.wn.geometry("1300x700+0+0")
        self.wn.resizable(False,False)
        self.my_db = MyDatabase()

        #  Necessary Photos
        self.title_photo = PhotoImage(file="C:\\store\\secondbackground.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=0, y=-20)

        self.title04_photo = PhotoImage(file="C:\\store\\monitor.png")
        self.title04_photo_lable = Label(self.wn, image=self.title04_photo,bd=0, bg="orange")
        self.title04_photo_lable.image = self.title04_photo
        self.title04_photo_lable.place(x=550, y=155)

        self.title02_photo = PhotoImage(file="C:\\store\\username_logo.png")
        self.title02_photo_lable = Label(self.wn, image=self.title02_photo)
        self.title02_photo_lable.image = self.title02_photo

        self.title03_photo = PhotoImage(file="C:\\store\\password.png")
        self.title03_photo_lable = Label(self.wn, image=self.title03_photo)
        self.title03_photo_lable.image = self.title03_photo

        self.title01_photo = PhotoImage(file="C:\\store\\customer_login.png")
        self.title01_photo_lable = Label(self.wn, image=self.title01_photo, bg="white", bd=0)
        self.title01_photo_lable.image = self.title01_photo
        self.title01_photo_lable.place(x=565, y=175)

        self.title0_photo = PhotoImage(file="C:\\store\\mobile.png")
        self.title0_photo_lable = Label(self.wn, image=self.title0_photo, bg="orange", bd=0)
        self.title0_photo_lable.image = self.title0_photo
        self.title0_photo_lable.place(x=20, y=10)


        # All Frames
        self.user_frame = Frame(self.wn, bg="white")
        self.user_frame.place(x=915, y=245)

        self.user_frame1 = Frame(self.wn, bg="white")
        self.user_frame1.place(x=915, y=175)

        self.user_frame2 = Frame(self.wn, bg="white")
        self.user_frame2.place(x=1090, y=175)

        # All Lables
        self.lb_heading = Label(self.user_frame1, text="Customer", font=('Impact', 26, 'bold', 'underline'),
                                justify="center", fg='red', bg="white")
        self.lb_heading.grid(row=0, column=0, columnspan=1, padx=20, pady=10)

        self.lb_heading2 = Label(self.user_frame2, text="Login", font=('Impact', 26, 'bold', 'underline'),
                                 justify="center", fg='blue', bg="white")
        self.lb_heading2.grid(row=0, column=1, columnspan=1, padx=20, pady=10)

        self.lb_username = Label(self.user_frame, text="Username:", bg="white", fg="Blue",
                                 font=("cambria", 15, 'bold', 'underline'), image=self.title02_photo, compound=LEFT)
        self.lb_username.grid(row=5, column=0, padx=10, pady=3)

        self.lb_password = Label(self.user_frame, text="Password:", bg="white", fg="Blue",
                                 font=("cambria", 15, 'bold', 'underline'), image=self.title03_photo, compound=LEFT)
        self.lb_password.grid(row=10, column=0, padx=10, pady=3)


        #  All Entries
        self.ent_username = Entry(self.user_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.ent_username.grid(row=6, column=0, padx=40, pady=3)

        self.a=Frame(self.user_frame, width=200, borderwidth=0, bg="black").place(x=540, y=315)

        self.ent_pass = Entry(self.user_frame, bg="white", fg="black", font=("arial", 15, "bold"), show="")
        self.ent_pass.grid(row=11, column=0, padx=40, pady=3)

        self.butn_forget = Button(self.user_frame, text="Forgot your password?", fg="blue", bg="white",
                                  font=("Arial", 10, "underline"), command=self.forgotpassword, cursor="hand2",
                                  relief=FLAT)
        self.butn_forget.grid(row=20, columnspan=2, padx=0, pady=6)

        #  Buttons Required
        self.ch_btn = Checkbutton(self.user_frame, text="Remember me", bg="white", fg="Black",
                                  font=("Arial MT", 10, "bold"), cursor="hand2")
        self.ch_btn.grid(row=14, columnspan=3, pady=3)

        self.loginbtn_photo = PhotoImage(file="C:\\store\\loginbtn.png")
        self.loginbtn_photo_button = Button(self.user_frame, image=self.loginbtn_photo, bg='white', fg="#3498eb",
                                            activebackground="#73C2FB", cursor="hand2",
                                            command=self.checking_credentials, font=("bold", 13), height=39, width=220,
                                            bd=0,relief=RAISED)
        self.loginbtn_photo_button.image = self.loginbtn_photo
        self.loginbtn_photo_button.grid(row=18, columnspan=2, padx=5, pady=2)

        self.create_account_button_photo = PhotoImage(file="C:\\store\\create.png")
        self.create_account_button_photo_button = Button(self.user_frame, image=self.create_account_button_photo,
                                                         bg='white', fg="#3498eb", activebackground="#73C2FB",
                                                         cursor="hand2", font=("bold", 13),
                                                         command=self.open_docregpage, height=39, width=180, bd=0)
        self.create_account_button_photo_button.image = self.create_account_button_photo
        self.create_account_button_photo_button.grid(row=22, columnspan=3, pady=2)

        # Username
        self.ent_username.bind("<FocusIn>", self.on_enter)
        self.ent_username.bind("<FocusOut>", self.on_leave)

        self.ent_username.insert(0, "Username")


        # Password
        self.ent_pass.bind("<FocusIn>", self.on_enter1)
        self.ent_pass.bind("<FocusOut>", self.on_leave1)

        self.ent_pass.insert(0, "Password")

        self.show_menu()
        self.wn.mainloop()


    # Username
    def on_enter(self, c):
        if self.ent_username.get() == "Username":
            self.ent_username.delete(0, 'end')

    def on_leave(self, c):
        if self.ent_username.get() == "":
            self.ent_username.insert(0, "Username")

    # Password
    def on_enter1(self, d):
        if self.ent_pass.get() == "Password":
            self.ent_pass.delete(0, 'end')
            self.ent_pass.config(show="*")

    def on_leave1(self, d):
        if self.ent_pass.get() == "":
            self.ent_pass.config(show="")
            self.ent_pass.insert(0, "Password")

    #  Open customer Registration Page

    def open_docregpage(self):
        self.wn.destroy()
        Userregistrationwindow()

    #  Opening customer Dashboard

    def open_customer_dashboard(self, userlogin, userloginname):
        self.wn.destroy()
        Customer_interface(userlogin, userloginname)

    #  Checking Credentials

    def checking_credentials(self):
        username = self.ent_username.get().lower()
        password = self.ent_pass.get().lower()
        if len(username) == 0 or len(password) == 0:
            messagebox.showerror("Missing data entry", "You can't leave any of the sections empty.")
        else:
            values = self.my_db.fetchingdata_customer()
            username_mylist = []
            for i in values:
                data = (i[0]).lower()
                username_mylist.append(data)
            if username in username_mylist:
                required_index = username_mylist.index(username)
                usrname_logged_in_user = values[required_index][0]
                name_logged_in_user = values[required_index][2]
                if (username == values[required_index][0].lower() and password == values[required_index][1].lower()):
                    if values[required_index][3] == "yes" or values[required_index][3] == "Yes":
                        messagebox.showinfo("Login Successful", f"Welcome Customer {values[required_index][2]}")
                        self.open_customer_dashboard(usrname_logged_in_user, name_logged_in_user)
                    else:
                        messagebox.showerror("User not authenticated",
                                             "Your registration hasn't been\n approved by the admin yet.")
                else:
                    messagebox.showerror("Login Credintials didn't matched",
                                         "The given username and password didn't matched")
            else:
                messagebox.showerror("User Doesn't Exist", "Sorry you aren't registered yet")

    #  MENU Button

    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="<-- Back", menu=log_out)
        log_out.add_cascade(label="<-- Back", command=self.logout)

    #  Logging out

    def logout(self):
        self.wn.destroy()
        from interface.first_window import Firstwindow
        Firstwindow()

    #  Forgot Password

    def forgotpassword(self):
        messagebox.showinfo("Service Unavailable", "The system is in its inital phase."
                                                   "\n Service regarding credintials shall"
                                                   "\n be provided very soon.\n"
                                                   "Please consult admin desk for more info.")

        self.wn.mainloop()

