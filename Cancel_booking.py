from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

def delete_book():
    CNIC = cnic_var.get()
    delete_sql = "DElETE FROM passenger_detail WHERE CNIC = %s"
    if CNIC == '':
        messagebox.showerror("Error", "Field cannot be empty")
        root.mainloop()
    else:
        try:
            cur.execute(delete_sql, (CNIC))
            con.commit()
            messagebox.showinfo('Success', "Booking, Cancelled Successfully!!!")
        except (pymysql.Error, pymysql.Warning):
            messagebox.showerror("Error", "Please check your Client Id.")
    cnic_var.set("")
    root.destroy()


def delete():
    global cnic_var, con, cur, root
    root = Toplevel()
    root.title("JourneyJunction")
    root.geometry("1450x801")
    con = pymysql.connect(host="localhost", user="root", password='', database="train")
    cur = con.cursor()

    back = ImageTk.PhotoImage(file = "lib.jpg")
    bg = Label(root, image = back, bg = "#FAA460").place(x = 0, y = 0, height = 801,width = 1450)
    cnic_var = StringVar()
    my_pass = ""
    my_database = "train"
    con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
    cur = con.cursor()
    background_image = Image.open("lib.jpg")
    img = ImageTk.PhotoImage(background_image)

    # ===Heading===
    heading_frame1 = Frame(root, bg="#F3AE58",bd=7, relief=RIDGE)
    heading_frame1.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.4)

    headingLabel = Label(heading_frame1, text="Cancel Booking", bg="#F3AE58", fg="black",
                     font=('Impact', 50,'bold'))
    headingLabel.place(relx=0.30, y=33)

    lb2 = Label(heading_frame1, text="Client Id: ", bg="#F3AE58", fg="black", font=('Calibri bold', 18))
    lb2.place(relx=0.1, rely=0.44, relheight=0.08)

    book_info2 = Entry(heading_frame1, textvariable=cnic_var, font=('Calibri bold', 12),bg='white', fg='black')
    book_info2.place(relx=0.25, rely=0.44, relwidth=0.62, relheight=0.08)

    submit_btn = Button(root,
                        text="Submit",
                        bg='#000000',
                        fg='#000000',
                        font=('Calibri bold', 22),
                        command=delete_book
                        )
    submit_btn.place(
        relx=0.33,
        rely=0.53,
        relwidth=0.15,
        relheight=0.06
        )

    quit_btn = Button(root,
                      text="Quit",
                      bg='#000000',
                      fg='#000000',
                      font=('Calibri bold', 22),
                      command=root.destroy
                      )
    quit_btn.place(
        relx=0.53,
        rely=0.53,
        relwidth=0.15,
        relheight=0.06
        )

    root.mainloop()