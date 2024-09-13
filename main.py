from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk,Image
from fare import price_c
from View_Booking import view
from update import m_ain
from book_your_ticket import main
from Cancel_booking import delete
import pymysql


class run():
    def __init__(self, root) :
        self.root = root
        self.root.title("JourneyJunction")
        self.root.geometry("1450x801")
        self.Login_Interface()


    def Login_Interface(self):
        self.bg = ImageTk.PhotoImage(file = "lib.jpg")
        bg = Label(self.root, image = self.bg).place(x = 0, y = 0, height = 801,width = 1536)

        self.Logo = ImageTk.PhotoImage(file = "icon.png")
        Logo = Label(self.root, image = self.Logo).place(x = 264.6, y = 180, height = 435, width = 435)

        Login_Frame = Frame(self.root, bg = "#F3AE58",relief = RIDGE,bd=5)
        Login_Frame.place(x = 700, y = 180, width = 450, height = 435)

        Title = Label(Login_Frame, text = "Sign In", font = ("FZShuTi", 50, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 46, y = 38)

        Username = Label(Login_Frame, text = "Username:", font = ("Product Sans", 20, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 46, y = 130)
        self.txt_Username = Entry (Login_Frame, font = ("Product Sans", 15), bg = "black",fg="white")
        self.txt_Username.place(x = 50, y = 170, height = 35, width = 350)

        Password = Label(Login_Frame, text = "Password:", font = ("Product Sans", 20, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 46, y = 230)
        self.txt_Password = Entry (Login_Frame, font = ('Calibri bold', 18, "bold"), bg = "black", show = "*",fg="white")
        self.txt_Password.place(x = 50, y = 270, height = 35, width = 350)

        btn_register = Button(Login_Frame, text = "Login",font = ('Calibri bold', 40,'bold'), bd = 1, bg = "#F3AE58", cursor = 'hand2',fg="#630000", relief = RIDGE, command = self.Login)
        btn_register.place(x = 250, y = 330, height = 80, width = 150)

        Title = Label(Login_Frame, text = "Don't Have an Account?", font = ("FZShuTi", 15, 'bold'), bg = "#F3AE58", fg = "#630000").place(x = 50, y = 335)
        btn_login = Button(self.root, text = "Sign Up", font = ('Calibri bold', 25,'bold'), bg = "#F99A05",fg="#630000", bd = 1, relief = RIDGE, cursor = "hand2", command = self.Registration_Interface)
        btn_login.place(x = 787, y = 552, height = 40, width = 110)

        btn6 = Button(self.root,
                    text="Quit",
                    bg='#000000',
                    fg="#000000",
                    font=('Calibri bold', 20,'bold'),
                    command=self.root.destroy
                    )
        btn6.place(
            relx=0.33,
            rely=0.83,
            relwidth=0.35,
            relheight=0.06
        )

        self.root.bind('<Return>',lambda event:self.Login())

    
    def Login(self):
        if self.txt_Username.get() == "" and self.txt_Password.get() == "" :
            messagebox.showerror("JourneyJunction", "Enter Username And Password", icon = "warning", parent = self.root)

        elif self.txt_Username.get() == "" :
            messagebox.showerror("JourneyJunction", "Enter Username", icon = "warning", parent = self.root)

        elif self.txt_Password.get() == "" :
            messagebox.showerror("JourneyJunction", "Enter Password", icon = "warning", parent = self.root)

        else:
            mycon = pymysql.connect(host="localhost",user="root",password="",database="train")
            cursor = mycon.cursor()
            cursor.execute("SELECT * FROM Accounts WHERE Username = %s AND Password = %s", (self.txt_Username.get(), self.txt_Password.get()))
            row = cursor.fetchone()
            if row == None :
                messagebox.showerror("JourneyJunction", "Invalid Username/Password", icon = "warning", parent = self.root)
                self.Login_Clear()
            else :
                messagebox.showinfo("JourneyJunction", "Welcome To JourneyJunction", parent = self.root)
                self.run_journey_junction()
            mycon.close()
            
    def Login_Clear(self) :
        self.txt_Username.delete("0",END)
        self.txt_Password.delete("0",END)


    def Registration_Interface(self):
        self.bg = ImageTk.PhotoImage(file = "lib.jpg")
        bg = Label(self.root, image = self.bg, bg = "#FAA460").place(x = 0, y = 0, height = 801,width = 1536)

        self.Logo = ImageTk.PhotoImage(file = "icon.png")
        Left = Label(self.root, image = self.Logo).place(x = 155, y = 180, height = 435, width = 435)

        Registration_Frame=Frame(self.root, bg = "#F3AE58",bd=5,relief=RIDGE)
        Registration_Frame.place(x = 588, y = 180, width = 700, height = 435)

        title = Label(Registration_Frame, text = "Sign Up", font = ("FZShuTi", 50, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 70, y = 30)

        FirstName = Label(Registration_Frame, text = "First Name:", font = ("Product Sans", 15, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 70, y = 120)
        self.txt_FirstName = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "black",fg="white")
        self.txt_FirstName.place(x = 70, y = 150, width = 250)

        LastName = Label(Registration_Frame, text = "Last Name:", font = ("Product Sans", 15, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 380, y = 120)
        self.txt_LastName = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "black",fg="white")
        self.txt_LastName.place(x = 380, y = 150, width = 250)

        Username = Label(Registration_Frame, text = "Username:", font = ("Product Sans", 15, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 70, y = 190)
        self.txt_Username = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "black",fg="white")
        self.txt_Username.place(x = 70, y = 220, width = 250)

        Email = Label(Registration_Frame, text = "E-Mail:", font = ("Product Sans", 15, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 380, y = 190)
        self.txt_Email = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "black",fg="white")
        self.txt_Email.place(x = 380, y = 220, width = 250)

        Password = Label(Registration_Frame, text = "Password:", font = ("Product Sans", 15, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 70, y = 270)
        self.txt_Password = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, bg = "black",fg="white", show = "*")
        self.txt_Password.place(x = 70, y = 300, width = 250)

        ConfirmPassword = Label(Registration_Frame, text = "Confirm Password:", font = ("Product Sans", 15, "bold"), bg = "#F3AE58", fg = "#630000").place(x = 380, y = 270)
        self.txt_ConfirmPassword = Entry (Registration_Frame, font = ("Product Sans", 15), justify = CENTER, show = "*",bg = "black",fg="white")
        self.txt_ConfirmPassword.place(x = 380, y = 300, width = 250)

        btn_register = Button(Registration_Frame, text = "Register",font = ("20th Century Font", 40,'bold'), bd = 1,fg="#630000", bg = "#F99A05", cursor = 'hand2', relief = RIDGE, command = self.Registration)
        btn_register.place(x = 410, y = 355, height = 60, width = 200)

        Title = Label(Registration_Frame, text = "Already Have An Account?", font = ("FZShuTi", 15, 'bold'), bg = "#F3AE58", fg = "#630000").place(x = 90, y = 345)
        btn_login = Button(self.root, text = "Sign In", font = ("20th Century Font", 20,'bold'), bg = "#F99A05",fg="#630000", bd = 1, relief = RIDGE, cursor = "hand2", command = self.Login_Interface)
        btn_login.place(x = 729, y = 562, height = 40, width = 110)

        btn6 = Button(self.root,
                    text="Quit",
                    bg='#000000',
                    fg="#000000",
                    font=('Calibri bold', 20,'bold'),
                    command=self.root.destroy
                    )
        btn6.place(
            relx=0.33,
            rely=0.83,
            relwidth=0.35,
            relheight=0.06
        )
        self.root.bind('<Return>',lambda event:self.Registration())

    def Registration(self) :
        if self.txt_FirstName.get() == "" or self.txt_Email.get() == "" or self.txt_FirstName.get() == "" or self.txt_Username.get() == "" or self.txt_Password.get() == "" or self.txt_ConfirmPassword.get() == "":
            messagebox.showerror("JourneyJunction", "All fields are required.", icon = "warning", parent = self.root)

        elif self.txt_Password.get() != self.txt_ConfirmPassword.get() :
            messagebox.showerror("JourneyJunction", "Confirm Password is different.", icon = "warning",  parent = self.root)

        else :
            mycon = pymysql.connect(host="localhost",user="root",password="",database="train")
            cursor = mycon.cursor()
            cursor.execute("SELECT * FROM Accounts WHERE Username = %s", self.txt_Username.get())
            Username = cursor.fetchone()
            cursor.execute("SELECT * FROM Accounts WHERE Email = %s", self.txt_Email.get())
            Email = cursor.fetchone()
            if Username != None :
                messagebox.showerror("JourneyJunction", "User already exists, Try Other!", icon = "warning", parent = self.root)
            elif Email != None :
                messagebox.showerror("JourneyJunction", "Email already exists, Try Other!", icon = "warning", parent = self.root)
            else :
                cursor.execute("INSERT INTO Accounts (First_Name, Last_Name, Username, Email, Password) VALUES (%s,%s,%s,%s,%s)",
                                                 (self.txt_FirstName.get(),
                                                 self.txt_LastName.get(),
                                                 self.txt_Username.get(),
                                                 self.txt_Email.get(),
                                                 self.txt_Password.get()
                                                    ))
                messagebox.showinfo("JourneyJunction", "Account Created Successfully", parent = self.root)        
            mycon.commit()
            mycon.close()	

    def Registration_Clear(self) :
        self.txt_FirstName.delete(0,END)
        self.txt_LastName.delete(0,END)
        self.txt_Username.delete(0,END)
        self.txt_Email.delete(0,END)
        self.txt_Password.delete(0,END)
        self.txt_ConfirmPassword.delete(0,END)

    def run_journey_junction(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="train")
        cursor= con.cursor()

        self.bg = ImageTk.PhotoImage(file = "lib.jpg")
        bg = Label(self.root, image = self.bg, bg = "#F3AE58").place(x = 0, y = 0, height = 801,width = 1450)

        headingFrame1 = Frame(self.root, bg="#F3AE58", bd=7,relief=RIDGE)
        headingFrame1.place(relx=0.305, rely=0.1, relwidth=0.4, relheight=0.8)

        authorLabel = Label(headingFrame1, text="Developed By: Pratik", bg="#F3AE58", fg='black', font=('Arial', 14))
        authorLabel.place(relx=0.38, rely=0.9)

        headingLabel = Label(headingFrame1, text="Welcome To\n JourneyJunction", bg="#F3AE58", fg='black',font=('FZShuTi', 40,'bold'))
        headingLabel.place(relx=0.2, y=50)

        btn1 = Button(root,
                    text="Book A Ticket",
                    bg='white',
                    fg="#000000",
                    font=('Calibri bold', 20,'bold'),
                    command=main
                    )
        btn1.place(
            relx=0.33,
            rely=0.33,
            relwidth=0.35,
            relheight=0.06
        )

        # ===Button 2===
        btn2 = Button(root,
                    text="Cancel Booking",
                    bg='#000000',
                    fg="#000000",
                    font=('Calibri bold', 20,'bold'),
                    command=delete
                    )
        btn2.place(
            relx=0.33,
            rely=0.65,
            relwidth=0.35,
            relheight=0.06
        )

        # ===Button 3===
        btn3 = Button(root,
                    text="Ticket Details",
                    bg='#000000',
                    fg="#000000",
                    font=('Calibri bold', 20,'bold'),
                    command=view
                    )
        btn3.place(
            relx=0.33,
            rely=0.49,
            relwidth=0.35,
            relheight=0.06
        )

        # ===Button 4===
        btn4 = Button(root,
                    text="Ticket Fare",
                    bg='#000000',
                    fg="#000000",
                    font=('Calibri bold', 20,'bold'),
                    command=price_c
                    )
        btn4.place(
            relx=0.33,
            rely=0.57,
            relwidth=0.35,
            relheight=0.06
        )

        # ===Button 5===
        btn5 = Button(root,
                    text="Update Booking",
                    bg='#000000',
                    fg="#000000",
                    font=('Calibri bold', 20,'bold'),
                    command=m_ain
                    )
        btn5.place(
            relx=0.33,
            rely=0.41,
            relwidth=0.35,
            relheight=0.06
        )

        btn6 = Button(root,
                    text="Quit",
                    bg='#000000',
                    fg="#000000",
                    font=('Calibri bold', 20,'bold'),
                    command=self.runpage
                    )
        btn6.place(
            relx=0.33,
            rely=0.73,
            relwidth=0.35,
            relheight=0.06
        )

    def runpage(self):
        self.Login_Interface()

root = Tk()
obj = run(root)
root.mainloop()
