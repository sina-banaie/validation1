from tkinter import *
from validation import*


phone_list=[]
total_list=[]
def click_submit():
    total_amaliat={quantity.get()*price.get()}
    phone = {"price":price.get(),"quntity":quantity.get(),"name":name.get()}
    #total={"price":price.get(),"quntity":quantity.get()}
    total_list.append(total_amaliat)


    phone_list.append(phone)
    print(phone_list)
    name.set("")
    quantity.set(0)
    price.set(0)
    total.set(total_amaliat)
    print("total=",total_list)



window = Tk()

window.title("phone")
window.geometry("600x600")




Label(window,text="price",fg="blue").place(x=50,y=150)

price = IntVar()
Entry(window, textvariable=price,fg="blue").place(x=110,y=150)


Label(window,text="quantity",fg="blue").place(x=50,y=110)
quantity = IntVar()
Entry(window, textvariable=quantity,fg="blue").place(x=110,y=110)

Label(window, text="name",fg="blue").place(x=50,y=70)
name = StringVar()
Entry(window, textvariable=name,fg="blue").place(x=110,y=70)

Label(window,text="total",fg="blue").place(x=50,y=220)
total = IntVar()
Entry(window, textvariable=total,fg="blue").place(x=110,y=220)



#Label(window,text="total").place(x=110,y=180)
#total = quantity.get()*price.get()

#Entry(window, textvariable=total).place(x=140,y=180)


Button(window, text="submit",width=10,command=click_submit,fg="green").place(x=180,y=250)

















window.mainloop()