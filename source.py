#book app
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

#buy books
def buy():
    g=""
    b=Tk()

    b.title("buy page")
    b.geometry("1000x800")
    b.resizable(0,0)

    c1=Canvas(b, bg="white", width=1000, height=800)
    c1.pack()
    c2=Canvas(b, bg="#00adb8", width=1000, height=200)
    c2.place(x=-1, y=-1)
    c3=Canvas(b, bg="#00adb8", width=1000, height=100)
    c3.place(x=-1, y=760)

    l3=Label(master=b, text="BUY BOOKS", font=("helvetica", 15, "bold"), bg="#00adb8").place(x=450, y=80)

    l1=Label(master=b, text="Buy secondhand books for afforable price", font=("helvetica", 13), bg="#00adb8").place(x=350, y=120)
    h=StringVar()
    l2=Label(master=b, text="1. Enter title or author/publisher:", font=("helvetica", 13), bg="white").place(x=50, y=300)
    e1=Entry(master=b, font=("helvetica", 13), bd=2, textvariable=h, width=38)
    e1.place(x=300, y=300) 
    e2=Text(master=b, font=("helvetica", 13), width=66, height=10)
    e2.place(x=50, y=410)

    def sub():
        global g
        x=e1.get()
        e2.delete('1.0', END)
        r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
        y=r.cursor()
        y.execute(f'SELECT title, authpub, buyp FROM book WHERE title="{x}" AND category="edu" OR authpub="{x}" AND category="edu"')
        g=y.fetchall()
        r.commit()
        if len(g)>0:
           e2.insert(INSERT,f"Title: {g[0][0]} {chr(10)}Author: {g[0][1]} {chr(10)}Price: ₹{g[0][2]} {chr(10)}{chr(10)}To continue, click 'Submit'")
        else:
            e2.insert(INSERT,"Sorry, the title or author you have entered does not match with any of our records. Please try again")

    def fic():
        global g
        x=e1.get()
        e2.delete('1.0', END)
        r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
        y=r.cursor()
        y.execute(f'SELECT title, authpub, buyp FROM book WHERE title="{x}" And category="fic" OR authpub="{x}" AND category="fic"')
        g=y.fetchall()
        r.commit()
        if len(g)>0:
            e2.insert(INSERT,f"Title: {g[0][0]} {chr(10)}Author: {g[0][1]} {chr(10)}Price: ₹{g[0][2]} {chr(10)}{chr(10)}To continue, click 'Submit'")
        else:
            e2.insert(INSERT,"Sorry, the title or author you have entered does not match with any of our records. Please try again")

    def nfic():
        global g
        x=e1.get()
        e2.delete('1.0', END)
        r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
        y=r.cursor()
        y.execute(f'SELECT title, authpub, buyp FROM book WHERE title="{x}" AND category="nfic" OR authpub="{x}" AND category="nfic"')
        g=y.fetchall()
        r.commit()
        if len(g)>0:
           e2.insert(INSERT,f"Title: {g[0][0]} {chr(10)}Author: {g[0][1]} {chr(10)}Price: ₹{g[0][2]} {chr(10)}{chr(10)}To continue, click 'Submit'")
        else:
            e2.insert(INSERT,"Sorry, the title or author you have entered does not match with any of our records. Please try again")

    l1=Label(master=b, text="2. Select category:", font=("helvetica", 13), bg="white").place(x=50, y=355)
    b1=Button(master=b, width=15, text="Educational", bg="#00adb8", font=("Helvetica", 13), command=lambda:sub()).place(x=200, y=350)
    b2=Button(master=b, width=15, text="Fiction", bg="#00adb8", font=("Helvetica", 13), command=lambda:fic()).place(x=350, y=350)
    b3=Button(master=b, width=15, text="Non-Fiction", bg="#00adb8", font=("Helvetica", 13), command=lambda:nfic()).place(x=500, y=350)

    def check():
        f=e2.get(1.0, "end-1c")
        if(len(f)==0 or f=="Sorry, the title or author you have entered does not match with any of our records. Please try again"):
            e2.delete(1.0, END)
            e2.insert(INSERT,"Please search for a book first.")
        else:
            fin()

    def fin():
        o=Tk()
        o.title("Details page")
        o.geometry("550x500")
        o.resizable(0,0)
        oc1=Canvas(o, bg="white", width=550, height=500).pack()
        oc2=Canvas(o, bg="#00adb8", width=550, height=100).place(x=-1,y=-1)
        ol4=Label(master=o, text="DETAILS", bg="#00adb8", font=("Helvetica", 15, "bold")).place(x=230, y=30)
        o1=StringVar()
        ol1=Label(master=o, text="1. Enter your name:", bg="white", font=("Helvetica", 13)).place(x=50, y=130)
        oe1=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o1)
        oe1.place(x=210, y=130)
        o2=StringVar()
        ol2=Label(master=o, text="2. Enter your address:", bg="white", font=("Helvetica", 13)).place(x=50, y=180)
        oe2=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o2)
        oe2.place(x=230, y=180)
        o3=StringVar()
        ol3=Label(master=o, text="3. Enter your phone number:", bg="white", font=("Helvetica", 13)).place(x=50, y=230)
        oe3=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o3)
        oe3.place(x=280, y=230)
        oc3=Canvas(o, bg="#00adb8", width=550, height=50).place(x=-1,y=470)

        def done():
            global g
            x=oe1.get()
            y=oe2.get()
            z=oe3.get()
            try:
                r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
                t=r.cursor()
                t.execute(f'INSERT INTO info VALUES("{x}", "{y}", "{z}", "{g}", "b")')
                r.commit()
            except:
                obl1=Label(master=o, text="Oops! Something went wrong. \nPlease check your details \nand try again.", bg="white", font=("helvetica", 13)).place(x=150, y=370)
            else:
                obl1=Label(master=o, text="   Thank you for using our app!\n\n\n", bg="white", font=("Helvetica", 13)).place(x=150, y=370)
            
        
        ob1=Button(master=o, width=15, text="Submit", bg="#00adb8", font=("helvetica", 13), command=lambda:done()).place(x=200, y=300)
    
        o.mainloop()

    b5=Button(master=b, width=15, text="Submit", bg="#00adb8", font=("helvetica", 12), command=lambda:check()).place(x=780, y=650)

    b.mainloop()

