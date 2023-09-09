from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class main_page:
    
    def __init__(self, root):
        
        self.root = root
        
        self.bg_img = Image.open('logo.png')
        self.bg_img = self.bg_img.resize((650,450))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.bg_lbl = Label(root, image= self.bg_img)
        self.bg_lbl.place(x = 0, y = 0)
        
        self.header = Label(root, text = "Hostel Help Desk", fg = "white", bg = "DodgerBlue", font = ("Times New Roman", 30, 'bold'))
        self.header.pack(fill = 'x')
        self.side_header1 = Label(root, text = "Admin", fg = "white", bg = "DodgerBlue", font = ("Times New Roman", 20, 'bold'))
        self.side_header1.place(x = 80, y = 130)
        self.side_header2 = Label(root, text = "Student", fg = "white", bg = "DodgerBlue", font = ("Times New Roman", 20, 'bold'))
        self.side_header2.place(x = 480, y = 130)
        
        self.nameA = Label(root, text = "   UserID  ", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.nameA.place(x = 20, y = 225)
        self.pwdA = Label(root, text = "Password", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.pwdA.place(x = 20, y = 265)
        
        self.nameB = Label(root, text = "  UserID  ", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.nameB.place(x = 410, y = 220)
        self.pwdB = Label(root, text = "Password", fg = "white", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.pwdB.place(x = 410, y = 260)
        
        self.eAA = Entry(root, bd = 3)
        self.eAA.place(x = 115, y = 228)  
        self.eAB = Entry(root, bd = 3)
        self.eAB.place(x = 115, y = 268)  
        
        self.eBA = Entry(root, bd = 3)
        self.eBA.place(x = 495, y = 222)  
        self.eBB = Entry(root, bd = 3)
        self.eBB.place(x = 495, y = 262)
        
        self.login_btnA = Button(root, text = 'Login', bg = 'green3', font=('Times New Roman', 15, 'bold'))
        self.login_btnA.place(x= 80, y = 320)
        
        self.login_btnB = Button(root, text = 'Login', bg = 'green3', font=('Times New Roman', 15, 'bold'), command= self.student_login)
        self.login_btnB.place(x= 480, y = 320)
        
    def login(self):
        messagebox.showinfo('Student Signed ','Student Signed In')
        
    def student_login(self):
        self.login()
        
        root = self.root
        self.header.destroy()
        self.side_header1.destroy()
        self.side_header2.destroy()
        self.eAA.destroy()
        self.eBB.destroy()
        self.eAB.destroy()
        self.eBA.destroy()
        self.nameA.destroy()
        self.pwdA.destroy()
        self.nameB.destroy()
        self.pwdB.destroy()
        self.login_btnA.destroy()
        self.login_btnB.destroy()
        
        self.home_title = Label(root, text= 'Student DashBoard', font = ('Times New Roman', 15, 'bold'))
        self.home_title.pack(fill = 'x')
        self.sd1 = Label(root, text = "Name : D.Saathwika", fg = "black", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.sd1.pack(side = TOP, pady=2)
        self.sd2 = Label(root, text = "Registered Number : 22B01A0536", fg = "black", bg = "orange", font = ("Times New Roman", 12, 'bold'))
        self.sd2.pack(side = TOP, pady=2)
        
        self.icon1=Image.open("health.jpg")
        self.icon1=self.icon1.resize((125,125))
        self.icon1=ImageTk.PhotoImage(self.icon1)
        self.icon_lbl=Label(root,image=self.icon1,bd='5',bg='black')
        self.icon_lbl.place(x=130,y=150)
        
        self.st_butA=Button(root,text='Health Issues',height=2,width=12, font = ("Times New Roman", 12, 'bold'), command = self.complaints)
        self.st_butA.place(x='147',y='315')
        
        self.icon2=Image.open("repairs.jpg")
        self.icon2=self.icon2.resize((125,125))
        self.icon2=ImageTk.PhotoImage(self.icon2)
        self.icon_lb2=Label(root,image=self.icon2,bd='5',bg='black')
        self.icon_lb2.place(x=380,y=150)
        
        self.st_butB=Button(root,text='Repairs',height=2,width=12, font = ("Times New Roman", 12, 'bold'), command = self.complaints)
        self.st_butB.place(x='400',y='315')
        
    def complaints(self):
        
        self.icon_lbl.destroy()
        self.st_butA.destroy()
        self.icon_lb2.destroy()
        self.st_butB.destroy()
        self.sd1.destroy()
        self.sd2.destroy()
        self.bg_lbl.destroy()
        
        
        self.l1=Label(root,text="PROBLEM DETAILS",bg="DodgerBlue2",fg="white",font=("Arial Bold",15),borderwidth=1,relief="solid")
        self.l1.pack(fill='x')
        
        self.l2=Label(root,text="Student Name:",borderwidth=1,relief="solid")
        self.l2.place(x=10,y=60,width=120)
        
        self.e1=Entry(root)
        self.e1.place(x=150,y=60,width=250)
        
        self.l3=Label(root,text="Regd No:",borderwidth=1,relief="solid")
        self.l3.place(x=10,y=100,width=120)
        
        self.e2=Entry(root)
        self.e2.place(x=150,y=100,width=150)
        
        self.l4=Label(root,text="Hostel Name,Roll No:",borderwidth=1,relief="solid")
        self.l4.place(x=10,y=140,width=120)
        
        self.e3=Entry(root)
        self.e3.place(x=150,y=140,width=250)
        
        self.l5=Label(root,text="Problem Description:",borderwidth=1,relief="solid")
        self.l5.place(x=10,y=180,width=150)
        
        self.e4=Text(root)
        self.e4.place(x=10,y=220,height=120,width=450)

        
        def clicked():
            messagebox.showinfo('Saved','Problem Details saved!')
            
        self.bn=Button(root,text="Submit",bg="DodgerBlue2",command=clicked)
        self.bn.place(x=225,y=350)
        
        self.bck_btn = Button(root, text = 'BACK', font=('Courier New', 15,'bold'), bd = 4, width= 6, command= self.back_to_home)
        self.bck_btn.place(x = 500, y = 400)
        
    def back_to_home(self):
        
        self.l1.destroy()
        self.l2.destroy()
        self.l3.destroy()
        self.l4.destroy()
        self.l5.destroy()
        self.e1.destroy()
        self.e2.destroy()
        self.e3.destroy()
        self.e4.destroy()
        self.bn.destroy()
        
        self.bck_btn.destroy()
        
        main = main_page(root)
            
        
root = Tk()
root.geometry("650x450+500+100")
root.configure(bg = 'grey')
root.title("Hostel Help Desk")
main = main_page(root)
root.mainloop()