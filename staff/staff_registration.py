from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from admin.connection import MyDatabase

class Staffregistrationwindow:
    def __init__(self):
        self.wn=Tk()
        self.wn.title("Staff Registration")
        self.wn.geometry("1350x735+0+0")
        self.wn.resizable(False,False)
        self.show_menu()


        #  Importing all necessary photo
        self.background = PhotoImage(file="C:\\store\\secondbackground.png")
        self.background_lable = Label(self.wn, image=self.background,bg="white")
        self.background_lable.image = self.background
        self.background_lable.place(x=0, y=0)

        self.title0_photo = PhotoImage(file="C:\\store\\mobile.png")
        self.title0_photo_lable = Label(self.wn, image=self.title0_photo, bd=0)
        self.title0_photo_lable.image = self.title0_photo
        self.title0_photo_lable.place(x=50, y=10)

        self.title0_photo = PhotoImage(file="C:\\store\\register1.png")
        self.title0_photo_lable = Label(self.wn, image=self.title0_photo, bd=0)
        self.title0_photo_lable.image = self.title0_photo
        self.title0_photo_lable.place(x=700, y=10)

        #  Creating Frames
        self.staff_frame=Frame(self.wn,bg="white")
        self.staff_frame.place(x=750, y=75)

        self.staff_frame1 = Frame(self.wn, bg="white")
        self.staff_frame1.place(x=750, y=15)

        self.staff_frame2 = Frame(self.wn, bg="white")
        self.staff_frame2.place(x=890, y=15)

        #  Major Heading
        self.lb_heading = Label(self.staff_frame1, text="Staffs",font=('Impact',25,'bold',"underline"),justify="right", fg='red',bg="white")
        self.lb_heading.grid(row=0, column=0,columnspan=1,padx=52,pady=1)

        self.lb_heading2 = Label(self.staff_frame2, text="Registration",font=('Impact',25,'bold',"underline"),justify="left", fg='blue',bg="white")
        self.lb_heading2.grid(row=0, column=1,columnspan=1,padx=39,pady=1)

        #  Picture With Label
        self.title01_photo = PhotoImage(file="C:\\store\\staff.png")
        self.title01_photo_lable = Label(self.staff_frame, image=self.title01_photo, bg="white")
        self.title01_photo_lable.image = self.title01_photo

        #  All Labels
        self.lb_staffname = Label(self.staff_frame, bg="white", fg="Black",
                                  font=("cambria", 15, 'bold', "underline"), image=self.title01_photo, compound=TOP,
                                  justify="center")
        self.lb_staffname.grid(row=1, column=0, columnspan=2, padx=7, pady=8)

        self.lb_staffname = Label(self.staff_frame, text="Staff's Name:", bg="white", fg="Blue",
                                  font=("cambria", 15, 'bold'), justify="center")
        self.lb_staffname.grid(row=3, column=0, padx=7, pady=3)

        self.lb_username = Label(self.staff_frame, text="Username:", bg="white", fg="Blue",
                                 font=("cambria", 15, 'bold'), justify="center")
        self.lb_username.grid(row=5, column=0, padx=7, pady=3)

        self.lb_password = Label(self.staff_frame, text="Password:", bg="white", fg="Blue",
                                 font=("cambria", 15, 'bold'), justify="center")
        self.lb_password.grid(row=7, column=0, padx=7, pady=3)

        self.lb_staffage = Label(self.staff_frame, text="Staff's Age:", bg="white", fg="Blue",
                                 font=("cambria", 15, 'bold'), justify="center")
        self.lb_staffage.grid(row=15, column=0, padx=7, pady=3)

        self.lb_staffgender = Label(self.staff_frame, text="Staff's Gender:", bg="white", fg="Blue",
                                    font=("cambria", 15, 'bold'), justify="center")
        self.lb_staffgender.grid(row=20, column=0, padx=7, pady=3)

        self.lb_staffaddress = Label(self.staff_frame, text="Staff's Address:", bg="white", fg="Blue",
                                     font=("cambria", 15, 'bold'), justify="center")
        self.lb_staffaddress.grid(row=25, column=0, padx=7, pady=3)


        #  All Entries
        self.ent_staffname = Entry(self.staff_frame, bg="white", fg="black", font=("arial", 15, "bold"),
                                   justify="center")
        self.ent_staffname.grid(row=3, column=1, padx=10, pady=3)

        self.ent_username = Entry(self.staff_frame, bg="white", fg="black", font=("arial", 15, "bold"),
                                  justify="center")
        self.ent_username.grid(row=5, column=1, padx=10, pady=3)

        self.ent_pass = Entry(self.staff_frame, bg="white", fg="black", font=("arial", 15, "bold"), show="*",
                              justify="center")
        self.ent_pass.grid(row=7, column=1, padx=10, pady=3)

        self.ent_staffage = Entry(self.staff_frame, bg="white", fg="black", font=("arial", 15, "bold"),
                                  justify="center")
        self.ent_staffage.grid(row=15, column=1, padx=10, pady=3)

        self.ent_staffgender = Entry(self.staff_frame, bg="white", fg="black", font=("arial", 15, "bold"),
                                     justify="center")
        self.ent_staffgender.grid(row=20, column=1, padx=10, pady=3)

        self.ent_staffaddress = Entry(self.staff_frame, bg="white", fg="black", font=("arial", 15, "bold"),
                                      justify="center")
        self.ent_staffaddress.grid(row=25, column=1, padx=10, pady=3)


        #  All Buttons
        self.create_account_button_photo = PhotoImage(file="C:\\store\\signup.png")
        self.create_account_button_photo_button = Button(self.staff_frame, image=self.create_account_button_photo,
                                                         bg='white', fg="#3498eb", activebackground="#73C2FB",
                                                         cursor="hand2", command=self.registering_staff,
                                                         font=("bold", 13), height=39, width=180, bd=0)
        self.create_account_button_photo_button.image = self.create_account_button_photo
        self.create_account_button_photo_button.grid(row=50, columnspan=2, padx=7, pady=20)

        self.my_database = MyDatabase()
        self.wn.mainloop()

    #  Regestring the Staff
    def registering_staff(self):
        name = self.ent_staffname.get()
        username = self.ent_username.get()
        password = self.ent_pass.get()
        age = self.ent_staffage.get()
        gender = self.ent_staffgender.get()
        address = self.ent_staffaddress.get()

        if len(name) != 0 and len(username) != 0 and len(password) != 0 and len(age) != 0 and len(gender) != 0 and len(
                address) != 0 :
            if age.isdigit():
                qry = "INSERT INTO staff_credentials (Staff_Name,username,password,Staff_Age,Staff_Gender,Staff_Address,Staff_Qualification,Staff_University,Staff_Email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (name, username, password, age, gender, address)
                self.my_database.add_update_delete(qry, values)
                messagebox.showinfo("Registration Successful.", "Please wait until \n admin approval for login.")
            else:
                messagebox.showerror("Numeric Data Needed.", "Age can't be a string value.")
        else:
            messagebox.showerror("Blank Space Detected", "You can't leave any entry boxes empty.")

    #  MENU Button
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="<-- Back", menu=log_out)
        log_out.add_cascade(label="<-- Back", command=self.logout)

    # =================================== Logging out ===================================#
    def logout(self):
        self.wn.destroy()
        from Staff.staff_login_interface import Staffwindow
        Staffwindow()




