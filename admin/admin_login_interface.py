from tkinter import*
from tkinter import messagebox
from admin.connection import MyDatabase
from admin.admin_interface_backend import Adminbackend
from admin.admin_interface import Addservice
from PIL import Image,ImageTk

class Adminwindow:
    def __init__(self):
        self.wn=Tk()
        self.wn.title("Admin Login")
        self.wn.geometry("1370x735+0+0")

        # adding icon image
        self.img = (Image.open("C:\\store\\admin_icon.png"))
        self.icoimg = ImageTk.PhotoImage(self.img)
        self.wn.iconphoto(False, self.icoimg)
        self.wn.resizable(False,False)
        self.my_db=MyDatabase()
        self.admin_backend=Adminbackend()

        # Importing all necessary photo
        self.title_photo = PhotoImage(file="C:\\store\\secondbackground.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=-30, y=0)

        self.title02_photo = PhotoImage(file="C:\\store\\username_logo.png")
        self.title02_photo_lable = Label(self.wn, image=self.title02_photo)
        self.title02_photo_lable.image = self.title02_photo

        self.title03_photo = PhotoImage(file="C:\\store\\password.png")
        self.title03_photo_lable = Label(self.wn, image=self.title03_photo)
        self.title03_photo_lable.image = self.title03_photo

        self.title010_photo = PhotoImage(file="C:\\store\\monitor.png")
        self.title010_photo_lable = Label(self.wn, image=self.title010_photo,bd=0, bg="orange")
        self.title010_photo_lable.image = self.title010_photo
        self.title010_photo_lable.place(x=550, y=155)

        self.title01_photo = PhotoImage(file="C:\\store\\aatry2.png")
        self.title01_photo_lable = Label(self.wn, image=self.title01_photo, bg="white")
        self.title01_photo_lable.image = self.title01_photo
        self.title01_photo_lable.place(x=565, y=175)

        self.title0_photo = PhotoImage(file="C:\\store\\mobile.png")
        self.title0_photo_lable = Label(self.wn, image=self.title0_photo, bg="orange" ,bd=0)
        self.title0_photo_lable.image = self.title0_photo
        self.title0_photo_lable.place(x=20, y=30)

        # Creating Frames
        self.admin_frame=Frame(self.wn,bg="white")
        self.admin_frame.place(x=925, y=260)
        self.admin_frame1 = Frame(self.wn, bg="white")
        self.admin_frame1.place(x=925, y=173)
        self.admin_frame2 = Frame(self.wn, bg="white")
        self.admin_frame2.place(x=1075, y=173)

        #  Major Heading
        self.lb_heading = Label(self.admin_frame1, text="Admin",font=('Impact',37,'bold','underline'),justify="center", fg='red',bg='white')
        self.lb_heading.grid(row=0, column=0,columnspan=1,padx=13,pady=10)

        self.lb_heading2 = Label(self.admin_frame2, text="Login",font=('Impact',37,'bold','underline'),justify="center", fg='blue',bg='white')
        self.lb_heading2.grid(row=0, column=1,columnspan=1,padx=13,pady=10)

        #  LABEL - USERNAME
        self.lb_username = Label(self.admin_frame, text="Username:", bg="white",fg="Blue", font=("cambria", 15, 'bold','underline'),image=self.title02_photo,compound=LEFT)
        self.lb_username.grid(row=5, column=0, padx=10, pady=5)

        #  LABEL - PASSWORD
        self.lb_password = Label(self.admin_frame, text="Password:", bg="white", fg="Blue", font=("cambria", 15, 'bold','underline'),image=self.title03_photo,compound=LEFT)
        self.lb_password.grid(row=10, column=0, padx=10, pady=5)

        # FIRST Entry - USERNAME
        self.ent_username = Entry(self.admin_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.ent_username.grid(row=6, column=0,padx=35, pady=5)

        #  SECOND Entry - PASSWORD
        self.ent_pass = Entry(self.admin_frame, bg="white", fg="black", font=("arial", 15, "bold"), show="")
        self.ent_pass.grid(row=11, column=0, padx=35, pady=5)


        # CHECK BUTTON
        self.ch_btn = Checkbutton(self.admin_frame, text="Remember me", bg="white",cursor="hand2", fg="Black",font=("Arial MT", 10, "bold"))
        self.ch_btn.grid(row=14, columnspan=2, padx=5, pady=5)

        #  LOGIN Button with picture inserted
        self.loginbtn_photo = PhotoImage(file="C:\\store\\loginbtn.png")
        self.loginbtn_photo_button = Button(self.admin_frame, image=self.loginbtn_photo,bg='white', fg="#3498eb", activebackground="#73C2FB",cursor="hand2",command=self.checking_credentials, font=("bold", 13), height=39, width=220,bd=0,relief=RAISED)
        self.loginbtn_photo_button.image = self.loginbtn_photo
        self.loginbtn_photo_button.grid(row=20, columnspan=2, padx=0, pady=6)

        #  FORGET PASSWORD
        self.butn_forget = Button(self.admin_frame, text="Forgot your password?", fg="#000080", bg="white",font=("Arial", 10, "underline"),command=self.forgotpassword,cursor="hand2", relief=FLAT)
        self.butn_forget.grid(row=22, columnspan=3, pady=7)

        # username
        self.ent_username.bind("<FocusIn>", self.on_enter)
        self.ent_username.bind("<FocusOut>", self.on_leave)

        self.ent_username.insert(0, "Username")

        # password
        self.ent_pass.bind("<FocusIn>", self.on_enter1)
        self.ent_pass.bind("<FocusOut>", self.on_leave1)

        self.ent_pass.insert(0, "Password")


        self.show_menu()
        self.wn.mainloop()

    # username
    def on_enter(self, c):
           if self.ent_username.get() == "Username":
             self.ent_username.delete(0, 'end')

    def on_leave(self, c):
        if self.ent_username.get() == "":
                self.ent_username.insert(0, "Username")

    # password
    def on_enter1(self, d):
        if self.ent_pass.get() == "Password":
            self.ent_pass.delete(0, 'end')
            self.ent_pass.config(show="*")

    def on_leave1(self, d):
        if self.ent_pass.get() == "":
            self.ent_pass.config(show="")
            self.ent_pass.insert(0, "Password")

    #  CHECK CREDENTIALS
    def checking_credentials(self):
        username = self.ent_username.get()
        password = self.ent_pass.get()
        if len(username) == 0 or len(password) == 0:
            messagebox.showerror("Missing data entry", "You can't leave any of the sections empty.")
        else:
            if self.admin_backend.check_login(username, password):
                messagebox.showinfo("Login Successful", f"Welcome Mr. {username}")
                self.admin_window()
            else:

                messagebox.showerror("Login Credintials didn't matched",
                                         "The given username and password didn't matched")


    # MENU Button
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

    #  ADMIN DASHBOARD INVOKING
    def admin_window(self):
        self.wn.destroy()
        Addservice()

    #  Forgot Password
    def forgotpassword(self):
        messagebox.showinfo("Service Unavailable", "The system is in its inital phase."
                                                   "\n Service regarding credintials shall"
                                                   "\n be provided very soon.\n"
                                                   "Please consult admin desk for more info.")







