from customtkinter import*
from PIL import Image,ImageDraw,ImageFont
from tkinter import messagebox
import tkinter as tk
from customtkinter import CTk

#
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All fields required')
    elif usernameEntry.get()=='Deezy' and passwordEntry.get()=='1234':
        messagebox.showinfo('Succes', 'Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Wrong Username or password!')


root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')
image= CTkImage(Image.open('back2.jpg'),size=(930,478))
imageLabel=CTkLabel(root,
                    image=image,
                    text='GSU Library\nEmployee Management System',
                    font=('Amaze Script', 24, 'bold'), text_color='#EDAA1E')
imageLabel.place(x=0, y=0)


# headinglabel1 = CTkLabel(root, text='GSU Library', font=('Amaze Script', 24, 'bold'), fg_color=None)
# headinglabel1.place(x=390, y=150)

# headinglabel=CTkLabel(root,text='Employee Management System', font=('COPPER', 24, 'bold'))
# headinglabel.place(x=285, y=200)

usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username')
usernameEntry.place(x=385, y=280)

passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password', show='*')
passwordEntry.place(x=385, y=330)

loginButton=CTkButton(root, text='Login', cursor='hand2', command=login)
loginButton.place(x=385, y=380)

root.mainloop()


