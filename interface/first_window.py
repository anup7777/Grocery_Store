# Importing all necessary modules
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from admin.admin_login_interface import Adminwindow
from User.user_login_interface import Userwindow
from Staff.staff_login_interface import Staffwindow

class Firstwindow:
    # creating Tkinter Window

    def __init__(self):
        self.wn=Tk()
        self.wn.title("Grocery Store System")
        self.wn.geometry("1350x700")
        #self.wn.config(bg="Grey")
        self.wn.resizable(False,False)

       #  Importing all necessary photo
        self.title_photo = PhotoImage(file="C:\\store\\finalbackground.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo,bd=0)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=-70, y=-25)

        #  Moving Pictures
        #  Photo - a
        self.a_photo = PhotoImage(file="C:\\store\\f1.png")
        self.a_photo_lable = Label(self.wn, image=self.a_photo, bg="white",bd=0)
        self.a_photo_lable.image = self.a_photo
        self.a_photo_lable.place(x=1050, y=20)

        # Photo - b
        self.b_photo = PhotoImage(file="C:\\store\\f2.png")
        self.b_photo_lable = Label(self.wn, image=self.b_photo, bg="white",bd=0)
        self.b_photo_lable.image = self.a_photo
        self.b_photo_lable.place(x=1050, y=20)

        #  Photo - c
        self.c_photo = PhotoImage(file="C:\\store\\f3.png")
        self.c_photo_lable = Label(self.wn, image=self.c_photo, bg="white",bd=0)
        self.c_photo_lable.image = self.a_photo
        self.c_photo_lable.place(x=1050, y=20)

        #  Photo - d
        self.d_photo = PhotoImage(file="C:\\store\\f4.png")
        self.d_photo_lable = Label(self.wn, image=self.d_photo, bg="white",bd=0)
        self.d_photo_lable.image = self.a_photo
        self.d_photo_lable.place(x=1050, y=20)

        #  Photo - e
        self.e_photo = PhotoImage(file="C:\\store\\f5.png")
        self.e_photo_lable = Label(self.wn, image=self.e_photo, bg="white",bd=0)
        self.e_photo_lable.image = self.a_photo
        self.e_photo_lable.place(x=1050, y=20)

        # Photo - f
        self.f_photo = PhotoImage(file="C:\\store\\f6.png")
        self.f_photo_lable = Label(self.wn, image=self.f_photo, bg="white",bd=0)
        self.f_photo_lable.image = self.a_photo
        self.f_photo_lable.place(x=1050, y=20)
        self.x=650
        self.slider_func()

        #  HEADINGS

        #  BUTTON - WELCOME
        self.welcome_button = PhotoImage(file="C:\\store\\welcomebtn.png")
        self.welcome_button_button = Button(self.wn, image=self.welcome_button,bg='orange', fg="#3498eb",
                                        activebackground="Grey", cursor="hand2", font=("bold", 13), height=75,
                                        width=246,bd=0,command=self.second_window,)
        self.welcome_button_button.image = self.welcome_button
        self.welcome_button_button.place(x=100, y=618)

        self.wn.mainloop()

    def slider_func(self):
        self.x +=1
        if self.x==1050:
            self.x=650
            #time.sleep(5)

            self.new_im = self.a_photo
            self.a_photo = self.b_photo
            self.b_photo = self.c_photo
            self.c_photo = self.d_photo
            self.d_photo = self.e_photo
            self.e_photo = self.f_photo
            self.f_photo = self.new_im

            self.a_photo_lable.config(image=self.a_photo)
            self.b_photo_lable.config(image=self.b_photo)
            self.c_photo_lable.config(image=self.c_photo)
            self.d_photo_lable.config(image=self.d_photo)
            self.e_photo_lable.config(image=self.e_photo)
            self.f_photo_lable.config(image=self.f_photo)

        # labling photo

        self.a_photo_lable.place(x=self.x, y=20)
        self.a_photo_lable.after(2,self.slider_func)


    def second_window(self):

        # Creating Frames

        self.frame22 = Frame(self.wn, bg="white")
        self.frame22.place(x=485, y=150)
        self.frame3 = Frame(self.wn, bg="white")
        self.frame3.place(x=800, y=480)
        self.frame33 = Frame(self.wn, bg="white")
        self.frame33.place(x=810, y=150)
        self.frame4 = Frame(self.wn, bg="white")
        self.frame4.place(x=1100, y=480)
        self.frame44 = Frame(self.wn, bg="white")
        self.frame44.place(x=1085, y=150)

        #  Importing OTHER necessary photo
        self.one_adminphoto = PhotoImage(file="C:\\store\\one_admin.png")
        self.one_adminphoto_lable = Label(self.wn, image=self.one_adminphoto, bg="white",bd=0)
        self.one_adminphoto_lable.image = self.one_adminphoto
        self.one_adminphoto_lable.place(x=470, y=200)

        self.one_docphoto = PhotoImage(file="C:\\store\\one_customer.png")
        self.one_docphoto_lable = Label(self.wn, image=self.one_docphoto, bg="white",bd=0)
        self.one_docphoto_lable.image = self.one_docphoto
        self.one_docphoto_lable.place(x=770, y=200)

        self.one_staffphoto = PhotoImage(file="C:\\store\\one_staff.png")
        self.one_staffphoto_lable = Label(self.wn, image=self.one_staffphoto, bg="white",bd=0)
        self.one_staffphoto_lable.image = self.one_staffphoto
        self.one_staffphoto_lable.place(x=1070, y=200)

        #  LABEL- ADMIN
        self.lb_login_admin = Label(self.frame22, text="ADMIN", bd=1, fg="black", bg="white",
                                    font=("Comic Sans MS", 18, "bold"), height=1, width=14)
        self.lb_login_admin.grid(row=0, column=0)

        #  BUTTON- ADMIN
        self.butn_login_admin = PhotoImage(file="C:\\store\\admin.png")
        self.butn_login_admin_photo = Button(self.wn, image=self.butn_login_admin,
                                        activeforeground="indigo", cursor="hand2",
                                       font=("Comic Sans MS", 14, "bold"), bg='dark orange', height=50, width=225,
                                       command=self.open_admin_loginpage,  bd=0)
        self.butn_login_admin_photo.image=self.butn_login_admin
        self.butn_login_admin_photo.place(x=480, y=480)

        #  LABEL- Customer
        self.lb_login_customer = Label(self.frame33, text="CUSTOMER", bd=1, fg="black", bg="white",
                                     font=("Comic Sans MS", 18, "bold"), height=1, width=14)
        self.lb_login_customer.grid(row=0, column=0)

        #  BUTTON- customer
        self.butn_login_customerbtn = PhotoImage(file="C:\\store\\customer_login_btn.png")
        self.butn_login_customer = Button(self.wn, image=self.butn_login_customerbtn, bd=0, bg='orange', fg="white",
                                        activebackground="#73C2FB", activeforeground="indigo",
                                        font=("Comic Sans MS", 14, "bold"), height=50, cursor="hand2",
                                        command=self.open_customer_loginpage, width=225, relief=RIDGE, overrelief=RAISED)
        self.butn_login_customer.image = self.butn_login_customerbtn
        self.butn_login_customer.place(x=800, y=480)

        # LABEL- STAFF
        self.lb_login_staff = Label(self.frame44, text="STAFF", bd=1, fg="black", bg="white",
                                    font=("Comic Sans MS", 18, "bold"), height=1, width=14)
        self.lb_login_staff.grid(row=0, column=0)

        # BUTTON- STAFF
        self.butn_login_staffbtn = PhotoImage(file="C:\\store\\staff_login_btn.png")
        self.butn_login_staff = Button(self.wn, image=self.butn_login_staffbtn, bd=0, bg='dark orange', fg="#3498eb",
                                       activebackground="#73C2FB", activeforeground="indigo", cursor="hand2",
                                       font=("Comic Sans MS", 14, "bold"), height=50, width=225,
                                       command=self.open_staff_loginpage, relief=RIDGE, overrelief=RAISED)
        self.butn_login_staff.image = self.butn_login_staffbtn
        self.butn_login_staff.place(x=1110, y=480)
    #  COMMAND TO OPEN ADMIN LOGIN PAGE
    def open_admin_loginpage(self):
        self.wn.destroy()
        Adminwindow()

    #  COMMAND TO OPEN DOCTOR LOGIN PAGE
    def open_customer_loginpage(self):
        self.wn.destroy()
        Userwindow()

    #  COMMAND TO OPEN STAFF LOGIN PAGE
    def open_staff_loginpage(self):
        self.wn.destroy()
        Staffwindow()


Firstwindow()
