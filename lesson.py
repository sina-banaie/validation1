from tkinter import *
from tkinter import ttk
from tkinter import messagebox

info_lessons=[]
def submit_click():
    information={
           "code":code.get(),
           "title":title.get(),
           "teacher":teacher.get(),
           "class_number":class_number.get(),
           "unit":unit.get(),
         }


    info_lessons.append(information)
    print(info_lessons)
    code.set(0)
    title.set("")
    teacher.set("")
    class_number.set(0)
    unit.set(0)
    table.insert("", END, values=tuple(information.values()))


def remove_click():
    selcted_item=table.focus()
    if not selcted_item:
        print("error")
        return
    table.delete(selcted_item)
    print("Deleted")
def edit_click():
    selected_item=table.focus()
    if not selected_item:
        print("error")
        return
    table.item(selected_item,values=(code.get,title.get,teacher.get(),class_number.get(),unit.get()))
def select_lessons(event):
    table_row=table.focus()
    if not table_row:
        return
    selected=table.item(table_row)["values"]
    code.set(selected[0])
    title.set(selected[1])
    teacher.set(selected[2])
    class_number.set(selected[3])
    unit.set(selected[4])
def search_click():
    pass



window = Tk()
window.geometry("700x500")
window.title("lessons")



#code

Label(window,text="code").place(x=20, y=40)
code=IntVar()
Entry(window,textvariable=code).place(x=70, y=40)

#title
title=StringVar()
Label(window,text="title").place(x=20, y=80)
Entry(window,textvariable=title).place(x=70, y=80)


#teacher
teacher=StringVar()
Label(window,text="teacher").place(x=20, y=120)
Entry(window,textvariable=teacher).place(x=70, y=120)


#class number
class_number=IntVar()
Label(window,text="class number").place(x=20, y=160)
Entry(window,textvariable=class_number).place(x=100, y=160)


#unit
unit=IntVar()
Label(window,text="unit").place(x=20, y=200)
Entry(window,textvariable=unit).place(x=70, y=200)

#search
search_code=IntVar()
Label(window,text="search code").place(x=300, y=5)
Entry(window,textvariable=search_code).place(x=400, y=5)

search_teacher=StringVar()
Label(window,text="search teacher").place(x=300, y=40)
Entry(window,textvariable=search_teacher).place(x=400, y=40)


Button(text="submit",command=submit_click).place(x=20, y=400)
Button(text="remove",command=remove_click).place(x=100, y=400)
Button(text="edit",command=edit_click).place(x=180, y=400)
Button(text="search",command=search_click).place(x=300, y=400)


table=ttk.Treeview(window,height=12,columns=(0,1,2,3,4),show="headings")
table.column(0, width=70)
table.column(1, width=100)
table.column(2, width=100)
table.column(3, width=80)
table.column(4, width=80)


table.heading(0,text="code")
table.heading(1,text="title")
table.heading(2,text="teacher")
table.heading(3,text="class")
table.heading(4,text="unit")

table.bind(table.bind("<<TreeviewSelect>>",select_lessons))
table.place(x=250, y=80)






























window.mainloop()