#rent books
def rent():
    g=""
    b=Tk()

    b.title("rent page")
    b.geometry("1000x800")
    b.resizable(0,0)

    c1=Canvas(b, bg="white", width=1000, height=800)
    c1.pack()
    c2=Canvas(b, bg="#87c44b", width=1000, height=200)
    c2.place(x=0, y=0)
    c3=Canvas(b, bg="#87c44b", width=1000, height=100)
    c3.place(x=0, y=760)

    l3=Label(master=b, text="RENT BOOKS", font=("helvetica", 15, "bold"), bg="#87c44b").place(x=450, y=80)
    l1=Label(master=b, text="Rent secondhand books for afforable price", font=("helvetica", 13), bg="#87c44b").place(x=360, y=120)

    h=StringVar()
    l2=Label(master=b, text="1. Enter title or author/publisher:", font=("helvetica", 13), bg="white").place(x=50, y=300)
    e1=Entry(master=b, font=("helvetica", 13), bd=2, textvariable=h, width=38)
    e1.place(x=300, y=300) 
    e2=Text(master=b, font=("helvetica", 13), width=66, height=10)
    e2.place(x=50, y=410)

    def sub():
        global g
        x=e1.get()
        e2.delete('1.0', END)
        r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
        y=r.cursor()
        y.execute(f'SELECT title, authpub, rentp FROM book WHERE title="{x}" AND category="edu" OR authpub="{x}" AND category="edu"')
        g=y.fetchall()
        r.commit()
        if len(g)>0:
           e2.insert(INSERT,f"Title: {g[0][0]} {chr(10)}Author: {g[0][1]} {chr(10)}Price: ₹{g[0][2]} {chr(10)}{chr(10)}To continue, click 'Submit'")
        else:
            e2.insert(INSERT,"Sorry, the title or author you have entered does not match with any of our records. Please try again")

    def fic():
        global g
        x=e1.get()
        e2.delete('1.0', END)
        r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
        y=r.cursor()
        y.execute(f'SELECT title, authpub, rentp FROM book WHERE title="{x}" AND category="fic" OR authpub="{x}" AND category="fic"')
        g=y.fetchall()
        r.commit()
        if len(g)>0:
            e2.insert(INSERT,f"Title: {g[0][0]} {chr(10)}Author: {g[0][1]} {chr(10)}Price: ₹{g[0][2]} {chr(10)}{chr(10)}To continue, click 'Submit'") 
        else:
            e2.insert(INSERT,"Sorry, the title or author you have entered does not match with any of our records. Please try again")

    def nfic():
        global g
        x=e1.get()
        e2.delete('1.0', END)
        r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
        y=r.cursor()
        y.execute(f'SELECT title, authpub, rentp FROM book WHERE title="{x}" AND category="nfic" OR authpub="{x}" AND category="nfic"')
        g=y.fetchall()
        r.commit()
        if len(g)>0:
           e2.insert(INSERT,f"Title: {g[0][0]} {chr(10)}Author: {g[0][1]} {chr(10)}Price: ₹{g[0][2]} {chr(10)}{chr(10)}To continue, click 'Submit'")
        else:
            e2.insert(INSERT,"Sorry, the title or author you have entered does not match with any of our records. Please try again")

    l1=Label(master=b, text="2. Select category:", font=("helvetica", 13), bg="white").place(x=50, y=355)
    b1=Button(master=b, width=15, text="Educational", bg="#87c44b", font=("Helvetica", 13), command=lambda:sub()).place(x=200, y=350)
    b2=Button(master=b, width=15, text="Fiction", bg="#87c44b", font=("Helvetica", 13), command=lambda:fic()).place(x=350, y=350)
    b3=Button(master=b, width=15, text="Non-Fiction", bg="#87c44b", font=("Helvetica", 13), command=lambda:nfic()).place(x=500, y=350)

    def check():
        f=e2.get(1.0, "end-1c")
        if(len(f)==0 or f=="Sorry, the title or author you have entered does not match with any of our records. Please try again"):
            e2.delete(1.0, END)
            e2.insert(INSERT,"Please search for a book first.")
        else:
            fin()

    def fin():
        o=Tk()
        o.title("Details page")
        o.geometry("550x500")
        o.resizable(0,0)
        oc1=Canvas(o, bg="white", width=550, height=500).pack()
        oc2=Canvas(o, bg="#87c44b", width=550, height=100).place(x=-1,y=-1)
        ol4=Label(master=o, text="DETAILS", bg="#87c44b", font=("Helvetica", 15, "bold")).place(x=230, y=30)
        o1=StringVar()
        ol1=Label(master=o, text="1. Enter your name:", bg="white", font=("Helvetica", 13)).place(x=50, y=130)
        oe1=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o1)
        oe1.place(x=210, y=130)
        o2=StringVar()
        ol2=Label(master=o, text="2. Enter your address:", bg="white", font=("Helvetica", 13)).place(x=50, y=180)
        oe2=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o2)
        oe2.place(x=230, y=180)
        o3=StringVar()
        ol3=Label(master=o, text="3. Enter your phone number:", bg="white", font=("Helvetica", 13)).place(x=50, y=230)
        oe3=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o3)
        oe3.place(x=280, y=230)
        oc3=Canvas(o, bg="#87c44b", width=550, height=50).place(x=-1, y=470)

        def done():
            global g
            x=oe1.get()
            y=oe2.get()
            z=oe3.get()
            try:
                r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
                t=r.cursor()
                t.execute(f'INSERT INTO info VALUES("{x}", "{y}", {z}, "{g}", "r")')
                r.commit()
            except:
                obl1=Label(master=o, text="Oops! Something went wrong. \nPlease check your details \nand try again.", bg="white", font=("helvetica", 13)).place(x=150, y=370)
            else:
                obl1=Label(master=o, text="   Thank you for using our app!\n\n\n", bg="white", font=("helvetica", 13)).place(x=150, y=370)
        
        ob1=Button(master=o, width=15, text="Submit", bg="#87c44b", font=("helvetica", 13), command=lambda:done()).place(x=200, y=300)
    
        o.mainloop()

    b5=Button(master=b, width=15, text="Submit", bg="#87c44b", font=("helvetica", 13), command=lambda:check()).place(x=780, y=650)
    l10=Label(master=b, font=("helvetica", 13), bg="white", text="*Rent prices are on a monthly basis.").place(x=50, y=600)

    b.mainloop()

