from tkinter import *

# Open Window
window = Tk()


def km_to_grams():
    grams = float(main_value.get())*1000
    e1.configure(text='%g' % grams)

def km_to_pounds():
    pounds = float(main_value.get())*2.20462
    e2.configure(text='%g' % pounds)

def km_to_ounces():
    ounces = float(main_value.get())*35.274
    e3.configure(text='%g' % ounces)


b1 = Button(window,text="Convert",command=lambda:[km_to_grams(),km_to_pounds(),km_to_ounces()])
b1.grid(row=0,column=0)

main_value = StringVar()
main_entry = Entry(window,textvariable=main_value,width=10)
main_entry.grid(row=0,column=1)

t0 = Label(text="Kg")
t0.grid(row=0,column=2)


# Kg to Grams
e1 = Label(window,width=10)
e1.grid(row=1,column=1)

t1 = Label(text="Grams")
t1.grid(row=1,column=2)

# Kg to Pounds
e2 = Label(window,width=10)
e2.grid(row=2,column=1)

t2 = Label(text="Pounds")
t2.grid(row=2,column=2)

# Kg to Ounces
e3 = Label(window,width=10)
e3.grid(row=3,column=1)

t3 = Label(text="Ounces")
t3.grid(row=3,column=2)


# Main Window Loop
window.title("Kilograms to Grams,Pounds and Ounces")
window.mainloop()