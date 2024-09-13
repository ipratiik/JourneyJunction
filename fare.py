from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
my_pass = ""
my_database = "train"
con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
cur = con.cursor()

def price():
    dep = dep_info.get()
    des = dest_info.get()

    if (dep == "Bhopal" and des == "Jabalpur") or (des == "Bhopal" and dep == "Jabalpur"):
        lb4 = Label(heading_frame1, text="Economy Fare: 500 \n Business Class Fare: 800",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Bhopal" and des == "Gwalior") or (dep == "Gwalior" and des == "Bhopal"):
        lb4 = Label(heading_frame1, text="Economy Fare: 400 \n Business Class Fare: 700",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Bhopal" and des == "Indore") or (dep == "Indore" and des == "Bhopal"):
        lb4 = Label(heading_frame1, text="Economy Fare: 1500 \n Business Class Fare: 1800",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Bhopal" and des == "Delhi") or (dep == "Delhi" and des == "Bhopal"):
        lb4 = Label(heading_frame1, text="Economy Fare: 500 \n Business Class Fare: 1100",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Bhopal" and des == "Jaipur") or (dep == "Jaipur" and des == "Bhopal"):
        lb4 = Label(heading_frame1, text="Economy Fare: 500 \n Business Class Fare: 800",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Bhopal" and des == "Lucknow") or (dep == "Lucknow" and des == "Bhopal"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "700          1100",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Jabalpur" and des == "Gwalior") or (dep == "Gwalior" and des == "Jabalpur"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "800          1100",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Jabalpur" and des == "Indore") or (dep == "Indore" and des == "Jabalpur"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1000          1300",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Jabalpur" and des == "Delhi") or (dep == "Delhi" and des == "Jabalpur"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "800          1100",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Jabalpur" and des == "Jaipur") or (dep == "Jaipur" and des == "Jabalpur"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "400          600",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Jabalpur" and des == "Lucknow") or (dep == "Lucknow" and des == "Jabalpur"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "400          600",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Gwalior" and des == "Indore") or (dep == "Indore" and des == "Gwalior"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1400          1700",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Gwalior" and des == "Delhi") or (dep == "Delhi" and des == "Gwalior"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "900          1200",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Gwalior" and des == "Jaipur") or (dep == "Jaipur" and des == "Gwalior"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "600          900",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Gwalior" and des == "Lucknow") or (dep == "Lucknow" and des == "Gwalior"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1000          1300",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Indore" and des == "Delhi") or (dep == "Delhi" and des == "Indore"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1000          1300",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Indore" and des == "Jaipur") or (dep == "Jaipur" and des == "Indore"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "1100          1400",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Indore" and des == "Lucknow") or (dep == "Lucknow" and des == "Indore"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "800          1100",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Delhi" and des == "Jaipur") or (dep == "Jaipur" and des == "Delhi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "800          1100",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Delhi" and des == "Lucknow") or (dep == "Lucknow" and des == "Delhi"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "600          900",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)
    elif (dep == "Jaipur" and des == "Lucknow") or (dep == "Lucknow" and des == "Jaipur"):
        lb4 = Label(heading_frame1, text="Economy Fare     Business Class Fare\n"
                                         "700          1000",  bg="#F3AE58", fg="black", font=('Calibri bold', 13)).place(relx=0.35, rely=0.5)

def price_c():
    global root, dep_info, dest_info, heading_frame1

    root = Toplevel()
    root.title("JourneyJunction")
    root.geometry("1450x801")
    con = pymysql.connect(host="localhost", user="root", password='', database="train")
    cur = con.cursor()

    back = ImageTk.PhotoImage(file = "lib.jpg")
    bg = Label(root, image = back, bg = "#F3AE58").place(x = 0, y = 0, height = 801,width = 1450)

    dep_info = StringVar()
    dest_info = StringVar()

    heading_frame1 = Frame(root, bg="#F3AE58",bd=7, relief=RIDGE)
    heading_frame1.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.4)

    headingLabel = Label(heading_frame1, text="Fare Details", bg="#F3AE58", fg="black",
                     font=('Impact', 50))
    headingLabel.place(relx=0.32, y=18)

    lb1 = Label(heading_frame1, text="Departure: ", bg="#F3AE58", fg="black", font=('Calibri', 18))
    lb1.place(relx=0.1, rely=0.3)

    inf1 = ttk.Combobox(heading_frame1, textvariable=dep_info, width=47)
    inf1['values'] = ['Select', "Bhopal", "Jabalpur", "Indore", "Gwalior", "Delhi", "Lucknow", "Jaipur"]
    inf1.place(relx=0.3, rely=0.3, relwidth=0.60)
    inf1.current(0)


    lb2 = Label(heading_frame1, text="Destination : ", bg="#F3AE58", fg="black", font=('Calibri', 18))
    lb2.place(relx=0.1, rely=0.4)

    inf2 = ttk.Combobox(heading_frame1, textvariable=dest_info, width=47)
    inf2['values'] = ['Select', "Bhopal", "Jabalpur", "Indore", "Gwalior", "Delhi", "Lucknow", "Jaipur"]
    inf2.place(relx=0.3, rely=0.4, relwidth=0.60)
    inf2.current(0)

    lb3 = Label(heading_frame1, text="Fare: ", bg="#F3AE58", fg="black", font=('Calibri bold', 18)).place(relx=0.1, rely=0.5)

    issue_btn = Button(root,
                       text="Submit",
                       bg='black',
                       fg='black',
                       font=('Calibri bold', 30),
                       command=price
                       )
    issue_btn.place(
        relx=0.29,
        rely=0.53,
        relwidth=0.18,
        relheight=0.08
    )

    quit_btn = Button(root,
                      text="Quit",
                      bg='black',
                      fg='black',
                      font=('Calibri bold', 30),
                      command=root.destroy
                      )
    quit_btn.place(
        relx=0.53,
        rely=0.53,
        relwidth=0.18,
        relheight=0.08
    )

    root.mainloop()