#sell books
def sell():

    p=0.0
    b=Tk()

    b.title("sell page")
    b.geometry("1000x800")
    b.resizable(0,0)

    c=Canvas(b, bg="white", width=1000, height=800)
    c.pack()
    c2=Canvas(b, bg="#ffb133", width=1000, height=200)
    c2.place(x=-1, y=-1)
    c3=Canvas(b, bg="#ffb133", width=1000, height=100)
    c3.place(x=-1, y=760)

    l3=Label(master=b, text="SELL BOOKS", font=("helvetica", 15, "bold"), bg="#ffb133").place(x=450, y=80)
    l3=Label(master=b, text="Sell your secondhand books here", font=("helvetica", 13), bg="#ffb133").place(x=390, y=120)
    h1=StringVar()
    l2=Label(master=b, text="1. Enter title:", font=("helvetica", 13), bg="white").place(x=50, y=300)
    e1=Entry(master=b, font=("helvetica", 13), bd=2, textvariable=h1)
    e1.place(x=160, y=300)

    h2=StringVar()
    l3=Label(master=b, text="2. Enter author/publisher:", font=("helvetica", 13), bg="white").place(x=50, y=350)
    e2=Entry(master=b, font=("helvetica",13), bd=2, textvariable=h2)
    e2.place(x=260, y=350)

    h2=StringVar()
    l5=Label(master=b, text="3. Enter edition:", font=("helvetica", 13), bg="white").place(x=50, y=400)
    e5=Entry(master=b, font=("helvetica",13), bd=2, textvariable=h2)
    e5.place(x=200, y=400)

    h3=StringVar()
    l4=Label(master=b, text="4. Enter price:", font=("helvetica", 13), bg="white").place(x=50, y=450)
    e3=Entry(master=b, font=("helvetica", 13), bd=2, textvariable=h3)
    e3.place(x=180, y=450)

    e4=Text(master=b, font=("helvetica", 13), width=50, height=10)
    e4.place(x=50, y=500)

    def check():
        global p
        p=float(e3.get())
        p=p/2
        e4.insert(INSERT, f"Offer price: ₹{p} \n\nTo continue, click 'Submit'.")

    b1=Button(master=b, width=15, text="Enter", bg="#ffb133", font=("helvetica", 13), command=lambda:check()).place(x=520, y=500)

    def che():
        f=e4.get(1.0, "end-1c")
        if(len(f)==0):
            e4.insert(INSERT,"Please enter the book details first.")
        else:
            fin()
        
    def fin():
        o=Tk()
        o.title("Details page")
        o.geometry("550x500")
        o.resizable(0,0)
        oc1=Canvas(o, bg="white", width=550, height=500).pack()
        oc2=Canvas(o, bg="#ffb133", width=550, height=100).place(x=-1,y=-1)
        ol4=Label(master=o, text="DETAILS", bg="#ffb133", font=("Helvetica", 15, "bold")).place(x=230, y=30)
        o1=StringVar()
        ol1=Label(master=o, text="1. Enter your name:", bg="white", font=("Helvetica", 13)).place(x=50, y=130)
        oe1=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o1)
        oe1.place(x=210, y=130)
        o2=StringVar()
        ol2=Label(master=o, text="2. Enter your address:", bg="white", font=("Helvetica", 13)).place(x=50, y=180)
        oe2=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o2)
        oe2.place(x=230, y=180)
        o3=StringVar()
        ol3=Label(master=o, text="3. Enter your phone number:", bg="white", font=("Helvetica", 13)).place(x=50, y=230)
        oe3=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o3)
        oe3.place(x=280, y=230)
        oc3=Canvas(o, bg="#ffb133", width=550, height=50).place(x=-1, y=470)

        def done():
            global p
            q=e1.get()
            k=e2.get()
            g=e5.get()
            k1=[(q, k, g, p)]
            x=oe1.get()
            y=oe2.get()
            z=oe3.get()
            try:
                r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
                t=r.cursor()
                t.execute(f'INSERT INTO info VALUES("{x}", "{y}", {z}, "{k1}", "s")')
                r.commit()
            except:
                obl1=Label(master=o, text="Oops! Something went wrong. \nPlease check your details \nand try again.", bg="white", font=("helvetica", 13)).place(x=150, y=370)
            else:
                obl1=Label(master=o, text="   Thank you for using our app!\n\n\n", bg="white", font=("helvetica", 13)).place(x=150, y=370)
        
        ob1=Button(master=o, width=15, text="Submit", bg="#ffb133", font=("helvetica", 13), command=lambda:done()).place(x=200, y=300)
    
        o.mainloop()

    b2=Button(master=b, width=15, text="Submit", bg="#ffb133", font=("helvetica", 13), command=lambda:che()).place(x=780, y=650)
    
    b.mainloop()
    
