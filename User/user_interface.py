from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time as tm
import datetime
from User.user_interface_backend import Customerbackend


class Customer_interface:
    # Creating Tkinter window

    def __init__(self, customerloggedin, customerloggedinname):
        self.wn = Tk()
        self.wn.title("Customerr Panel")
        self.wn.geometry("1370x735+0+0")
        self.wn.configure(bg="white")
        self.wn.resizable(False, False)
        self.customer_backend = Customerbackend()
        self.lastuserloggedin = customerloggedin
        self.lastuserloggedinname = customerloggedinname

        self.wn.mainloop()


