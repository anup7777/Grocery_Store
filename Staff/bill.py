from tkinter import *
import math,random
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import smtplib
from tkinter import Tk, Label, Frame, Entry, Button
from subprocess import Popen



class Bill_App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1350x700")
        self.master.title("Bill")
        # adding icon image
        self.img = (Image.open("C:\\store\\staff_icon.jpg"))
        self.icoimg = ImageTk.PhotoImage(self.img)
        self.master.iconphoto(False, self.icoimg)
        self.master.resizable(False, False)

        title = Label(self.master, text="BILL", bd=8, relief=GROOVE, bg="dark orange",
                      font=("times new roman", 27, "bold"), pady=2).pack(fill=X)



        #    variable

        #   snack & crackers
        self.pringles = IntVar()
        self.lays = IntVar()
        self.kurkure = IntVar()
        self.potato_biscuit = IntVar()
        self.monaco = IntVar()
        self.oreo = IntVar()

        # rice & grains varible
        self.chickpeas = IntVar()
        self.rajma = IntVar()
        self.maize = IntVar()
        self.peas = IntVar()
        self.rice = IntVar()
        self.daal = IntVar()

        # beverages
        self.fanta = IntVar()
        self.coca_cola = IntVar()
        self.soda = IntVar()
        self.old_darbar = IntVar()
        self.vodka = IntVar()
        self.big_master = IntVar()

        # fruit & vegetable

        self.apple = IntVar()
        self.banana = IntVar()
        self.oranges = IntVar()
        self.onion = IntVar()
        self.tomato = IntVar()
        self.spanich = IntVar()

        #   bakery & dairy
        self.bread = IntVar()
        self.crossiant = IntVar()
        self.doughnut = IntVar()
        self.butter = IntVar()
        self.paneer = IntVar()
        self.ddc_milk = IntVar()

        # product price varible

        self.snacks_price = StringVar()
        self.riceandgrains_price = StringVar()
        self.cold_drink_price = StringVar()
        self.fruitsandvegetables_price = StringVar()
        self.backeryanddairy_price = StringVar()

        # tax varible

        self.snacks_tax = StringVar()
        self.riceandgrains_tax = StringVar()
        self.beverages_tax = StringVar()
        self.fruitsandvegetables_tax = StringVar()
        self.backeryanddairy_tax = StringVar()

        # customer details

        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.c_mail = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        # admin
        self.admin_id = StringVar()
        self.admin_pass = StringVar()

        # CUSTOMER DETAILS
        F0 = LabelFrame(self.master, bd=8, relief=GROOVE, text="Customer Details",
                        font=("times new roman", 15, "bold"), fg="black", bg="dark orange")
        F0.place(x=0, y=58, width=1350)

        cname_label = Label(F0, text="Customer Name", bg="dark orange", font=("times new romen", 18, "bold")).place(x=150, y=3)
        cname_txt = Entry(F0, width=18, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=2, padx=350, pady=3)

        cphn_label = Label(F0, text="Phone No.", bg="dark orange", font=("times new romen", 18, "bold")).place(x=700, y=3)
        cphn_txt = Entry(F0, width=18, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).place(x=850, y=3)
        # Snack & crackers frame
        F2 = LabelFrame(self.master, bd=5, relief=GROOVE, text="Snacks & Crackers", font=("times new roman", 15, "bold"),
                        fg="black", bg="dark orange")
        F2.place(x=5, y=140, width=200, height=393)

        pringles_txt = Entry(F2, width=2, textvariable=self.pringles, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10, sticky=W)
        pringles_label = Label(F2, text="Pringles", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        # lays
        lays_label = Label(F2, text="Lays", font=("times new roman", 16, "bold"), fg="black",
                                bg="dark orange").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        lays_txt = Entry(F2, width=2, textvariable=self.lays, font=("times new roman", 16, "bold"), bd=5,
                              relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Kurkure
        kurkure_label = Label(F2, text="Kurkure", font=("times new roman", 16, "bold"), fg="black",
                               bg="dark orange").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        kurkure_txt = Entry(F2, width=2, textvariable=self.kurkure, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # potato_biscuit
        potato_biscuit_label = Label(F2, text="Potata", font=("times new roman", 16, "bold"), fg="black",
                                bg="dark orange").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        potato_biscuit_txt = Entry(F2, width=2, textvariable=self.potato_biscuit, font=("times new roman", 16, "bold"), bd=5,
                              relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Monaco
        Monaco_label = Label(F2, text="Monaco", font=("times new roman", 16, "bold"), fg="black",
                               bg="dark orange").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Monaco_txt = Entry(F2, width=2, textvariable=self.monaco, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # oreo
        oreo_label = Label(F2, text="Oreo", font=("times new roman", 16, "bold"), fg="black",
                              bg="dark orange").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        oreo_txt = Entry(F2, width=2, textvariable=self.oreo, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10, sticky=W)


        #  riceandgrains frame
        F3 = LabelFrame(self.master, bd=5, relief=GROOVE, text="Rice & Grains", font=("times new roman", 15, "bold"),
                        fg="black", bg="dark orange")
        F3.place(x=205, y=140, width=210, height=393)

        g1_label = Label(F3, text="Chickpeas", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g1_txt = Entry(F3, width=4, textvariable=self.chickpeas, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=1, pady=10, sticky=W)

        g2_label = Label(F3, text="Rajma", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=1,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g2_txt = Entry(F3, width=4, textvariable=self.rajma, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=1, pady=10, sticky=W)

        g3_label = Label(F3, text="Maize", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g3_txt = Entry(F3, width=4, textvariable=self.maize, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=1, pady=10, sticky=W)

        g4_label = Label(F3, text="Peas", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=4, textvariable=self.peas, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=1, pady=10, sticky=W)

        g5_label = Label(F3, text="Daal", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=4,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g5_txt = Entry(F3, width=4, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=1, pady=10, sticky=W)

        g6_label = Label(F3, text="Rice", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=5,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g6_txt = Entry(F3, width=4, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=1, pady=10, sticky=W)

        #  beverages frame
        F4 = LabelFrame(self.master, bd=5, relief=GROOVE, text="Beverages", font=("times new roman", 15, "bold"),
                        fg="black", bg="dark orange")
        F4.place(x=410, y=140, width=210, height=393)

        c1_label = Label(F4, text="Fanta", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=0,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        c1_txt = Entry(F4, width=4, textvariable=self.fanta, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=1, pady=10, sticky=W)

        c2_label = Label(F4, text="Coca cola", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=4, textvariable=self.coca_cola, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=1, pady=10, sticky=W)

        c3_label = Label(F4, text="Soda", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=4, textvariable=self.soda, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=1, pady=10, sticky=W)

        c4_label = Label(F4, text="Old Darbar", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=3,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        c4_txt = Entry(F4, width=4, textvariable=self.old_darbar, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=1, pady=10, sticky=W)

        c5_label = Label(F4, text="Vodka", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        c5_txt = Entry(F4, width=4, textvariable=self.vodka, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=1, pady=10, sticky=W)

        c6_label = Label(F4, text="Big Master", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=5,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        c6_txt = Entry(F4, width=4, textvariable=self.big_master, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=1, pady=10, sticky=W)

        #  fruitsandvegetables frame
        F4 = LabelFrame(self.master, bd=5, relief=GROOVE, text="Fruits & Vegetables", font=("times new roman", 15, "bold"),
                        fg="black", bg="dark orange")
        F4.place(x=620, y=140, width=200, height=393)

        c1_label = Label(F4, text="Apple", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=4, textvariable=self.apple, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10, sticky=W)

        c2_label = Label(F4, text="Banana", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=4, textvariable=self.banana, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10, sticky=W)

        c3_label = Label(F4, text="Oranges", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=2,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        c3_txt = Entry(F4, width=4, textvariable=self.oranges, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10, sticky=W)

        c4_label = Label(F4, text="Onion", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=4, textvariable=self.onion, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10, sticky=W)

        c5_label = Label(F4, text="Tomato", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=4, textvariable=self.tomato, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10, sticky=W)

        c6_label = Label(F4, text="Spanich", font=("times new roman", 16, "bold"), fg="black", bg="dark orange").grid(row=5,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        c6_txt = Entry(F4, width=4, textvariable=self.spanich, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10, sticky=W)

        # Bakery and Dairy frame

        F5 = LabelFrame(self.master, bd=5, relief=GROOVE, text="Bakery & Dairy",
                        font=("times new roman", 15, "bold"),
                        fg="black", bg="dark orange")
        F5.place(x=810, y=140, width=210, height=393)


        b1_label = Label(F5, text="Bread", font=("times new roman", 16, "bold"), fg="black",
                               bg="dark orange").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        b1_txt = Entry(F5, width=4, textvariable=self.bread, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=1, pady=10, sticky=W)
        # crossiant
        b2_label = Label(F5, text="Crossiant", font=("times new roman", 16, "bold"), fg="black",
                           bg="dark orange").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        b2_txt = Entry(F5, width=4, textvariable=self.crossiant, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=1, column=1, padx=1, pady=10, sticky=W)

        # doughnut
        b3_label = Label(F5, text="Doughnut", font=("times new roman", 16, "bold"), fg="black",
                              bg="dark orange").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        b3_txt = Entry(F5, width=4, textvariable=self.doughnut, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=2, column=1, padx=1, pady=10, sticky=W)

        # butter
        b4_label = Label(F5, text="Butter", font=("times new roman", 16, "bold"), fg="black",
                                     bg="dark orange").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        b4_txt = Entry(F5, width=4, textvariable=self.butter, font=("times new roman", 16, "bold"),
                                   bd=5,
                                   relief=SUNKEN).grid(row=3, column=1, padx=1, pady=10, sticky=W)

        # paneer
        b5_label = Label(F5, text="Paneer", font=("times new roman", 16, "bold"), fg="black",
                             bg="dark orange").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        b5_txt = Entry(F5, width=4, textvariable=self.paneer, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4, column=1, padx=1, pady=10, sticky=W)

        # ddc_milk
        b6_label = Label(F5, text="DDC_Milk", font=("times new roman", 16, "bold"), fg="black",
                           bg="dark orange").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        b6_txt = Entry(F5, width=4, textvariable=self.ddc_milk, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=5, column=1, padx=1, pady=10, sticky=W)

        # bill Area ....................................

        F6 = LabelFrame(self.master, bd=5, relief=GROOVE)
        F6.place(x=1005, y=140, width=350, height=393)
        bill_title = Label(F6, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        scrol_y = Scrollbar(F6, orient=VERTICAL)
        self.txtarea = Text(F6, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #  bottom button frame----------------------------------

        F7 = LabelFrame(self.master, bd=8, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="black", bg="dark orange")
        F7.place(x=0, y=500, relwidth=1, height=200)

        m1 = Label(F7, text="Total Snacks Price", bg="dark orange", fg="black",
                   font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky=W)
        ml_txt = Entry(F7, width=18, textvariable=self.snacks_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=1, pady=1)

        m2 = Label(F7, text="Total Riceandgrains Price", bg="dark orange", fg="black",
                   font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky=W)
        m2_txt = Entry(F7, width=18, textvariable=self.riceandgrains_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=1, pady=1)

        m3 = Label(F7, text="Total Beverages Price", bg="dark orange", fg="black",
                   font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky=W)
        m3_txt = Entry(F7, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=1, pady=1)

        m4 = Label(F7, text="Total Fruitsandvegetables Price", bg="dark orange", fg="black",
                   font=("times new roman", 14, "bold")).grid(row=3, column=0, padx=20, pady=1, sticky=W)
        m4_txt = Entry(F7, width=18, textvariable=self.fruitsandvegetables_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=3, column=1, padx=1, pady=1)

        m5 = Label(F7, text="Total BakeryandDairy Price", bg="dark orange", fg="black",
                   font=("times new roman", 14, "bold")).grid(row=4, column=0, padx=20, pady=1, sticky=W)
        m5_txt = Entry(F7, width=18, textvariable=self.backeryanddairy_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(
            row=4, column=1, padx=1, pady=1)

        # for tax

        tax1 = Label(F7, text="Snacks Tax (28%)", bg="dark orange", fg="black",
                     font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky=W)
        taxl_txt = Entry(F7, width=18, textvariable=self.snacks_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=1)

        tax2 = Label(F7, text="Riceandgrains Tax (5%)", bg="dark orange", fg="black", font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=20, pady=1, sticky=W)
        tax2_txt = Entry(F7, width=18, textvariable=self.riceandgrains_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=1)

        tax3 = Label(F7, text="Beverages Tax (40%)", bg="dark orange", fg="black",
                     font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky=W)
        tax3_txt = Entry(F7, width=18, textvariable=self.beverages_tax, font="arial 10 bold", bd=7,
                         relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        tax4 = Label(F7, text="fruitsandvegetables Tax (5%)", bg="dark orange", fg="black", font=("times new roman", 14, "bold")).grid(
            row=3, column=2, padx=20, pady=1, sticky=W)
        tax4_txt = Entry(F7, width=18, textvariable=self.fruitsandvegetables_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=3, column=3, padx=10, pady=1)

        tax5 = Label(F7, text="Bakery&dairy Tax (1%)", bg="dark orange", fg="black",
                    font=("times new roman", 14, "bold")).grid(
            row=4, column=2, padx=20, pady=1, sticky=W)
        tax5_txt = Entry(F7, width=18, textvariable=self.backeryanddairy_tax, font="arial 10 bold", bd=7,
                         relief=SUNKEN).grid(
            row=4, column=3, padx=10, pady=1)

        #Button_Frame

        self.total_btn_img = PhotoImage(file="C:\\store\\totalbtn.png")
        self.total_button = Button(self.master, image=self.total_btn_img, bg='orange', fg="black",
                                     activebackground="#73C2FB",
                                     activeforeground="indigo", cursor="hand2", font=("Comic Sans MS", 14, "bold"),
                                     height=37, width=145, bd=0, command=self.total, relief=FLAT, overrelief=RIDGE)
        self.total_button.image = self.total_btn_img
        self.total_button.place(x=950, y=530)

        self.genbill_btn_img = PhotoImage(file="C:\\store\\generatebill.png")
        self.genbill_button = Button(self.master, image=self.genbill_btn_img, bg='orange', fg="black",
                                   activebackground="#73C2FB",
                                   activeforeground="indigo", cursor="hand2", font=("Comic Sans MS", 14, "bold"),
                                   height=37, width=145, bd=0, command=self.bill_area, relief=FLAT, overrelief=RIDGE)
        self.genbill_button.image = self.genbill_btn_img
        self.genbill_button.place(x=1150, y=530)

        self.clear_btn_img = PhotoImage(file="C:\\store\\clearbtn.png")
        self.clear_button = Button(self.master, image=self.clear_btn_img, bg='orange', fg="black",
                                     activebackground="#73C2FB",
                                     activeforeground="indigo", cursor="hand2", font=("Comic Sans MS", 14, "bold"),
                                     height=37, width=145, bd=0, command=self.clear_data, relief=FLAT, overrelief=RIDGE)
        self.clear_button.image = self.clear_btn_img
        self.clear_button.place(x=950, y=610)

        self.exit_btn_img = PhotoImage(file="C:\\store\\exitbtn.png")
        self.exit_button = Button(self.master, image=self.exit_btn_img, bg='orange', fg="black",
                                   activebackground="#73C2FB",
                                   activeforeground="indigo", cursor="hand2", font=("Comic Sans MS", 14, "bold"),
                                   height=37, width=145, bd=0, command=self.exit_app, relief=FLAT, overrelief=RIDGE)
        self.exit_button.image = self.clear_btn_img
        self.exit_button.place(x=1150, y=610)


        self.welcome_bill()


    def total(self):
        self.s_pr = self.pringles.get() * 268
        self.s_la = self.lays.get() * 45  # *self.find_price("pringles",self.pringles_clicked.get())
        self.s_ku = self.kurkure.get() * 150  # *self.find_price("lays",self.laus_clicked.get())
        self.s_pob = self.potato_biscuit.get() * 150  # *self.find_price("potato",self.potatobiscuit_clicked.get())
        self.s_mob = self.monaco.get() * 80  # *self.find_price("monaco",self.monacobiscuit_clicked.get())
        self.s_or = self.oreo.get() * 25  # *self.find_price("oreo",self.oreo_clicked.get())
        self.total_snacks_price = float(
            self.s_pr +
            self.s_la +
            self.s_ku +
            self.s_pob +
            self.s_mob +
            self.s_or
        )

        self.s_tax = round((self.total_snacks_price * 0.28), 2)
        self.snacks_price.set("Rs. " + str(self.total_snacks_price))
        self.snacks_tax.set("Rs. " + str(self.s_tax))

        self.r_mg = self.chickpeas.get() * 108
        self.r_rc = self.rajma.get() * 216
        self.r_wh = self.maize.get() * 88
        self.r_sg = self.peas.get() * 183
        self.r_fol = self.rice.get() * 1800
        self.r_dl = self.daal.get() * 131

        self.total_riceandgrains_price = float(
            self.r_dl +
            self.r_fol +
            self.r_mg +
            self.r_rc +
            self.r_sg +
            self.r_wh
        )
        self.r_tax = round((self.total_riceandgrains_price * 0.05), 2)
        self.riceandgrains_price.set("Rs. " + str(self.total_riceandgrains_price))
        self.riceandgrains_tax.set("Rs. " + str(self.r_tax))

        self.cd_mz = self.fanta.get() * 100
        self.cd_cc = self.coca_cola.get() * 225
        self.cd_sl = self.soda.get() * 50
        self.ccd_thu = self.old_darbar.get() * 2900
        self.cd_ft = self.vodka.get() * 820
        self.cd_ps = self.big_master.get() * 750

        self.total_beverages_price = float(
            self.cd_cc +
            self.cd_ft +
            self.cd_mz +
            self.cd_ps +
            self.cd_sl +
            self.ccd_thu
        )
        self.cd_tax = round((self.total_beverages_price * 0.40), 2)
        self.cold_drink_price.set("Rs. " + str(self.total_beverages_price))
        self.beverages_tax.set("Rs. " + str(self.cd_tax))

        self.fv_a = self.apple.get() * 234
        self.fv_b = self.banana.get() * 130
        self.fv_o = self.oranges.get() * 250
        self.fv_on = self.onion.get() * 80
        self.fv_t = self.tomato.get() * 50
        self.fv_s = self.spanich.get() * 60

        self.total_fruitsandvegetables_price = float(
            self.fv_a +
            self.fv_b +
            self.fv_o +
            self.fv_on +
            self.fv_t +
            self.fv_s
        )
        self.fv_tax = round((self.total_fruitsandvegetables_price * 0.05), 2)
        self.fruitsandvegetables_price.set("Rs. " + str(self.total_fruitsandvegetables_price))
        self.fruitsandvegetables_tax.set("Rs. " + str(self.fv_tax))

        self.b_b = self.bread.get() * 60
        self.b_c = self.crossiant.get() * 20
        self.b_d = self.doughnut.get() * 30
        self.b_bu = self.butter.get() * 130
        self.b_p = self.paneer.get() * 200
        self.b_m = self.ddc_milk.get() * 76

        self.total_BakeryandDairy_price = float(
            self.b_b +
            self.b_c +
            self.b_d +
            self.b_bu +
            self.b_p +
            self.b_m
        )
        self.b_tax = round((self.total_BakeryandDairy_price * 0.56), 2)
        self.backeryanddairy_price.set("Rs. " + str(self.total_BakeryandDairy_price))
        self.backeryanddairy_tax.set("Rs. " + str(self.b_tax))

        self.total_bill = float(
            self.total_snacks_price +
            self.total_riceandgrains_price +
            self.total_beverages_price +
            self.total_fruitsandvegetables_price +
            self.total_BakeryandDairy_price +
            self.s_tax +
            self.r_tax +
            self.cd_tax +
            self.b_tax +
            self.fv_tax
        )

    def stock_update_after_purchased(self, name, n):
        f1 = open("stock.csv", "w+", encoding='utf-8-sig')
        for i in f1:
            data = i.split(",")
            if data[0] == name:
                if n <= int(data[1]):
                    x = int(data[1])
                    x = x - n
                    return n

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\t|| ADMIRAL SHOP ||")
        self.txtarea.insert(END, "\n_________________________________________\n")
        self.txtarea.insert(END, f"\nBill No. : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name :   {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone no.:    {self.c_phon.get()}")
        self.txtarea.insert(END, "\n==========================================")
        self.txtarea.insert(END, "\nProducts\t\t\tQTY\t   Price")
        self.txtarea.insert(END, "\n==========================================")

    def bill_area(self):

        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Fill Customer details")
        elif self.snacks_price == "Rs. 0.0" and self.riceandgrains_price == "Rs. 0.0" and self.cold_drink_price == "Rs. 0.0" and self.biscuit_price == "Rs. 0.0":
            messagebox.showerror("Error", "No product purchased")
        else:
            self.welcome_bill()
            # snacks & crackers
            if self.pringles.get() != 0:
                self.txtarea.insert(END, f"\npringles    \t\t\t{self.pringles.get()}\t    {self.s_pr}")
            if self.lays.get() != 0:
                self.txtarea.insert(END, f"\nlays \t\t\t{self.lays.get()}\t    {self.s_la}")
            if self.kurkure.get() != 0:
                self.txtarea.insert(END, f"\nkurkure\t\t\t{self.kurkure.get()}\t    {self.s_ku}")
            if self.potato_biscuit.get() != 0:
                self.txtarea.insert(END, f"\npotatobiscuit\t\t\t{self.potato_biscuit.get()}\t    {self.s_pob}")
            if self.monaco.get() != 0:
                self.txtarea.insert(END, f"\nmonaco \t\t\t{self.monaco.get()}\t    {self.s_mob}")
            if self.oreo.get() != 0:
                self.txtarea.insert(END, f"\noreo\t\t\t{self.oreo.get()}\t    {self.s_or}")

            # BakeryandDairy
            if self.bread.get() != 0:
                self.txtarea.insert(END, f"\nbread    \t\t\t{self.bread.get()}\t    {self.b_b}")
            if self.crossiant.get() != 0:
                self.txtarea.insert(END, f"\ncrossiant \t\t\t{self.crossiant.get()}\t    {self.b_c}")
            if self.doughnut.get() != 0:
                self.txtarea.insert(END, f"\ndoughnut \t\t\t{self.doughnut.get()}\t    {self.b_d}")
            if self.butter.get() != 0:
                self.txtarea.insert(END, f"\nbutter \t\t\t{self.butter.get()}\t    {self.b_bu}")
            if self.paneer.get() != 0:
                 self.txtarea.insert(END, f"\npaneer \t\t\t{self.paneer.get()}\t    {self.b_p}")
            if self.ddc_milk.get() != 0:
                self.txtarea.insert(END, f"\nddc_milk \t\t\t{self.ddc_milk.get()}\t    {self.b_m}")


            # rice and grains print
            if self.chickpeas.get() != 0:
                self.txtarea.insert(END, f"\nchickpeas   \t\t\t{self.chickpeas.get()}\t    {self.r_mg}")
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\nRice     \t\t\t{self.rice.get()}\t    {self.r_rc}")
            if self.rajma.get() != 0:
                self.txtarea.insert(END, f"\nrajma   \t\t\t{self.rajma.get()}\t    {self.r_wh}")
            if self.maize.get() != 0:
                self.txtarea.insert(END, f"\nmaize \t\t\t{self.maize.get()}\t    {self.r_fol}")
            if self.peas.get() != 0:
                self.txtarea.insert(END, f"\npeas    \t\t\t{self.peas.get()}\t    {self.r_sg}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\nDaal     \t\t\t{self.daal.get()}\t    {self.r_dl}")

            # fruits and vegetables print
            if self.apple.get() != 0:
                self.txtarea.insert(END, f"\napple  \t\t\t{self.apple.get()}\t    {self.fv_a}")
            if self.banana.get() != 0:
                self.txtarea.insert(END, f"\nbanana    \t\t\t{self.banana.get()}\t    {self.fv_b}")
            if self.oranges.get() != 0:
                self.txtarea.insert(END, f"\noranges \t\t\t{self.oranges.get()}\t    {self.fv_o}")
            if self.onion.get() != 0:
                self.txtarea.insert(END, f"\nonion \t\t\t{self.onion.get()}\t    {self.fv_on}")
            if self.tomato.get() != 0:
                self.txtarea.insert(END, f"\ntomato  \t\t\t{self.tomato.get()}\t    {self.fv_t}")
            if self.spanich.get() != 0:
                self.txtarea.insert(END, f"\nspanich   \t\t\t{self.spanich.get()}\t    {self.fv_s}")

            # Cold-drink print
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\nfanta     \t\t\t{self.fanta.get()}\t    {self.cd_mz}")
            if self.coca_cola.get() != 0:
                self.txtarea.insert(END, f"\nCoca-Cola\t\t\t{self.coca_cola.get()}\t    {self.cd_cc}")
            if self.soda.get() != 0:
                self.txtarea.insert(END, f"\nSoda   \t\t\t{self.soda.get()}\t    {self.cd_sl}")
            if self.old_darbar.get() != 0:
                self.txtarea.insert(END, f"\nold-darbar \t\t\t{self.old_darbar.get()}\t    {self.ccd_thu}")
            if self.vodka.get() != 0:
                self.txtarea.insert(END, f"\nVodka    \t\t\t{self.vodka.get()}\t    {self.cd_ps}")
            if self.big_master.get() != 0:
                self.txtarea.insert(END, f"\nbig-master   \t\t\t{self.big_master.get()}\t    {self.cd_ft}")

            self.txtarea.insert(END, "\n`````````````````````````````````````````")
            if self.snacks_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nsnacks Tax\t\t\t       {self.snacks_tax.get()}")
            if self.riceandgrains_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nriceandgrains  Tax\t\t\t       {self.riceandgrains_tax.get()}")
            if self.fruitsandvegetables_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nfruitsandvegetables  Tax\t\t\t       {self.fruitsandvegetables_tax.get()}")
            if self.beverages_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nbeverages Tax\t\t\t      {self.beverages_tax.get()}")
            if self.backeryanddairy_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nbackeryanddairy  Tax\t\t\t       {self.backeryanddairy_tax.get()}")


            self.txtarea.insert(END, "\n`````````````````````````````````````````")
            self.txtarea.insert(END, f"\nTotal Bill :\t\t\t      Rs. {str(self.total_bill)}")
            self.txtarea.insert(END, "\n`````````````````````````````````````````")

            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("save bill", "Do you want to save the bill ?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            fp1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            fp1.write(self.bill_data)
            fp1.close()
            messagebox.showinfo("Saved", f"Bill No. :{self.bill_no.get()} Saved successfuly")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                self.txtarea.insert(END, f1.read())
                f1.close()
                present = "yes"

        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear_data(self):
        #   snacks & crackers variable
        op = messagebox.askyesno("Clear", "Do you want to Clear")
        if op > 0:
            self.pringles.set(0)
            self.lays.set(0)
            self.kurkure.set(0)
            self.potato_biscuit.set(0)
            self.monaco.set(0)
            self.oreo.set(0)

            # riceandgrains varible
            self.chickpeas.set(0)
            self.rice.set(0)
            self.maize.set(0)
            self.rajma.set(0)
            self.daal.set(0)
            self.peas.set(0)

            # cold drink
            self.fanta.set(0)
            self.coca_cola.set(0)
            self.soda.set(0)
            self.old_darbar.set(0)
            self.vodka.set(0)
            self.big_master.set(0)

            # fruits and vegetables varible

            self.apple.set(0)
            self.banana.set(0)
            self.oranges.set(0)
            self.onion.set(0)
            self.tomato.set(0)
            self.spanich.set(0)

            # bakery & dairy varible
            self.bread.set(0)
            self.crossiant.set(0)
            self.doughnut.set(0)
            self.butter.set(0)
            self.paneer.set(0)
            self.ddc_milk.set(0)

            # product price varible

            self.snacks_price.set("")
            self.riceandgrains_price.set("")
            self.cold_drink_price.set("")
            self.fruitsandvegetables_price.set("")
            self.backeryanddairy_price.set("")


            # tax varible

            self.snacks_tax.set("")
            self.riceandgrains_tax.set("")
            self.beverages_tax.set("")
            self.fruitsandvegetables_tax.set("")
            self.backeryanddairy_tax.set("")


            # snacks & crackers details

            self.c_name.set("")
            self.c_phon.set("")
            self.c_mail.set("")
            self.bill_no.set("")
            self.search_bill.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.welcome_bill()

        else:
            return

    def exit_app(self):
        op1 = messagebox.askyesno("Exit", "Do you want to Exit")
        if op1 > 0:
            self.master.destroy()
        else:
            return

    def check_mail(self):
        txt_msg = self.bill_app()
        messagebox.showinfo("Sent", f"Bill No. :{self.bill_no.get()} Sent successfuly")




        # Notepad Area ....................................

        F4 = LabelFrame(self.bill_app, bd=10, relief=GROOVE)
        F4.place(x=780, y=133, width=757, height=600)
        bill_title = Label(F4, text="Notepad Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        scrol_y = Scrollbar(F4, orient=VERTICAL)
        self.txtarea = Text(F4, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        self.welcome_bill_admin()


    def welcome_bill_admin(self):

        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\t\t\t\t|| grocery SHOP ||")
        self.txtarea.insert(END,
                            "\n_________________________________________________________________________________________\n")

    def check_stock(self):

        self.txtarea.delete('1.0', END)

        self.welcome_bill_admin()

        f1 = open("stock.csv", "r", encoding='utf-8-sig')

        # self.txtarea.insert(END,f1.read())
        self.txtarea.insert(END, "|| Product    || \t\t\t\t\t\t\t\t ||Quantity")
        self.txtarea.insert(END,
                            "\n_________________________________________________________________________________________\n")
        for i in f1:
            data = i.split(",")
            #    print((data[0],data[1]))

            self.txtarea.insert(END, "\n" + data[0] + "\t\t\t\t\t\t\t\t " + data[1])

        f1.close()

    def clear_admin_notebook(self):
        self.txtarea.delete('1.0', END)
        self.welcome_bill_admin()

    def bill_list(self):

        j = 1
        self.txtarea.insert(END, "S.No.\t Bill \n\n")
        for i in os.listdir("bills/"):
            self.txtarea.insert(END, str(j) + ".\t" + str(i) + "\n\n")
            j += 1

    def Update_stock(self):
        # os.startfile('stock.csv','r')
        p = Popen('stock.csv', shell=True)