#school specials
def spec():

    p=0.0
    g=""
    b=Tk()

    b.title("school specials page")
    b.geometry("1000x800")
    b.resizable(0,0)

    c=Canvas(b, bg="white", width=1000, height=800)
    c.pack()
    c2=Canvas(b, bg="#ed8512", width=1010, height=200)
    c2.place(x=-11, y=-1)
    c3=Canvas(b, bg="#ed8512", width=1010, height=100)
    c3.place(x=-1, y=760)

    l1=Label(master=b, text="SCHOOL SPECIALS", font=("helvetica", 15, "bold"), bg="#ed8512").place(x=410, y=80)
    l4=Label(master=b, text="Special offer on rented books", font=("helvetica", 13), bg="#ed8512").place(x=400, y=120)
    l5=Label(master=b, bg="white", font=("helvetica", 13), text="Rent a pack of textbooks for the whole year, at a minimal price.\nPack includes all necessary textbooks, subject to class and board")
    l5.place(x=280, y=250)
    l2=Label(master=b, text="1. Select Class", font=("helvetica", 13), bg="white").place(x=50, y=320)

    e2=Text(master=b, font=("helvetica", 13), width=55, height=10)
    e2.place(x=50, y=460)

    frame = Frame(b)
    frame.place(x=50,y=350)

    l = Listbox(frame, width=28, height=4, font=("helvetica", 13),activestyle="none",selectbackground="#ed8512",selectforeground="black")
    l.insert(1,"Class I")
    l.insert(2,"Class II")
    l.insert(3,"Class III")
    l.insert(4,"Class IV")
    l.insert(5,"Class V")
    l.insert(6,"Class VI")
    l.insert(7,"Class VII")
    l.insert(8,"Class VIII")
    l.insert(9,"Class IX")
    l.insert(10,"Class X")
    l.pack(side="left", fill="y")

    scrollbar = Scrollbar(frame, orient="vertical")
    scrollbar.config(command=l.yview)
    scrollbar.pack(side="right", fill="y")

    l.config(yscrollcommand=scrollbar.set)

    def cbse():
        global g
        e2.delete('1.0', END)
        q=l.get(l.curselection())
        r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
        y=r.cursor()
        y.execute(f'SELECT class, board, price FROM specials WHERE class="{q}" AND board="CBSE"')
        g=y.fetchall()
        r.commit()
        if len(g)>0:
            e2.insert(INSERT,f"Class: {g[0][0]} {chr(10)}Board: {g[0][1]} {chr(10)}Price: ₹{g[0][2]} {chr(10)}{chr(10)}To continue, click 'Submit'")
        else:
            e2.insert(INSERT,"Sorry, this pack does not exist.")

    def ssc():
        global g
        e2.delete('1.0', END)
        q=l.get(l.curselection())
        r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
        y=r.cursor()
        y.execute(f'SELECT class, board, price FROM specials WHERE class="{q}" AND board="SSC"')
        g=y.fetchall()
        r.commit()
        if len(g)>0:
           e2.insert(INSERT,f"Class: {g[0][0]} {chr(10)}Board: {g[0][1]} {chr(10)}Price: ₹{g[0][2]} {chr(10)}{chr(10)}To continue, click 'Submit'")
        else:
            e2.insert(INSERT,"Sorry, this pack does not exist.")

    def check():
        f=e2.get(1.0, "end-1c")
        if(len(f)==0 or f=="Sorry, this pack does not exist"):
            e2.delete(1.0, END)
            e2.insert(INSERT,"Please search for a book first.")
        else:
            fin()

    def fin():
        o=Tk()
        o.title("Details page")
        o.geometry("550x500")
        o.resizable(0,0)
        oc1=Canvas(o, bg="white", width=550, height=500).pack()
        oc2=Canvas(o, bg="#ed8512", width=550, height=100).place(x=-1,y=-1)
        ol4=Label(master=o, text="DETAILS", bg="#ed8512", font=("Helvetica", 15, "bold")).place(x=230, y=30)
        o1=StringVar()
        ol1=Label(master=o, text="1. Enter your name:", bg="white", font=("Helvetica", 13)).place(x=50, y=130)
        oe1=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o1)
        oe1.place(x=210, y=130)
        o2=StringVar()
        ol2=Label(master=o, text="2. Enter your address:", bg="white", font=("Helvetica", 13)).place(x=50, y=180)
        oe2=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o2)
        oe2.place(x=230, y=180)
        o3=StringVar()
        ol3=Label(master=o, text="3. Enter your phone number:", bg="white", font=("Helvetica", 13)).place(x=50, y=230)
        oe3=Entry(master=o, font=("helvetica", 13), bd=2, textvariable=o3)
        oe3.place(x=280, y=230)
        oc3=Canvas(o, bg="#ed8512", width=550, height=50).place(x=-1,y=470)

        def done():
            global g
            x=oe1.get()
            y=oe2.get()
            z=oe3.get()
            try:
                r=mysql.connector.connect(host="localhost",user="root",password="nitya",database="bproj")
                t=r.cursor()
                t.execute(f'INSERT INTO info VALUES("{x}", "{y}", {z}, "{g}", "sp")')
                r.commit()
            except:
                obl1=Label(master=o, text="Oops! Something went wrong. \nPlease check your details \nand try again.", bg="white", font=("helvetica", 13)).place(x=150, y=370)
            else:
                obl1=Label(master=o, text="   Thank you for using our app!", bg="white", font=("Helvetica", 13)).place(x=150, y=370)
        
        ob1=Button(master=o, width=15, text="Submit", bg="#ed8512", font=("helvetica", 13), command=lambda:done()).place(x=200, y=300)
    
        o.mainloop()
    
    l3=Label(master=b, text="2. Select Board:", font=("helvetica", 13), bg="white").place(x=500, y=320)
    b1=Button(b,text="CBSE", width=15, bg="#ed8512", font=("helvetica", 13), command=lambda: cbse()).place(x=500, y=350)
    b2=Button(b,text="SSC", width=15, bg="#ed8512", font=("helvetica", 13), command=lambda: ssc()).place(x=500, y=400)


    b3=Button(b,text="Submit", width=15, bg="#ed8512", font=("helvetica", 13), command=lambda: check()).place(x=780, y=650)
    b.mainloop()
    

