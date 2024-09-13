from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
import pymysql
import random
from PIL import ImageTk, Image

def passenger_details():
    global name_var, age_var, cnic_var, date_var, class_var, departure_var, txt_destination, txt_timing
    con = pymysql.connect(host="localhost", user="root", password='', database="train")
    cur = con.cursor()
    name_var_ = name_var.get()
    age_var_ = age_var.get()
    cnic_var_ = cnic_var.get()
    date_var_ = date_var.get()
    class_var_ = class_var.get()
    departure_var_ = departure_var.get()
    txt_destination_ = txt_destination.get()
    txt_timing_ = txt_timing.get()
    fair = 0
    if (departure_var_ == "Bhopal" and txt_destination_ == "Jabalpur") or (txt_destination_ == "Bhopal" and departure_var_ == "Jabalpur"):
        if class_var_ == "Economy":
            fair += 500
        elif class_var_ == "Business":
            fair += 800
    elif (departure_var_ == "Bhopal" and txt_destination_ == "Gwalior") or (departure_var_ == "Gwalior" and txt_destination_ == "Bhopal"):
        if class_var_ == "Economy":
            fair += 400
        elif class_var_ == "Business":
            fair += 700
    elif (departure_var_ == "Bhopal" and txt_destination_ == "Indore") or (departure_var_ == "Indore" and txt_destination_ == "Bhopal"):
        if class_var_ == "Economy":
            fair += 1200
        elif class_var_ == "Business":
            fair += 1600
    elif (departure_var_ == "Bhopal" and txt_destination_ == "Delhi") or (departure_var_ == "Delhi" and txt_destination_ == "Bhopal"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Bhopal" and txt_destination_ == "Jaipur") or (departure_var_ == "Jaipur" and txt_destination_ == "Bhopal"):
        if class_var_ == "Economy":
            fair += 400
        elif class_var_ == "Business":
            fair += 700
    elif (departure_var_ == "Bhopal" and txt_destination_ == "Lucknow") or (departure_var_ == "Lucknow" and txt_destination_ == "Bhopal"):
        if class_var_ == "Economy":
            fair += 700
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Jabalpur" and txt_destination_ == "Gwalior") or (departure_var_ == "Gwalior" and txt_destination_ == "Jabalpur"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Jabalpur" and txt_destination_ == "Indore") or (departure_var_ == "Indore" and txt_destination_ == "Jabalpur"):
        if class_var_ == "Economy":
            fair += 1000
        elif class_var_ == "Business":
            fair += 1300
    elif (departure_var_ == "Jabalpur" and txt_destination_ == "Delhi") or (departure_var_ == "Delhi" and txt_destination_ == "Jabalpur"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Jabalpur" and txt_destination_ == "Jaipur") or (departure_var_ == "Jaipur" and txt_destination_ == "Jabalpur"):
        if class_var_ == "Economy":
            fair += 400
        elif class_var_ == "Business":
            fair += 600
    elif (departure_var_ == "Jabalpur" and txt_destination_ == "Lucknow") or (departure_var_ == "Lucknow" and txt_destination_ == "Jabalpur"):
        if class_var_ == "Economy":
            fair += 400
        elif class_var_ == "Business":
            fair += 600
    elif (departure_var_ == "Gwalior" and txt_destination_ == "Indore") or (departure_var_ == "Indore" and txt_destination_ == "Gwalior"):
        if class_var_ == "Economy":
            fair += 1400
        elif class_var_ == "Business":
            fair += 1700
    elif (departure_var_ == "Gwalior" and txt_destination_ == "Delhi") or (departure_var_ == "Delhi" and txt_destination_ == "Gwalior"):
        if class_var_ == "Economy":
            fair += 900
        elif class_var_ == "Business":
            fair += 1200
    elif (departure_var_ == "Gwalior" and txt_destination_ == "Jaipur") or (departure_var_ == "Jaipur" and txt_destination_ == "Gwalior"):
        if class_var_ == "Economy":
            fair += 600
        elif class_var_ == "Business":
            fair += 900
    elif (departure_var_ == "Gwalior" and txt_destination_ == "Lucknow") or (departure_var_ == "Lucknow" and txt_destination_ == "Gwalior"):
        if class_var_ == "Economy":
            fair += 1000
        elif class_var_ == "Business":
            fair += 1300
    elif (departure_var_ == "Indore" and txt_destination_ == "Delhi") or (departure_var_ == "Delhi" and txt_destination_ == "Indore"):
        if class_var_ == "Economy":
            fair += 1000
        elif class_var_ == "Business":
            fair += 1300
    elif (departure_var_ == "Indore" and txt_destination_ == "Jaipur") or (departure_var_ == "Jaipur" and txt_destination_ == "Indore"):
        if class_var_ == "Economy":
            fair += 1100
        elif class_var_ == "Business":
            fair += 1400
    elif (departure_var_ == "Indore" and txt_destination_ == "Lucknow") or (departure_var_ == "Lucknow" and txt_destination_ == "Indore"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Delhi" and txt_destination_ == "Jaipur") or (departure_var_ == "Jaipur" and txt_destination_ == "Delhi"):
        if class_var_ == "Economy":
            fair += 800
        elif class_var_ == "Business":
            fair += 1100
    elif (departure_var_ == "Delhi" and txt_destination_ == "Lucknow") or (departure_var_ == "Lucknow" and txt_destination_ == "Delhi"):
        if class_var_ == "Economy":
            fair += 600
        elif class_var_ == "Business":
            fair += 900
    elif (departure_var_ == "Jaipur" and txt_destination_ == "Lucknow") or (departure_var_ == "Lucknow" and txt_destination_ == "Jaipur"):
        if class_var_ == "Economy":
            fair += 700
        elif class_var_ == "Business":
            fair += 1000

    if name_var_ == '' or age_var_ == '' or cnic_var_ == '' or date_var_ == '' or class_var_ == '' or departure_var_ == '' or txt_destination_ == '' or txt_timing_ == '':
        messagebox.showerror("Error!", "Field cannot be empty")
    else:
        age_var_ = int(age_var_)
        if age_var_ <= 2:
            fair = fair*0
        elif age_var_ <= 18 and age_var_ > 2:
            fair = fair*(1-0.2)
        elif age_var_ >= 60:
            fair = fair*(1-0.4)
        age_var_ = str(age_var_)
        cur.execute("select * from passenger_detail where cnic = %s", cnic_var_)
        row = cur.fetchone()
        if row is not None:
            messagebox.showerror("Error", "Ticket already booked . If you want to book or another destination cancel previous ticket.")
        else:
            sql = "INSERT INTO `passenger_detail` (`name`,`age`, `CNIC`, `date`,`booking_class`,`departure`,`destination`,`timing`, `fare`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name_var_, age_var_, cnic_var_, date_var_, class_var_, departure_var_, txt_destination_, txt_timing_, fair)
            cur.execute(sql, val)
            con.commit()
            print(cur.rowcount, "record inserted.")
            name_var.set("")
            age_var.set("")
            cnic_var.set("")
            date_var.set("")
            class_var.set("")
            departure_var.set("")
            txt_destination.set("")
            txt_timing.set("")
            messagebox.showinfo("Success!", "Booking Done Successfully")


def main():
    global name_var, age_var, cnic_var, date_var, class_var, departure_var, txt_destination, txt_timing, headingFrame1
    root = Toplevel()
    root.title("JourneyJunction")
    root.geometry("1450x801")
    con = pymysql.connect(host="localhost", user="root", password='', database="train")
    cur = con.cursor()

    cnic_var = StringVar()
    name_var = StringVar()
    age_var = StringVar()
    cnic_var = StringVar()
    date_var = StringVar()
    class_var = StringVar()
    departure_var = StringVar()
    txt_destination = StringVar()
    txt_timing = StringVar()

    back = ImageTk.PhotoImage(file = "lib.jpg")
    bg = Label(root, image = back, bg = "#FAA460").place(x = 0, y = 0, height = 801,width = 1450)

    headingFrame1 = Frame(root, bg="#F3AE58",bd=7, relief=RIDGE)
    headingFrame1.place(relx=0.31, rely=0.1, relwidth=0.38, relheight=0.85)

    headingLabel = Label(headingFrame1, text="Ticket Booking", bg="#F3AE58", fg="black",font=('Impact', 50))
    headingLabel.place(relx=0.197, y=15)

    userName = Label(headingFrame1, text="Name:",  bg="#F3AE58", fg="black", font=('Calibri bold', 15)).place(relx=0.2,y=90)
    txt_userName = Entry(headingFrame1, textvariable=name_var, font=('Calibri', 13)).place(relx=0.2, y=120, width=300)

    age = Label(headingFrame1, text="Age:",  bg="#F3AE58", fg="black", font=('Calibri bold', 15)).place(relx=0.2,y=150)
    txt_age = Entry(headingFrame1, textvariable=age_var, font=('Calibri', 13)).place(relx=0.2, y=180, width=300)

    CNIC = Label(headingFrame1, text="Client Id:",  bg="#F3AE58", fg="black", font=('Calibri bold', 15)).place(relx=0.2,y=210)
    txt_cnic = Entry(headingFrame1, textvariable=cnic_var, font=('Calibri', 13)).place(relx=0.2, y=240, width=300)

    Date = Label(headingFrame1, text="Date:",  bg="#F3AE58", fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=270)
    txt_date = DateEntry(headingFrame1, textvariable=date_var, selectmode='day', date_pattern='yyyy/mm/dd').place(relx=0.2, y=300, width=300)

    Booking_Class = Label(headingFrame1, text="Booking Class:",  bg="#F3AE58", fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=330)
    txt_class = ttk.Combobox(headingFrame1, textvariable=class_var, width=47)
    txt_class['values'] = ['Select', "Economy", "Business"]
    txt_class.place(relx=0.2, y=360, width=300)
    txt_class.current(0)

    Departure = Label(headingFrame1, text="Departure:",  bg="#F3AE58", fg="black", font=('Calibri bold', 15)).place(relx=0.2,y=390)
    txt_departure = ttk.Combobox(headingFrame1, textvariable=departure_var, width=47)
    txt_departure['values'] = ['Select', "Bhopal", "Jabalpur", "Indore", "Gwalior", "Delhi", "Lucknow", "Jaipur"]
    txt_departure.place(relx=0.2, y=420, width=300)
    txt_departure.current(0)

    Destination = Label(headingFrame1, text="Destination:",  bg="#F3AE58", fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=450)
    txt_destination = ttk.Combobox(headingFrame1, textvariable=txt_destination, width=47)
    txt_destination['values'] = ['Select', "Bhopal", "Jabalpur", "Indore", "Gwalior", "Delhi", "Lucknow", "Jaipur"]
    txt_destination.place(relx=0.2, y=480, width=300)
    txt_destination.current(0)

    Timing = Label(headingFrame1, text="Time:",  bg="#F3AE58", fg="black", font=('Calibri bold', 15)).place(relx=0.2, y=510)
    txt_timing = ttk.Combobox(headingFrame1, textvariable=txt_timing, width=47)
    v1 = ['Select', 'Departure : 10AM     Destination : 02PM', 'Departure : 12AM     Destination : 04PM', 'Departure : 02PM     Destination : 06PM', 'Departure : 04PM     Destination : 08PM', 'Departure : 06PM     Destination : 10PM']
    v2 = ['Select', 'Departure : 10AM     Destination : 01PM', 'Departure : 12AM     Destination : 03PM', 'Departure : 02PM     Destination : 05PM', 'Departure : 04PM     Destination : 07PM', 'Departure : 06PM     Destination : 09PM']
    v3 = ['Select', 'Departure : 10AM     Destination : 04PM', 'Departure : 12AM     Destination : 06PM', 'Departure : 02PM     Destination : 08PM', 'Departure : 04PM     Destination : 10PM', 'Departure : 06PM     Destination : 12AM']
    v4 = ['Select', 'Departure : 10AM     Destination : 10PM', 'Departure : 12AM     Destination : 12PM', 'Departure : 02PM     Destination : 02AM', 'Departure : 04PM     Destination : 04AM', 'Departure : 06PM     Destination : 06AM']
    v5 = ['Select', 'Departure : 10AM     Destination : 03PM', 'Departure : 12AM     Destination : 05PM', 'Departure : 02PM     Destination : 07AM', 'Departure : 04PM     Destination : 09AM', 'Departure : 06PM     Destination : 11AM']
    v = [v1, v2, v3, v4, v5]
    r = random.choice(v)
    txt_timing['values'] = r
    txt_timing.place(relx=0.2, y=540, width=300)
    txt_timing.current(0)

    confirm = Button(headingFrame1,
                     command=passenger_details,
                     text="Confirm",
                     bg='#000000',
                     fg='#000000',
                     font=('Calibri bold', 30,'bold')).place(relx=0.118, y=600, width=400)
    
    backbutton = Button(root,
                     command=root.destroy,
                     text="Back",
                     bg='#000000',
                     fg='#000000',
                     font=('Calibri bold', 20)).place(relx=0.475, y=763, width=60)

    root.mainloop()

# passenger_details()