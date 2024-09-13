from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
import pymysql
import random
from PIL import ImageTk, Image

def p_detail():
    global cnic_var, date_var, class_var, departure_var, txt_destination, txt_timing
    con = pymysql.connect(host="localhost", user="root", password="", database="train")
    cur = con.cursor()
    cnic_var_ = cnic_var.get()
    date_var_ = date_var.get()
    class_var_ = class_var.get()
    departure_var_ = departure_var.get()
    txt_destination_ = txt_destination.get()
    txt_timing_ = txt_timing.get()

    if cnic_var_ == '' or date_var_ == '' or class_var_ == '' or departure_var_ == '' or txt_destination_ == '' or txt_timing_ == '':
        messagebox.showerror("Error!", "Field cannot be empty")

    else:
        cur.execute("select * from passenger_detail where cnic = %s", cnic_var_)
        row = cur.fetchone()
        if row is not None:
            sql = "UPDATE passenger_detail SET CNIC = %s, date = %s, booking_class = %s, departure = %s, destination = %s, timing = %s WHERE CNIC = %s"
            val = (cnic_var_, date_var_, class_var_, departure_var_, txt_destination_, txt_timing_, cnic_var_)
            cur.execute(sql, val)
            con.commit()
            print(cur.rowcount, "Booking Updated.")
            cnic_var.set("")
            date_var.set("")
            class_var.set("")
            departure_var.set("")
            txt_destination.set("")
            txt_timing.set("")
            messagebox.showinfo("Info", "Booking,Updated!!!")
        else:
            messagebox.showerror("Error", "No booking to update.")



def update_c():
    con = pymysql.connect(host="localhost", user="root", password="", database="train")
    cur = con.cursor()
    global row
    CNIC = cnic_var.get()
    update_sql = "SElECT * FROM passenger_detail WHERE CNIC = %s"
    try:
        cur.execute(update_sql, (CNIC,))
        row = cur.fetchone()
        print(row)
        m_ain()

    except (pymysql.Error, pymysql.Warning):
        messagebox.showerror("Error", "Please check your Client Id.")
    cnic_var.set("")


def m_ain():
    global cnic_var, date_var, class_var, departure_var, txt_destination, txt_timing, n_ame
    root = Toplevel()
    root.title("JourneyJunction")
    root.geometry("1450x801")
    con = pymysql.connect(host="localhost", user="root", password='', database="train")
    cur = con.cursor()
    cnic_var = StringVar()
    date_var = StringVar()
    class_var = StringVar()
    departure_var = StringVar()
    txt_destination = StringVar()
    txt_timing = StringVar()

    back = ImageTk.PhotoImage(file = "lib.jpg")
    bg = Label(root, image = back, bg = "#FAA460").place(x = 0, y = 0, height = 801,width = 1450)

    headingFrame1 = Frame(root, bg='#F3AE58',bd=7, relief=RIDGE)
    headingFrame1.place(relx=0.3, rely=0.19, relwidth=0.37, relheight=0.69)
    headingLabel = Label(headingFrame1, text="Update Booking", bg='#F3AE58', fg='black',font=('Impact', 50))
    headingLabel.place(relx=0.18, y=17)

    cur.execute("select * from passenger_detail")
    con.commit()
    for i in cur:
        n_ame = i[3]
        print(n_ame)

    CNIC = Label(headingFrame1, text="Client Id:", bg='#F3AE58', fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=90)
    txt_cnic = Entry(headingFrame1, textvariable=cnic_var, font=('Calibri', 12)).place(relx=0.2, y=120, width=300)

    Date = Label(headingFrame1, text="Date:", bg='#F3AE58', fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=150)
    txt_date = DateEntry(headingFrame1, textvariable=date_var, selectmode='day', date_pattern='yyyy/mm/dd')
    txt_date.place(relx=0.2, y=180, width=300)

    Booking_Class = Label(headingFrame1, text="Booking Class:", bg='#F3AE58', fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=210)
    txt_class = ttk.Combobox(headingFrame1, textvariable=class_var, width=47)
    txt_class['values'] = ['Select', "Economy", "Business"]
    txt_class.place(relx=0.2, y=240, width=300)

    Departure = Label(headingFrame1, text="Departure:", bg='#F3AE58', fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=270)
    txt_departure = ttk.Combobox(headingFrame1, textvariable=departure_var, width=47)
    txt_departure['values'] = ['Select', "Bhopal", "Jabalpur", "Indore", "Gwalior", "Delhi", "Lucknow", "Jaipur"]
    txt_departure.place(relx=0.2, y=300,width=300)

    Destination = Label(headingFrame1, text="Destination:", bg='#F3AE58', fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=330)
    txt_destination = ttk.Combobox(headingFrame1, textvariable=txt_destination, width=47)
    txt_destination['values'] = ['Select', "Bhopal", "Jabalpur", "Indore", "Gwalior", "Delhi", "Lucknow", "Jaipur"]
    txt_destination.place(relx=0.2, y=360, width=300)

    Timing = Label(headingFrame1, text="Time:", bg='#F3AE58', fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=390)
    txt_timing = ttk.Combobox(headingFrame1, textvariable=txt_timing, width=30)
    v1 = ['Select', 'Departure : 10AM     Destination : 02PM', 'Departure : 12AM     Destination : 04PM', 'Departure : 02PM     Destination : 06PM', 'Departure : 04PM     Destination : 08PM', 'Departure : 06PM     Destination : 10PM']
    v2 = ['Select', 'Departure : 10AM     Destination : 01PM', 'Departure : 12AM     Destination : 03PM', 'Departure : 02PM     Destination : 05PM', 'Departure : 04PM     Destination : 07PM', 'Departure : 06PM     Destination : 09PM']
    v3 = ['Select', 'Departure : 10AM     Destination : 04PM', 'Departure : 12AM     Destination : 06PM', 'Departure : 02PM     Destination : 08PM', 'Departure : 04PM     Destination : 10PM', 'Departure : 06PM     Destination : 12AM']
    v4 = ['Select', 'Departure : 10AM     Destination : 10PM', 'Departure : 12AM     Destination : 12PM', 'Departure : 02PM     Destination : 02AM', 'Departure : 04PM     Destination : 04AM', 'Departure : 06PM     Destination : 06AM']
    v5 = ['Select', 'Departure : 10AM     Destination : 03PM', 'Departure : 12AM     Destination : 05PM', 'Departure : 02PM     Destination : 07AM', 'Departure : 04PM     Destination : 09AM', 'Departure : 06PM     Destination : 11AM']
    v = [v1, v2, v3, v4, v5]
    r = random.choice(v)
    txt_timing['values'] = r
    txt_timing.place(relx=0.2, y=418)

    confirm = Button(headingFrame1,
                     command=p_detail,
                     text="Confirm",
                     bg='#000000',
                     fg='#000000',
                     font=('Calibri bold', 20)).place(relx=0.1, y=480, width=400)
    
    backbutton = Button(root,
                     command=root.destroy,
                     text="Back",
                     bg='#000000',
                     fg='#000000',
                     font=('Calibri bold', 20)).place(relx=0.458, y=730, width=60)
    
    
    root.mainloop()