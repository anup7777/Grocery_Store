from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from PIL import Image, ImageTk
import time as tm
import datetime
from admin.admin_interface_backend import Adminbackend

class Addservice:
    def __init__(self):
        self.wn = Tk()
        self.wn.title("Admin Panel")
        self.wn.geometry("1350x700+0+0")
        self.wn.configure(bg="white")
        self.wn.resizable(False, False)

        # MAKING UPDATE INDEX GLOBAL
        self.admin_backend=Adminbackend()
        self.update_index0 = ""
        self.update_index00 = ""
        self.update_index = ""

        # Importing all necessary photo

        self.title_photo = PhotoImage(file="C:\\store\\admin_top.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo, bg="white",bd=0)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=0, y=0)

        self.title_photo01 = PhotoImage(file="C:\\store\\one_admin_service.png")
        self.title_photo01_lable = Label(self.wn, image=self.title_photo01,bd=0)
        self.title_photo01_lable.image = self.title_photo01
        self.title_photo01_lable.place(x=310, y=0)

        #  Creating Frames
        #  Main Frame
        self.frame1 = Frame(self.wn, bg="white")
        self.frame1.place(x=0, y=260)

        # Tree Frame
        self.tree_frame = Frame(self.wn, bg="white")
        self.tree_frame.place(x=312, y=0)

        #  Navigation Frame
        self.navigation_frame = Frame(self.wn, bg="white")
        self.navigation_frame.place(x=312, y=247)

        #  NAvigation0 Frame
        self.navigation_frame0 = LabelFrame(self.wn, bg="white", bd=2)
        self.navigation_frame0.place(x=1125, y=0)

        # Major Heading
        self.lb_heading_inital = Label(self.frame1, text="Admin", bg="white", font=('Impact', 35, 'bold', 'underline'),fg='red')
        self.lb_heading_inital.grid(row=20, column=40, padx=16, pady=10)
        self.lb_heading_end = Label(self.frame1, text="Panel", bg="white", font=('Impact', 35, 'bold', 'underline'),fg='blue')
        self.lb_heading_end.grid(row=20, column=80, padx=13, pady=10)

        # Creating Frame-2
        self.frame2 = Frame(self.wn, bg="white")
        self.frame2.place(x=1, y=350)


        #  Creating Seprator and Buttons

        # First Seprator
        self.first_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.first_seperator.configure(bg="black")
        self.first_seperator.grid(row=0, column=0)

        # First Button
        self.service_button = Button(self.frame2, text="Services", bg='white', fg="black", activebackground="#73C2FB",
                                     activeforeground="indigo", cursor="hand2", font=("Comic Sans MS", 14, "bold"),
                                     height=1,width=15, relief=FLAT, overrelief=RIDGE)
        self.service_button.grid(row=5, column=0, padx=58, pady=7)

        #  Second Seprator
        self.second_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.second_seperator.configure(bg="black")
        self.second_seperator.grid(row=10, column=0)

        #  Second Button
        self.medicine_button = Button(self.frame2, text="Products", bd=1, bg='yellow', fg="black",
                                      activebackground="#73C2FB", activeforeground="indigo", cursor="hand2",
                                      font=("Comic Sans MS", 14, "bold"), height=1, width=15,
                                      relief=RIDGE, overrelief=RAISED)
        self.medicine_button.grid(row=20, column=0, padx=58, pady=7)

        # Third Seprator
        self.third_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.third_seperator.configure(bg="black")
        self.third_seperator.grid(row=25, column=0)

        # Third Button
        self.doctor_button = Button(self.frame2, text="Customers", bd=1, bg='red', fg="white", activebackground="#73C2FB",
                                    activeforeground="indigo", font=("Comic Sans MS", 14, "bold"), height=1,
                                    cursor="hand2", width=15, relief=RIDGE, overrelief=RAISED)
        self.doctor_button.grid(row=40, column=0, padx=30, pady=7)

        # Fourth Seprator
        self.fourth_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.fourth_seperator.configure(bg="black")
        self.fourth_seperator.grid(row=45, column=0)

        #  Fourth Button
        self.staff_button = Button(self.frame2, text="Staff", bd=1, bg='red', fg="white", activebackground="#73C2FB",
                                   activeforeground="indigo", font=("Comic Sans MS", 14, "bold"), height=1,
                                   cursor="hand2", width=15, relief=RIDGE, overrelief=RAISED)
        self.staff_button.grid(row=60, column=0, padx=30, pady=7)

        #  Fifth Seprator
        self.fifth_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.fifth_seperator.configure(bg="black")
        self.fifth_seperator.grid(row=65, column=0)


        self.show_menu()
        self.wn.mainloop()

        # Menu Button
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="Log Out", menu=log_out)
        log_out.add_cascade(label="Log Out", command=self.logout)


    #  Logging out
    def logout(self):
        self.wn.destroy()
        from interface.first_window import Firstwindow
        Firstwindow()




