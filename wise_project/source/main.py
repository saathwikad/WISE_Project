from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM - HOME")
        
        self.bg_img = Image.open('bg.png')
        self.bg_img = self.bg_img.resize((500,300))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.bg_lbl = Label(root, image= self.bg_img)
        self.bg_lbl.place(x = 0 , y = 0)

        self.home_title = Label(root, text= 'WELCOME TO MY ATM', font = ('Courier New', 15, 'bold'))
        self.home_title.pack(fill = 'x')

        self.language_btn = Button(root, text = 'LANGUAGE', font=('Courier New', 15, 'bold'))
        self.language_btn.place(x= 20, y = 150)

        self.enter_pin = Button(root, text= 'ENTER PIN', font= ('Courier New', 15,'bold'),command= self.enter_pin_page)
        self.enter_pin.place(x = 300, y = 150)
    
    def enter_pin_page(self):
        self.home_title.destroy()
        self.language_btn.destroy()
        self.enter_pin.destroy()

        root = self.root
        self.enter_pin_page_title = Label(root, text= 'ENTER PIN', font=('Courier New',15,'bold'))
        self.enter_pin_page_title.pack(fill = 'x')

        self.pin_label = Label(root, text= "ENTER YOUR PIN: ", font=('Courier New', 15, 'bold'))
        self.pin_label.place(x = 50, y = 150)
        self.pin_entry = Entry(root, font=('Courier New',15,'bold'))
        self.pin_entry.place(x = 250, y = 150)

        self.submit_btn = Button(root, text='SUBMIT', font=('Courier New',15, 'bold'), bd = 4,command= self.login)
        self.submit_btn.place(x = 350, y =  200)

        self.bck_btn = Button(root, text = 'BACK', font=('Courier New', 15,'bold'), bd = 4, width= 6, command= self.back_to_home)
        self.bck_btn.place(x = 20, y = 200)

    def login(self):
        messagebox.showinfo('GOOD PIN','GOOD PIN ENTERED')
    
    def back_to_home(self):
        self.enter_pin_page_title.destroy()
        self.pin_label.destroy()
        self.pin_entry.destroy()
        self.submit_btn.destroy()
        self.bck_btn.destroy()
        home = Home(root)
        
home =Home(root)
root.geometry('500x300+550+150')
root.mainloop()
