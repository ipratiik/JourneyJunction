from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

def view():
    root = Toplevel()
    root.title("JourneyJunction")
    root.geometry("1450x801")
    con = pymysql.connect(host="localhost", user="root", password='', database="train")
    cur = con.cursor()

    back = ImageTk.PhotoImage(file = "lib.jpg")
    bg = Label(root, image = back, bg = "#FAA460").place(x = 0, y = 0, height = 801,width = 1450)

    heading_frame1 = Frame(root, bg='#F3AE58',bd=7, relief=RIDGE)
    heading_frame1.place(relx=0.03, rely=0.06, relwidth=0.95, relheight=0.8)

    heading_label = Label(heading_frame1, text="Booking Details", bg='#F3AE58', fg='black', font=('FZShuTi', 50,'bold'))
    heading_label.place(relx=0.37, y=25)

    y = 0.3

    Label(heading_frame1,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg='#F3AE58',fg="black").place(relx=0.05, rely=0.17)
    Label(heading_frame1, text="    {:<15}   {:<5} {:<8} {:<20} {:<16} {:<13} {:<43} {:<40} {:<10}".format('Name', 'Age', 'CNIC', 'Date', 'Booking Class', 'Departure', 'Destination', 'Time', 'Fare'), font=('Calibri bold', 18), bg='#F3AE58', fg="black").place(
        relx=0.07, rely=0.21)
    Label(heading_frame1,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg='#F3AE58',
    fg="black").place(relx=0.05, rely=0.25)
    get_bookings = "select * from " + "passenger_detail"
    try:
        cur.execute(get_bookings)
        con.commit()
        for i in cur:
            Label(heading_frame1, text='%-20s %-7s%-10s%-18s%-23s%-20s%-20s%-50s%-10s' % (i[0], i[1], i[2], i[3], i[4] , i[5], i[6], i[8], i[9]), font=('Calibri', 16), bg='#F3AE58', fg="black").place(
                relx=0.07, rely=y)
            y += 0.1
    except (pymysql.Error, pymysql.Warning):
        messagebox.showinfo("Failed to fetch files from database.")

    quit_btn = Button(root,
                      text="Quit",
                      bg='black',
                      fg='black',
                      font=('Calibri bold', 18),
                      command=root.destroy
                      )
    quit_btn.place(
        relx=0.4,
        rely=0.9,
        relwidth=0.18,
        relheight=0.08
        )

    root.mainloop()