from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def reset_form():
    code.set(0)
    name.set("")
    brand.set("")
    price.set(0)
    quantity.set(0)

def select_product(event):
    table_row = table.focus()
    selected = table.item(table_row)["values"]
    code.set(selected[0])
    name.set(selected[1])
    brand.set(selected[2])
    price.set(selected[3])
    quantity.set(selected[4])

def save_click():
    product = {
        "code":code.get(),
        "name":name.get(),
        "brand":brand.get(),
        "price":price.get(),
        "quantity": quantity.get()
    }
    # Data Validation
    # Save to file/database
    messagebox.showinfo("Save", f"Successfully saved!\n{product}")
    reset_form()
    # افزودن داده ی جدید به صورت تاپل به جدول
    table.insert("", END, values=tuple(product.values()))

def edit_click():
    pass

def remove_click():
    pass


window = Tk()
window.title("Orders")
window.geometry("710x360")
window.resizable(False, False)

# Code
code = IntVar()
Label(window,text="Code").place(x=20,y=20)
Entry(window, textvariable=code).place(x=100,y=20)

# Name
name = StringVar()
Label(window,text="Name").place(x=20,y=60)
Entry(window, textvariable=name).place(x=100,y=60)

# Brand
brand = StringVar()
Label(window,text="Brand").place(x=20,y=100)
Entry(window, textvariable=brand).place(x=100,y=100)

# Price
price = IntVar()
Label(window,text="Price").place(x=20,y=140)
Entry(window, textvariable=price).place(x=100,y=140)

# Quantity
quantity = IntVar()
Label(window,text="Quantity").place(x=20,y=180)
Entry(window, textvariable=quantity).place(x=100,y=180)


Button(window, text="Save", command=save_click, width=7).place(x=20,y=300)
Button(window, text="Edit", command=save_click, width=7).place(x=95,y=300)
Button(window, text="Remove", command=save_click, width=7).place(x=170,y=300)

table = ttk.Treeview(window, height=12,columns=(1,2,3,4,5),show="headings")
table.column(1, width=70)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=80)
table.column(5, width=80)

table.heading(1, text="Code")
table.heading(2, text="Name")
table.heading(3, text="Brand")
table.heading(4, text="Price")
table.heading(5, text="Quantity")

table.bind("<<TreeviewSelect>>", select_product)

table.place(x=250, y = 60)


window.mainloop()



