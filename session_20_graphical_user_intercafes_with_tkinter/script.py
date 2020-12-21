from tkinter import *

# Open Window
window = Tk()


def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.configure(text='%g' % miles)


b1 = Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Label(window,height=1,width=20)
t1.grid(row=0,column=2)

# Main Window Loop
window.mainloop()