h=Tk()

h.title("homepage")
h.geometry("1000x800")
h.resizable(0,0)

c=Canvas(h, bg="white", width=1000, height=800)
c.pack()

i1=(Image.open("top.gif"))
img1=i1.resize((1000, 200), Image.ANTIALIAS)
im1=ImageTk.PhotoImage(img1)
li1=Label(image=im1).place(x=-1,y=-1) 


i2=(Image.open("logo2.gif"))
img2=i2.resize((200, 200), Image.ANTIALIAS)
im2=ImageTk.PhotoImage(img2)
li2=Label(image=im2, bd=0).place(x=400,y=210) 

l1=Label(h, text="ENGRAFO", font=("garamond", 16, "bold"), bg="white").place(x=442, y=400)

b1=Button(h,text="Buy Books", width=20, bg="#00adb8", font=("helvetica", 13), command=buy).place(x=120, y=460)
b2=Button(h,text="Rent Books", width=20, bg="#87c44b", font=("helvetica", 13), command=rent).place(x=310, y=460)
b3=Button(h,text="Sell Books", width=20, bg="#ffb133", font=("helvetica", 13), command=sell).place(x=490, y=460)
b4=Button(h,text="School Specials", width=20, bg="#ed8512", font=("helvetica", 13), command=spec).place(x=680, y=460)

l2=Label(h, font=("helvetica", 13), bg="white", text="ENGRAFO is a free application that allows its\nusers to borrow, sell and purchase pre-owned books.\n\nIt has been developed, keeping in mind the need to\nreduce student's expenditure and to promote\nthe idea of reusing resources.")
l2.place(x=310, y=570)

h.mainloop()
