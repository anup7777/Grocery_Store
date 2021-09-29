from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time as tm
import datetime
from User.user_interface_backend import Customerbackend
from User.user_cart import cart


class Customer_interface:
    # Creating Tkinter window

    def __init__(self, customerloggedin, customerloggedinname):
        self.wn = Tk()
        self.wn.title("Customer Panel")
        self.wn.geometry("1370x735+0+0")
        self.wn.configure(bg="white")
        self.wn.resizable(False, False)
        self.customer_backend = Customerbackend()
        self.lastuserloggedin = customerloggedin
        self.lastuserloggedinname = customerloggedinname


        #  Necessary Frames
        self.frame1 = LabelFrame(self.wn, bg="white")
        self.frame1.place(x=0, y=150)
        self.entry_frame = Frame(self.wn, bg="white")
        self.entry_frame.place(x=300, y=20)
        self.tree_frame = LabelFrame(self.wn, bg="white", bd=2)
        self.tree_frame.place(x=500, y=0)
        self.navigation_frame = LabelFrame(self.wn, bg="white")
        self.navigation_frame.place(x=500, y=247)
        self.navigation_frame0 = LabelFrame(self.wn, bg="white", bd=2)
        self.navigation_frame0.place(x=1100, y=0)

        # Major Heading
        self.lb_heading_inital = Label(self.frame1, text="Customer", bg="white",
                                       font=('Impact', 34, 'bold', 'underline'), fg='red')
        self.lb_heading_inital.grid(row=20, column=40, padx=8, pady=12)
        self.lb_heading_end = Label(self.frame1, text="Panel", bg="white", font=('Impact', 34, 'bold', 'underline'),
                                    fg='blue')
        self.lb_heading_end.grid(row=20, column=80, padx=7, pady=12)

        # = Creating Frame-2
        self.frame2 = LabelFrame(self.wn, bg="white", borderwidth=2)
        self.frame2.place(x=0, y=350)

        self.frame3 = LabelFrame(self.wn, bg="white", borderwidth=2)
        self.frame3.place(x=250, y=350)

        # Creating Seprator and Buttons

        # First Button
        self.credentials_button = Button(self.frame2, text="Credentials", bg='green', fg="white",
                                         activebackground="#73C2FB", activeforeground="indigo", cursor="hand2",
                                         command=self.change_customer_credentials, font=("Comic Sans MS", 15, "bold"),
                                         height=1,
                                         width=15, relief=RIDGE, overrelief=RAISED)
        self.credentials_button.grid(row=5, column=0, padx=10, pady=70)

        self.cart_button = Button(self.frame3, text="View Items", bg='green', fg="white",
                                         activebackground="#73C2FB", activeforeground="indigo", cursor="hand2",
                                         command= self.show_items, font=("Comic Sans MS", 15, "bold"),
                                         height=1,
                                         width=15, relief=RIDGE, overrelief=RAISED)
        self.cart_button.grid(row=5, column=100, padx=10, pady=70)

        self.show_menu()
        self.wn.mainloop()

    # Menu Buttonrubi11

    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="Log Out", menu=log_out)
        log_out.add_cascade(label="Log Out", command=self.logout)

    # Changing Credentials

    def change_customer_credentials(self):

        self.deleteframe()
        self.display_date()
        self.display_time()

        #  Change Credential Logo
        self.change_credential_pic = PhotoImage(file="C:\\store\\change_credentials.png")
        self.change_credential_pic_lable = Label(self.tree_frame, image=self.change_credential_pic, bg="white")
        self.change_credential_pic_lable.image = self.change_credential_pic

        # First Seperator
        self.data0 = 22
        while self.data0 <= 800:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=0)
            self.data0 += 10

        # Second Seperator
        self.data = 22
        while self.data <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=230)
            self.data += 10

        #  Third Seprator
        self.data1 = 22
        while self.data1 <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=300)
            self.data1 += 10

        #  First label - Major heading
        self.changeboard_lbhead = Label(self.tree_frame, text="Change Credentials",
                                        image=self.change_credential_pic,
                                        compound=TOP, bg="white", font=('Arial', 18, 'bold', 'underline'),
                                        fg='Black')
        self.changeboard_lbhead.grid(row=2, column=1, columnspan=2, padx=115, pady=13)

        #  FIRST LABEL - NAME
        self.changeboard_lb1 = Label(self.navigation_frame, text="Username", bg="white", font=('Arial', 12, 'bold'),
                                     fg='Black')
        self.changeboard_lb1.grid(row=3, column=1, padx=10, pady=15)

        # Second LABEL - OLd Password
        self.changeboard_lb2 = Label(self.navigation_frame, text="Old Password", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.changeboard_lb2.grid(row=4, column=1, padx=10, pady=14)

        # Third LABEL - New password
        self.changeboard_lb3 = Label(self.navigation_frame, text="New Password", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.changeboard_lb3.grid(row=5, column=1, padx=10, pady=14)

        #  First Entry - Name
        self.changeboard_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.changeboard_entbx1.grid(row=3, column=2, padx=12, pady=15)

        #  Second Entry - old Passowrd
        self.changeboard_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.changeboard_entbx2.grid(row=4, column=2, padx=12, pady=15)

        #  Third Entry - New password
        self.changeboard_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.changeboard_entbx3.grid(row=5, column=2, padx=14, pady=15)

        # Fourth Entry - resenter password
        self.changeboard_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.changeboard_entbx4.grid(row=6, column=2, padx=13, pady=15)

        #  Fourth LABEL - Reenter pasword
        self.changeboard_lb4 = Label(self.navigation_frame, text="Re-enter New Password", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.changeboard_lb4.grid(row=6, column=1, padx=10, pady=14)

        # Required Buttons
        self.changeboard_btn1_img = PhotoImage(file="C:\\store\\updatebutton.png")
        self.changeboard_btn1 = Button(self.navigation_frame, image=self.changeboard_btn1_img,
                                       command=self.updating_credentials,
                                       bg="white", fg="black", font=("arial", 15), height=25, width=95)
        self.changeboard_btn1.image = self.changeboard_btn1_img
        self.changeboard_btn1.grid(row=7, column=1, columnspan=2, padx=10, pady=22)

        #  Fifth LABEL -Instruction to follow
        self.changeboard_lb5 = Label(self.navigation_frame, text="Please follow the following Instruction.",
                                     bg="white",
                                     font=('Arial', 12, 'bold', "underline"), fg='Black')
        self.changeboard_lb5.grid(row=8, column=1, columnspan=2, padx=10, pady=14)

        self.changeboard_lb6 = Label(self.navigation_frame, text="Ensure your password are 8 character long.\n\n"
                                                                 "Please don't use your birthdates, phone numbers for passwords.\n\n"
                                                                 "Passwords mustn't be shared with anyone.",
                                     bg="white",
                                     font=('Arial', 10, 'bold'), fg='Black')
        self.changeboard_lb6.grid(row=9, column=1, columnspan=2, pady=14)

    def updating_credentials(self):
        username = self.changeboard_entbx1.get()
        oldpassword = self.changeboard_entbx2.get()
        newpassword = self.changeboard_entbx3.get()
        retype_newpassword = self.changeboard_entbx4.get()
        if len(username) != 0 and len(oldpassword) != 0 and len(newpassword) != 0 and len(retype_newpassword) != 0:
            if username == self.lastuserloggedin.lower():
                if self.customer_backend.return_customer_search_data(username)[0][0] == oldpassword:
                    if len(newpassword) >= 8:
                        if newpassword == retype_newpassword:
                            self.customer_backend.update_customer_login_data(retype_newpassword, username)
                            messagebox.showinfo("Success", "Credentials changed.")
                        else:
                            messagebox.showerror("Password didn't matched",
                                                 "The password you provided in \n  both column are not identical.")
                    else:
                        messagebox.showerror("Password too Short.", "The password must be 8 character long.")
                else:
                    messagebox.showerror("Wrong Password", "The password you provided didn't matched.")
            else:
                messagebox.showerror("Unauthenticated user", "You can't change other people credentials.")
        else:
            messagebox.showerror("Empty Input", "You can't leave any boxes empty.")

    # DATE AND TIME SELECTED FRAME

    def display_time(self):
        current_time = tm.strftime('%I:%M:%S %p ')
        self.wn.after(200, self.display_time)
        clock_label = Label(self.navigation_frame0, text=current_time, font=("Ticking Timebomb BB Regular", 27),
                            bg='white', fg='#000000')
        clock_label.grid(row=0, column=0, padx=14)

    def display_date(self):
        x = datetime.datetime.now()
        current_date = x.strftime('%A,%B %d')
        date_label = Label(self.navigation_frame0, text=current_date, font="Ariel 15", bg='white', fg='#2b2b2b')
        date_label.grid(row=1, column=0, padx=15)

    #  DELETE LAST SELECTED FRAME

    def deleteframe(self):
        for widget in self.entry_frame.winfo_children():
            widget.destroy()

        for widget in self.navigation_frame.winfo_children():
            widget.destroy()

        for widget in self.navigation_frame0.winfo_children():
            widget.destroy()

        for widget in self.tree_frame.winfo_children():
            widget.destroy()

    #  Logging out

    def logout(self):
        self.wn.destroy()
        from interface.first_window import Firstwindow
        Firstwindow()

    def show_items(self):
        self.wn.destroy()
        cart()





