# =========================== Importing all the necessary modules ============================#
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time as tm
import datetime
from Staff.staff_interface_backend import Staffbackend


class Staff_interface:
    # =============================== Creating Tkinter Window ================================#
    def __init__(self,staffloggedin):
        self.wn = Tk()
        self.wn.title("Staff Panel")
        self.wn.geometry("1370x735+0+0")
        self.wn.configure(bg="white")
        self.wn.resizable(False, False)
        self.staff_backend = Staffbackend()
        self.lastuserloggedin=staffloggedin
        self.update_index0=""
        self.update_index1=""

        # =========================== Importing all necessary photo =============================#
        self.title_photo = PhotoImage(file="C:\\store\\staff_logooo.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo, bg="white",bd=1,borderwidth=1)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=1, y=0)


        self.title_photo01 = PhotoImage(file="C:\\store\\staff_board_background.png")
        self.title_photo01_lable = Label(self.wn, image=self.title_photo01,bg="white")
        self.title_photo01_lable.image = self.title_photo01
        self.title_photo01_lable.place(x=280, y=0)

        # ===========================  Necessary Frames =============================#
        self.frame1 = LabelFrame(self.wn, bg="white")
        self.frame1.place(x=1, y=270)
        self.tree_frame = Frame(self.wn, bg="white")
        self.tree_frame.place(x=285, y=0)
        self.navigation_frame = Frame(self.wn, bg="white")
        self.navigation_frame.place(x=285, y=247)
        self.navigation_frame0 = LabelFrame(self.wn, bg="white", bd=2)
        self.navigation_frame0.place(x=1100, y=0)

        # ==================================== Major Heading ====================================#
        self.lb_heading_inital = Label(self.frame1, text="Staff", bg="white", font=('Impact', 34, 'bold', 'underline'),fg='red')
        self.lb_heading_inital.grid(row=20, column=40, padx=15, pady=10)
        self.lb_heading_end = Label(self.frame1, text="Panel", bg="white", font=('Impact', 34, 'bold', 'underline'),fg='blue')
        self.lb_heading_end.grid(row=20, column=80, padx=17, pady=10)

        # =================================== Creating Frame-2 ===================================#
        self.frame2 = LabelFrame(self.wn, bg="white")
        self.frame2.place(x=1, y=350)

        self.show_menu()
        self.wn.mainloop()

    # ==================================== Menu Button ====================================#
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="Log Out", menu=log_out)
        log_out.add_cascade(label="Log Out", command=self.logout)

    # =================================== Logging out ===================================#
    def logout(self):
        self.wn.destroy()
        from interface.first_window import Firstwindow
        Firstwindow()

    # ================================ END PHOTO =======================================#
    def endphoto(self):
        self.photo00 = PhotoImage(file="C:\\store\\logo.png")
        self.photo_lable00 = Label(self.navigation_frame0, image=self.photo00, bg="white")
        self.photo_lable00.image = self.photo00
        self.photo_lable00.grid(row=8, column=0, padx=5, pady=43)

# Staff_interface("test")