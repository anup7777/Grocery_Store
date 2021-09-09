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
        self.tree_frame.place(x=310, y=0)

        #  Navigation Frame
        self.navigation_frame = Frame(self.wn, bg="white")
        self.navigation_frame.place(x=310, y=335)

        #  Navigation Frame
        self.navigation_frame0 = LabelFrame(self.wn, bg="white", bd=2)
        self.navigation_frame0.place(x=1123, y=0)

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
        self.product_button = Button(self.frame2, text="Products", bg='white', fg="black", activebackground="#73C2FB",
                                     activeforeground="indigo", cursor="hand2", font=("Comic Sans MS", 14, "bold"),
                                     height=1,width=15,command=self.product, relief=FLAT, overrelief=RIDGE)
        self.product_button.grid(row=5, column=0, padx=58, pady=7)

        #  Second Seprator
        self.second_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.second_seperator.configure(bg="black")
        self.second_seperator.grid(row=10, column=0)

        #  Second Button
        self.customer_button = Button(self.frame2, text="Customers", bd=1, bg='yellow', fg="black",
                                      activebackground="#73C2FB", activeforeground="indigo", cursor="hand2",
                                      font=("Comic Sans MS", 14, "bold"), height=1, width=15,command=self.customerboard,
                                      relief=RIDGE, overrelief=RAISED)
        self.customer_button.grid(row=20, column=0, padx=58, pady=7)

        # Third Seprator
        self.third_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.third_seperator.configure(bg="black")
        self.third_seperator.grid(row=25, column=0)

        # Third Button
        self.staff_button = Button(self.frame2, text="Staffs", bd=1, bg='red', fg="white", activebackground="#73C2FB",
                                    activeforeground="indigo", font=("Comic Sans MS", 14, "bold"), height=1,
                                    cursor="hand2", width=15,command=self.staffboard, relief=RIDGE, overrelief=RAISED)
        self.staff_button.grid(row=40, column=0, padx=30, pady=7)

        # Fourth Seprator
        self.fourth_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.fourth_seperator.configure(bg="black")
        self.fourth_seperator.grid(row=45, column=0)

        self.show_menu()
        self.wn.mainloop()

        # Menu Button
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="Log Out", menu=log_out)
        log_out.add_cascade(label="Log Out", command=self.logout)

        # Window for PRODUCT Button

    def product(self):
        self.deleteframe()
        self.endphoto()
        self.display_date()
        self.display_time()

        # First Seperator
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=5)
            self.data0 += 10

        #  SCEOND Seperator
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=65)
            self.data += 10

        # Product Logo
        self.product_photo = PhotoImage(
            file="C:\\store\\product_logo.png")
        self.product_photo_lable = Label(self.navigation_frame0, image=self.product_photo, bg="white")
        self.product_photo_lable.image = self.product_photo
        self.product_photo_lable.grid(row=3, column=0, padx=5)

        #  FIRST label - NAME
        self.product_lb1 = Label(self.navigation_frame, text="Name of the Product", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.product_lb1.grid(row=2, column=1, padx=5, pady=10)

        #  SECEOND label - TYPE
        self.product_lb2 = Label(self.navigation_frame, text="Type of the Product", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.product_lb2.grid(row=3, column=1, padx=5, pady=10)

        #  THIRD label - PRICE
        self.product_lb3 = Label(self.navigation_frame, text="Price of the Product", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.product_lb3.grid(row=4, column=1, padx=5, pady=10)

        #  FOURTH label - COMPANY
        self.product_lb4 = Label(self.navigation_frame, text="Company of the Product", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.product_lb4.grid(row=5, column=1, padx=5, pady=10)

        # FIFTH label - EXPIRY
        self.product_lb5 = Label(self.navigation_frame, text="Expiry of the Product", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.product_lb5.grid(row=6, column=1, padx=5, pady=10)

        # FIRST ENTRY - NAME
        self.product_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.product_entbx1.grid(row=2, column=2, padx=12, pady=6)

        # SCEOND ENTRY - TYPE
        self.product_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.product_entbx2.grid(row=3, column=2, padx=13, pady=4)

        #  THIRD ENTRY - PRICE
        self.product_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.product_entbx3.grid(row=4, column=2, padx=13, pady=4)

        #  FOURTH ENTRY - COMPANY
        self.product_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.product_entbx4.grid(row=5, column=2, padx=13, pady=4)

        #  FIFTH ENTRY - EXPIRY
        self.product_entbx5 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.product_entbx5.grid(row=6, column=2, padx=13, pady=4)

        #  PRODUCT TREE
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.product_tree = ttk.Treeview(self.tree_frame,
                                         column=("Name", "Type", "Price", "Company", "Expiry Date"),
                                         yscrollcommand=self.yscroll.set, height=16)
        self.yscroll.config(command=self.product_tree.yview)
        self.product_tree.pack()

        self.product_tree['show'] = 'headings'

        self.product_tree.column('Name', width=170)
        self.product_tree.column('Type', width=150)
        self.product_tree.column('Price', width=150)
        self.product_tree.column('Company', width=155)
        self.product_tree.column('Expiry Date', width=170)

        self.product_tree.heading('Name', text="Product Name")
        self.product_tree.heading('Type', text="Type")
        self.product_tree.heading('Price', text="Rate")
        self.product_tree.heading('Company', text="Company")
        self.product_tree.heading('Expiry Date', text="Expiry Date")

        #  ADD Button with picture inserted
        self.product_addbutton_img = PhotoImage(
            file="C:\\store\\addbutton.png")
        self.product_addbutton = Button(self.navigation_frame, image=self.product_addbutton_img,
                                        command=self.addproduct, bg="white", fg="black", font=("arial", 15),
                                        height=25, width=95)
        self.product_addbutton.image = self.product_addbutton_img
        self.product_addbutton.grid(row=15, column=2, padx=10, pady=14)

        # SHOW Button with picture inserted
        self.product_showbutton_img = PhotoImage(
            file="C:\\store\\showbutton.png")
        self.product_showbutton = Button(self.navigation_frame, image=self.product_showbutton_img,
                                         command=self.showitemintree_productdata, bg="white", fg="black",
                                         font=("arial", 15), height=37, width=145)
        self.product_showbutton.image = self.product_showbutton_img
        self.product_showbutton.grid(row=1, column=1, columnspan=3, padx=331, pady=14)

        #  UPDATE Button with picture inserted
        self.product_updatebutton_img = PhotoImage(
            file="C:\\store\\updatebutton.png")
        self.product_updatebutton = Button(self.navigation_frame, image=self.product_updatebutton_img,
                                           command=self.product_updatefrntend, bg="white", fg="black",
                                           font=("arial", 15), height=25, width=95)
        self.product_updatebutton.image = self.product_updatebutton_img
        self.product_updatebutton.grid(row=15, column=1, padx=10, pady=14)

        #  DELETE Button with picture inserted
        self.product_deletebutton_img = PhotoImage(
            file="C:\\store\\deletebutton.png")
        self.product_deletebutton = Button(self.navigation_frame, image=self.product_deletebutton_img,
                                           command=self.deleteproduct, bg="white", fg="black", font=("arial", 15),
                                           height=25, width=95)
        self.product_deletebutton.image = self.product_deletebutton_img
        self.product_deletebutton.grid(row=15, column=1, columnspan=2, padx=10, pady=14)

        # SEARCH Button with picture inserted
        self.product_searchbutton_img = PhotoImage(
            file="C:\\store\\searchbuton.png")
        self.product_searchbutton = Button(self.navigation_frame0, image=self.product_searchbutton_img,
                                           command=self.productsearch, bg="white", fg="black", font=("arial", 15),
                                           height=25, width=95)
        self.product_searchbutton.image = self.product_searchbutton_img
        self.product_searchbutton.grid(row=6, column=0, padx=10, pady=10)

        #  SEARCH COMBOBOX VALUE
        self.product_search_obj = StringVar()
        self.productboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                   textvariable=self.product_search_obj, width=27, height=5)
        self.productboard_searchbox['values'] = ["Product_name", "Product_type", "Product_price",
                                                 "Product_company", "Product_expiry"]
        self.productboard_searchbox.grid(row=4, column=0, pady=10)

        # SEARCH ENTRYBOX VALUE
        self.product_search_value = StringVar()
        self.productboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.product_search_value,
                                             bg="white", fg="black", font=("arial", 12, "bold"))
        self.productboard_searchbx10.grid(row=5, column=0, padx=15, pady=10)

        #  THIRD SEPRATOR
        self.data1 = 22
        while self.data1 <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=412)
            self.data1 += 10

        #  ADDING PRODUCTS

    def addproduct(self):
        pro_name = self.product_entbx1.get()
        pro_type = self.product_entbx2.get()
        pro_price = self.product_entbx3.get()
        pro_company = self.product_entbx4.get()
        pro_expiry = self.product_entbx5.get()
        if len(pro_name) != 0 and len(pro_type) != 0 and len(pro_price) != 0 and len(
                pro_company) != 0 and len(pro_expiry) != 0:
            if pro_price.isdigit():
                if self.admin_backend.product_add(pro_name, pro_type, pro_price, pro_company, pro_expiry):
                    messagebox.showinfo('Success', "Product Added")
                    self.showitemintree_productdata()
                    self.update_index1 = ""
                else:
                    messagebox.showerror("Error", "Can't add your product.")
            else:
                messagebox.showerror("Error", "Price must be an integer.")
        else:
            messagebox.showerror("Error", "Can't leave any blank spaces.")

        # = SHOWING DATA IN PRODUCT_TREE

    def showitemintree_productdata(self):
        self.product_tree.delete(*self.product_tree.get_children())
        reqdata = self.admin_backend.product_backend_showdata()
        for i in reqdata:
            self.product_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
        self.product_tree.bind("<Double-1>", self.product_onitemselect)

        # SELECTING DATA FROM PRODUCT TREE

    def product_onitemselect(self, event):
        selected_row00 = self.product_tree.selection()[0]
        selected_item00 = self.product_tree.item(selected_row00, 'values')
        self.update_index00 = self.product_tree.item(selected_row00, 'text')

        self.product_entbx1.delete(0, END)
        self.product_entbx1.insert(0, selected_item00[0])
        self.product_entbx2.delete(0, END)
        self.product_entbx2.insert(0, selected_item00[1])
        self.product_entbx3.delete(0, END)
        self.product_entbx3.insert(0, selected_item00[2])
        self.product_entbx4.delete(0, END)
        self.product_entbx4.insert(0, selected_item00[3])
        self.product_entbx5.delete(0, END)
        self.product_entbx5.insert(0, selected_item00[4])

        #  UPDATING PRODUCT DATA

    def product_updatefrntend(self):
        if self.update_index00 == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            pro_name = self.product_entbx1.get()
            pro_type = self.product_entbx2.get()
            pro_price = self.product_entbx3.get()
            pro_company = self.product_entbx4.get()
            pro_expiry = self.product_entbx5.get()
            if len(pro_name) != 0 and len(pro_type) != 0 and len(pro_price) != 0 and len(
                    pro_company) != 0 and len(pro_expiry) != 0:
                if pro_price.isdigit():
                    if self.admin_backend.product_status_update(self.update_index00, pro_name, pro_type, pro_price,
                                                                pro_company, pro_expiry):
                        messagebox.showinfo('Item', "Item Updated")
                        self.showitemintree_productdata()
                        self.update_index00 = ""
                    else:
                        messagebox.showerror("Error", 'Can not be updated !!!')
                else:
                    messagebox.showerror("Error", "Price must be an integer.")
            else:
                messagebox.showerror("Error", "Can't leave any blank spaces.")

        #  SEARCHING PRODUCT DATA

    def productsearch(self):
        if len(self.product_search_value.get()) != 0 and len(self.product_search_obj.get()) != 0:
            searcheed_data00 = self.admin_backend.return_product_search_data(self.product_search_value.get(),
                                                                             self.product_search_obj.get())
            if len(searcheed_data00) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.product_tree.delete(*self.product_tree.get_children())
            else:
                self.product_tree.delete(*self.product_tree.get_children())
                for i in searcheed_data00:
                    self.product_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.product_tree.bind("<Double-1>", self.product_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

        #  Delete Product

    def deleteproduct(self):
        if self.update_index00 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.admin_backend.delete_product(self.update_index00):
                messagebox.showinfo("Product Deleted", "The product is now deleted.")
                self.showitemintree_productdata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

        #  Customer Board

    def customerboard(self):
        self.deleteframe()
        self.endphoto()
        self.display_date()
        self.display_time()

        # FIRST SEPERATOR
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=2)
            self.data0 += 10

        #  SECOND SEPERATOR
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=55)
            self.data += 10

        # Customer Logo
        self.customer_photoo = PhotoImage(
            file="C:\\store\\customer_logo.png")
        self.customer_photoo_lable = Label(self.navigation_frame0, image=self.customer_photoo, bg="white")
        self.customer_photoo_lable.image = self.customer_photoo
        self.customer_photoo_lable.grid(row=3, column=0, padx=2)

        # FIRST LABEL - NAME
        self.customerboard_lb1 = Label(self.navigation_frame, text="Name of the Customer", bg="white",
                                       font=('Arial', 12, 'bold'), fg='Black')
        self.customerboard_lb1.grid(row=2, column=1, padx=10, pady=8)

        # SCEOND LABEL - AGE
        self.customerboard_lb2 = Label(self.navigation_frame, text="Age of the Customer", bg="white",
                                       font=('Arial', 12, 'bold'), fg='Black')
        self.customerboard_lb2.grid(row=3, column=1, padx=10, pady=8)

        # THIRD LABEL - GENDER
        self.customerboard_lb3 = Label(self.navigation_frame, text="Gender of the Customer", bg="white",
                                       font=('Arial', 12, 'bold'), fg='Black')
        self.customerboard_lb3.grid(row=4, column=1, padx=10, pady=8)

        #  FOURTH LABEL - ADDRESS
        self.customerboard_lb4 = Label(self.navigation_frame, text="Address of the Customer", bg="white",
                                       font=('Arial', 12, 'bold'), fg='Black')
        self.customerboard_lb4.grid(row=5, column=1, padx=10, pady=8)

        # FIFTH LABEL - EMAIL
        self.customerboard_lb5 = Label(self.navigation_frame, text="Email of the Customer", bg="white",
                                       font=('Arial', 12, 'bold'), fg='Black')
        self.customerboard_lb5.grid(row=6, column=1, padx=10, pady=6)

        # SIXTH LABEL - ADMIN APPROVAL
        self.customerboard_lb6 = Label(self.navigation_frame, text="Admin Approval", bg="white",
                                       font=('Arial', 12, 'bold'), fg='Black')
        self.customerboard_lb6.grid(row=7, column=1, padx=10, pady=8)

        # FIRST ENTRY - NAME
        self.customerboard_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.customerboard_entbx1.grid(row=2, column=2, padx=10, pady=5)

        #  SCEOND ENTRY - AGE
        self.customerboard_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.customerboard_entbx2.grid(row=3, column=2, padx=10, pady=5)

        #  THIRD ENTRY - GENDER
        self.customerboard_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.customerboard_entbx3.grid(row=4, column=2, padx=10, pady=5)

        #  FOURTH ENTRY - ADDRESS
        self.customerboard_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.customerboard_entbx4.grid(row=5, column=2, padx=10, pady=5)

        #  FIFTH ENTRY - EMAIL
        self.customerboard_entbx5 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.customerboard_entbx5.grid(row=6, column=2, padx=10, pady=5)

        #  ADMIN APPROVAL_COMBOBOX
        self.customerboard_entbx6 = ttk.Combobox(self.navigation_frame, width=33, height=2)
        self.customerboard_entbx6.grid(row=7, column=2)
        self.customerboard_entbx6['values'] = ["Yes", "No"]

        #  CUSTOMER SEARCH COMBOBOX VALUE
        self.customer_search_obj = StringVar()
        self.customerboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                    textvariable=self.customer_search_obj, width=27, height=5)
        self.customerboard_searchbox['values'] = ["Customer_Name", "Customer_Age", "Customer_Gender",
                                                  "Customer_Address", "Customer_Email", "Admin_Approval"]
        self.customerboard_searchbox.grid(row=4, column=0, pady=10)

        #  CUSTOMER SEARCH VALUE
        self.customer_search_value = StringVar()
        self.customerboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.customer_search_value,
                                              bg="white",
                                              fg="black", font=("arial", 12, "bold"))
        self.customerboard_searchbx10.grid(row=5, column=0, pady=10)

        # CUSTOMER TREE
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=LEFT, fill=Y)
        self.customerboard_tree = ttk.Treeview(self.tree_frame, column=(
            "Name", "Age", "Gender", "Address", "Email", "Admin Approval"),
                                               yscrollcommand=self.yscroll.set, height=17)
        self.yscroll.config(command=self.customerboard_tree.yview)
        self.customerboard_tree.pack()
        self.customerboard_tree['show'] = 'headings'

        self.customerboard_tree.column('Name', width=160)
        self.customerboard_tree.column('Age', width=90)
        self.customerboard_tree.column('Gender', width=110)
        self.customerboard_tree.column('Address', width=120)
        self.customerboard_tree.column('Email', width=160)
        self.customerboard_tree.column('Admin Approval', width=155)

        self.customerboard_tree.heading('Name', text="Name")
        self.customerboard_tree.heading('Age', text="Age")
        self.customerboard_tree.heading('Address', text="Address")
        self.customerboard_tree.heading('Gender', text="Gender")
        self.customerboard_tree.heading('Email', text="Email")
        self.customerboard_tree.heading('Admin Approval', text="Admin Approval")

        # SHOW Button with picture inserted
        self.customerboard_showbutton_img = PhotoImage(
            file="C:\\store\\showbutton.png")
        self.customerboard_showbutton = Button(self.navigation_frame, image=self.customerboard_showbutton_img,
                                               command=self.showitemintree_customerdata, bg="white", fg="black",
                                               font=("arial", 15), height=40, width=120)
        self.customerboard_showbutton.image = self.customerboard_showbutton_img
        self.customerboard_showbutton.grid(row=1, column=1, columnspan=3, padx=344, pady=5)

        # UPDATE Button with picture inserted
        self.customerboard_updatebutton_img = PhotoImage(
            file="C:\\store\\updatebutton.png")
        self.customerboard_updatebutton = Button(self.navigation_frame, image=self.customerboard_updatebutton_img,
                                                 command=self.customer_status_updatefrntend, bg="white", fg="black",
                                                 font=("arial", 15), height=25, width=95)
        self.customerboard_updatebutton.image = self.customerboard_updatebutton_img
        self.customerboard_updatebutton.grid(row=15, column=2, padx=10, pady=12)

        #  DELETE Button with picture inserted
        self.customerboard_deletebutton_img = PhotoImage(
            file="C:\\store\\deletebutton.png")
        self.customerboard_deletebutton = Button(self.navigation_frame, image=self.customerboard_deletebutton_img,
                                                 command=self.deletecustomers, bg="white", fg="black",
                                                 font=("arial", 15),
                                                 height=25, width=95)
        self.customerboard_deletebutton.image = self.customerboard_deletebutton_img
        self.customerboard_deletebutton.grid(row=15, column=1, padx=10, pady=12)

        #  SEARCH Button with picture inserted
        self.customerboard_searchbutton_img = PhotoImage(
            file="C:\\store\\searchbuton.png")
        self.customerboard_searchbutton = Button(self.navigation_frame0, image=self.customerboard_searchbutton_img,
                                                 command=self.customersearch, bg="white", fg="black",
                                                 font=("arial", 15),
                                                 height=25, width=95)
        self.customerboard_searchbutton.image = self.customerboard_searchbutton_img
        self.customerboard_searchbutton.grid(row=6, column=0, pady=10)

        #  THIRD SEPERATOR
        self.data1 = 22
        while self.data1 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=420)
            self.data1 += 10

        # SHOWING CUSTOMER DATA IN TREE

    def showitemintree_customerdata(self):
        self.customerboard_tree.delete(*self.customerboard_tree.get_children())
        reqdata = self.admin_backend.customer_backend_showdata()
        for i in reqdata:
            self.customerboard_tree.insert("", "end", text=i[0],
                                           value=(i[1], i[4], i[5], i[6], i[7], i[8]))
        self.customerboard_tree.bind("<Double-1>", self.customerdata_onitemselect)

        # SELECTING VALUE IN CUSTOMER TREE

    def customerdata_onitemselect(self, event):
        selected_row = self.customerboard_tree.selection()[0]
        selected_item = self.customerboard_tree.item(selected_row, 'values')
        self.update_index = self.customerboard_tree.item(selected_row, 'text')
        # print(selected_item)

        self.customerboard_entbx1.delete(0, END)
        self.customerboard_entbx1.insert(0, selected_item[0])
        self.customerboard_entbx2.delete(0, END)
        self.customerboard_entbx2.insert(0, selected_item[1])
        self.customerboard_entbx3.delete(0, END)
        self.customerboard_entbx3.insert(0, selected_item[2])
        self.customerboard_entbx4.delete(0, END)
        self.customerboard_entbx4.insert(0, selected_item[3])
        self.customerboard_entbx5.delete(0, END)
        self.customerboard_entbx5.insert(0, selected_item[4])
        self.customerboard_entbx6.delete(0, END)
        self.customerboard_entbx6.insert(0, selected_item[5])

        #  UPDATING CUSTOMER DATA

    def customer_status_updatefrntend(self):
        if self.update_index == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            print(self.update_index)
            name = self.customerboard_entbx1.get()
            age = self.customerboard_entbx2.get()
            gender = self.customerboard_entbx3.get()
            address = self.customerboard_entbx4.get()
            email = self.customerboard_entbx5.get()
            admin_approval = self.customerboard_entbx6.get()

            if len(name) != 0 and len(age) != 0 and len(gender) != 0 and len(address) != 0 and len(email) != 0 and len(
                    admin_approval) != 0:
                if age.isdigit():
                    if self.admin_backend.customer_status_update(self.update_index, name, age, gender, address, email,
                                                                 admin_approval):
                        messagebox.showinfo('Item', "Item Updated")
                        self.showitemintree_customerdata()
                        self.update_index = ""
                    else:
                        messagebox.showerror("Error", 'Can not be updated !!!')
                else:
                    messagebox.showerror("Error", "Age must be an integer.")
            else:
                messagebox.showerror("Error", "You can't leave any blank spaces")

        #  SEARCH DOCTOR DATA

    def customersearch(self):
        if len(self.customer_search_value.get()) != 0 and len(self.customer_search_obj.get()) != 0:
            searcheed_data = self.admin_backend.return_customer_search_data(self.customer_search_value.get(),
                                                                            self.customer_search_obj.get())
            if len(searcheed_data) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.customerboard_tree.delete(*self.customerboard_tree.get_children())
            else:
                self.customerboard_tree.delete(*self.customerboard_tree.get_children())
                for i in searcheed_data:
                    self.customerboard_tree.insert("", "end", text=i[0],
                                                   value=(i[1], i[2], i[4], i[5], i[6], i[7]))
                self.customerboard_tree.bind("<Double-1>", self.customerdata_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

        # Delete CUSTOMERS

    def deletecustomers(self):
        if self.update_index == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.admin_backend.delete_customer(self.update_index):
                messagebox.showinfo("Customer Data Deleted", "The desired data is now deleted.")
                self.showitemintree_customerdata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

        #  STAFF BOARD

    def staffboard(self):
        self.deleteframe()
        self.endphoto()
        self.display_date()
        self.display_time()

        #  FIRST SEPERATOR
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=5)
            self.data0 += 10

        #  SECOND SEPERATOR
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=65)
            self.data += 10

        # Staff  Logo
        self.staff_photo = PhotoImage(
            file="C:\\store\\staff_logo.png")
        self.staff_photo_lable = Label(self.navigation_frame0, image=self.staff_photo, bg="white")
        self.staff_photo_lable.image = self.staff_photo
        self.staff_photo_lable.grid(row=3, column=0, padx=5)

        # FIRST LABEL - NAME
        self.staffboard_lb1 = Label(self.navigation_frame, text="Name of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb1.grid(row=2, column=1, padx=10, pady=10)

        # SCEOND LABEL - AGE
        self.staffboard_lb2 = Label(self.navigation_frame, text="Age of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb2.grid(row=3, column=1, padx=10, pady=10)

        #  THIRD LABEL - GENDER
        self.staffboard_lb3 = Label(self.navigation_frame, text="Gender of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb3.grid(row=4, column=1, padx=10, pady=10)

        #  FOURTH LABEL - ADDRESS
        self.staffboard_lb4 = Label(self.navigation_frame, text="Address of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb4.grid(row=5, column=1, padx=10, pady=10)

        #  FIFTH LABEL - ADMIN
        self.staffboard_lb5 = Label(self.navigation_frame, text="Admin Approval", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb5.grid(row=6, column=1, padx=10, pady=10)

        # FIRST ENTRY - NAME
        self.staffboard_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx1.grid(row=2, column=2, padx=10, pady=6)

        #  SECEOND ENTRY - AGE
        self.staffboard_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx2.grid(row=3, column=2, padx=10, pady=6)

        #  THIRD ENTRY - GENDER
        self.staffboard_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx3.grid(row=4, column=2, padx=10, pady=6)

        #  FOURTH ENTRY - ADDRESS
        self.staffboard_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx4.grid(row=5, column=2, padx=10, pady=6)

        #  FIFTH ENTRY - ADMIN
        self.staffboard_entbx5 = ttk.Combobox(self.navigation_frame, width=33, height=2)
        self.staffboard_entbx5.grid(row=6, column=2)
        self.staffboard_entbx5['values'] = ["Yes", "No"]

        #  STAFF TREE VIEW

        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.staffboard_tree = ttk.Treeview(self.tree_frame, column=(
            "Name", "Age", "Gender", "Address", "Admin Approval"),
                                            yscrollcommand=self.yscroll.set, height=16)
        self.yscroll.config(command=self.staffboard_tree.yview)
        self.staffboard_tree.pack()
        self.staffboard_tree['show'] = 'headings'

        self.staffboard_tree.column('Name', width=220)
        self.staffboard_tree.column('Age', width=120)
        self.staffboard_tree.column('Gender', width=120)
        self.staffboard_tree.column('Address', width=160)
        self.staffboard_tree.column('Admin Approval', width=175)

        self.staffboard_tree.heading('Name', text="Name")
        self.staffboard_tree.heading('Age', text="Age")
        self.staffboard_tree.heading('Gender', text="Gender")
        self.staffboard_tree.heading('Address', text="Address")
        self.staffboard_tree.heading('Admin Approval', text="Admin Approval")

        # SHOW Button with picture inserted
        self.staffboard_showbutton_img = PhotoImage(
            file="C:\\store\\showbutton.png")
        self.staffboard_showbutton = Button(self.navigation_frame, image=self.staffboard_showbutton_img,
                                            command=self.showitemintree_staffdata, bg="white", fg="black",
                                            font=("arial", 15), height=40, width=120)
        self.staffboard_showbutton.image = self.staffboard_showbutton_img
        self.staffboard_showbutton.grid(row=1, column=1, columnspan=3, padx=344, pady=10)

        #  UPDATE Button with picture inserted
        self.staffboard_updatebutton_img = PhotoImage(
            file="C:\\store\\updatebutton.png")
        self.staffboard_updatebutton = Button(self.navigation_frame, image=self.staffboard_updatebutton_img,
                                              command=self.staff_status_updatefrntend, bg="white", fg="black",
                                              font=("arial", 15), height=25, width=95)
        self.staffboard_updatebutton.image = self.staffboard_updatebutton_img
        self.staffboard_updatebutton.grid(row=22, column=2, padx=10, pady=15)

        #  DELETE Button with picture inserted
        self.staffboard_deletebutton_img = PhotoImage(
            file="C:\\store\\deletebutton.png")
        self.staffboard_deletebutton = Button(self.navigation_frame, image=self.staffboard_deletebutton_img,
                                              command=self.deletestaffs, bg="white", fg="black", font=("arial", 15),
                                              height=25, width=95)
        self.staffboard_deletebutton.image = self.staffboard_deletebutton_img
        self.staffboard_deletebutton.grid(row=22, column=1, padx=10, pady=15)

        # SEARCH Button with picture inserted
        self.staffboard_searchbutton_img = PhotoImage(
            file="C:\\store\\searchbuton.png")
        self.staffboard_searchbutton = Button(self.navigation_frame0, image=self.staffboard_searchbutton_img,
                                              command=self.staffsearch, bg="white", fg="black", font=("arial", 15),
                                              height=25, width=95)
        self.staffboard_searchbutton.image = self.staffboard_searchbutton_img
        self.staffboard_searchbutton.grid(row=6, column=0, padx=10, pady=10)

        # STAFF SEARCH COMBOBOX VALUE
        self.staff_search_obj = StringVar()
        self.staffboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                 textvariable=self.staff_search_obj, width=27, height=5)
        self.staffboard_searchbox['values'] = ["Staff_Name", "Staff_Age", "Staff_Gender", "Staff_Address"
            , "Admin_approval"]
        self.staffboard_searchbox.grid(row=4, column=0, pady=10)

        #  STAFF SEARCH VALUE
        self.staff_search_value = StringVar()
        self.staffboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.staff_search_value, bg="white",
                                           fg="black", font=("arial", 12, "bold"))
        self.staffboard_searchbx10.grid(row=5, column=0, padx=15, pady=10)

        #  THIRD SEPERATOR
        self.data1 = 22
        while self.data1 <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=410)
            self.data1 += 10

        #  SHOWING STAFF DATA IN TREE

    def showitemintree_staffdata(self):
        self.staffboard_tree.delete(*self.staffboard_tree.get_children())
        reqdata = self.admin_backend.staff_backend_showdata()
        for i in reqdata:
            self.staffboard_tree.insert("", "end", text=i[0], value=(i[1], i[4], i[5], i[6], i[7]))
        self.staffboard_tree.bind("<Double-1>", self.staffdata_onitemselect)

        # SELECTING STAFF DATA IN TREE

    def staffdata_onitemselect(self, event):
        selected_row1 = self.staffboard_tree.selection()[0]
        selected_item1 = self.staffboard_tree.item(selected_row1, 'values')
        self.update_index0 = self.staffboard_tree.item(selected_row1, 'text')

        self.staffboard_entbx1.delete(0, END)
        self.staffboard_entbx1.insert(0, selected_item1[0])
        self.staffboard_entbx2.delete(0, END)
        self.staffboard_entbx2.insert(0, selected_item1[1])
        self.staffboard_entbx3.delete(0, END)
        self.staffboard_entbx3.insert(0, selected_item1[2])
        self.staffboard_entbx4.delete(0, END)
        self.staffboard_entbx4.insert(0, selected_item1[3])
        self.staffboard_entbx5.delete(0, END)
        self.staffboard_entbx5.insert(0, selected_item1[4])

        #  UPDATING STAFF DATA IN TREE

    def staff_status_updatefrntend(self):
        if self.update_index0 == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            name = self.staffboard_entbx1.get()
            age = self.staffboard_entbx2.get()
            gender = self.staffboard_entbx3.get()
            address = self.staffboard_entbx4.get()
            admin_approval = self.staffboard_entbx5.get()

            if len(name) != 0 and len(age) != 0 and len(gender) != 0 and len(address) != 0 and len(admin_approval) != 0:
                if age.isdigit():
                    if self.admin_backend.staff_status_update(self.update_index0, name, age, gender, address
                            , admin_approval):
                        messagebox.showinfo('Item', "Item Updated")
                        self.showitemintree_staffdata()
                        self.update_index0 = ""
                    else:
                        messagebox.showerror("Error", 'Can not be updated !!!')
                else:
                    messagebox.showerror("Error", "Age must be an integer.")
            else:
                messagebox.showerror("Error", "Can't leave any blank spaces.")

        #  SEARCHING STAFF DATA IN TREE

    def staffsearch(self):
        if len(self.staff_search_value.get()) != 0 and len(self.staff_search_obj.get()) != 0:
            searcheed_data02 = self.admin_backend.return_staff_search_data(self.staff_search_value.get(),
                                                                           self.staff_search_obj.get())
            if len(searcheed_data02) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.staffboard_tree.delete(*self.staffboard_tree.get_children())
            else:
                self.staffboard_tree.delete(*self.staffboard_tree.get_children())
                for i in searcheed_data02:
                    self.staffboard_tree.insert("", "end", text=i[0],
                                                value=(i[1], i[4], i[5], i[6]))
                self.staffboard_tree.bind("<Double-1>", self.staffdata_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

        #  Delete Staffs

    def deletestaffs(self):
        if self.update_index0 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.admin_backend.delete_staffs(self.update_index0):
                messagebox.showinfo("Staff Data Deleted", "The desired data is now deleted.")
                self.showitemintree_staffdata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

        # DATE AND TIME SELECTED FRAME

    def display_time(self):
        current_time = tm.strftime('%I:%M:%S %p ')
        self.wn.after(200, self.display_time)
        clock_label = Label(self.navigation_frame0, text=current_time, font=("Ticking Timebomb BB Regular", 27),
                            bg='white', fg='#000000')
        clock_label.grid(row=0, column=0, padx=12, pady=2)

    def display_date(self):
        x = datetime.datetime.now()
        current_date = x.strftime('%A,%B %d')
        date_label = Label(self.navigation_frame0, text=current_date, font="Ariel 15", bg='white', fg='#2b2b2b')
        date_label.grid(row=1, column=0, pady=2)

        # DELETE LAST SELECTED FRAME

    def deleteframe(self):
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

    #  END PHOTO
    def endphoto(self):
        self.photo00 = PhotoImage(
            file="C:\\store\\end_photo.png")
        self.photo_lable00 = Label(self.navigation_frame0, image=self.photo00, bg="white")
        self.photo_lable00.image = self.photo00
        self.photo_lable00.grid(row=8, column=0, padx=5, pady=43)



