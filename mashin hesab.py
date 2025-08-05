from tkinter import *

def add_char(char):
    entry.insert(END, char)

def clear():
    entry.delete(0, END)

def calculate():
    matn = entry.get()

    num1 = ""
    num2 = ""
    amalgar = ""
    adad=0

    i = 0
    while i < len(matn):
        ch = matn[i]
        if (ch == "+" or ch == "-" or ch == "*" or ch == "/") and adad == 0:
            amalgar = ch
            adad = 1
        elif adad == 0:
            num1 = num1 + ch
        else:
            num2 = num2 + ch
        i = i + 1

    if num1 != "" and num2 != "" and amalgar != "":
        a = float(num1)
        b = float(num2)

        if amalgar == "+":
            result = a + b
        elif amalgar == "-":
            result = a - b
        elif amalgar == "*":
            result = a * b
        elif amalgar == "/":
            if b == 0:
                result = "errore"
            else:
                result = a / b
        else:
            result = "errore"
    else:
        result = "errore"

    entry.delete(0, END)
    entry.insert(0, str(result))


window = Tk()
window.title("mashin hesab")
window.geometry("240x330")


entry = Entry(window, font=20)
entry.place(x=10, y=10, width=220, height=40)


Button(window, text="7", width=5, command=lambda: add_char("7")).place(x=10, y=60)
Button(window, text="8", width=5, command=lambda: add_char("8")).place(x=70, y=60)
Button(window, text="9", width=5, command=lambda: add_char("9")).place(x=130, y=60)

Button(window, text="4", width=5, command=lambda: add_char("4")).place(x=10, y=110)
Button(window, text="5", width=5, command=lambda: add_char("5")).place(x=70, y=110)
Button(window, text="6", width=5, command=lambda: add_char("6")).place(x=130, y=110)

Button(window, text="1", width=5, command=lambda: add_char("1")).place(x=10, y=160)
Button(window, text="2", width=5, command=lambda: add_char("2")).place(x=70, y=160)
Button(window, text="3", width=5, command=lambda: add_char("3")).place(x=130, y=160)

Button(window, text="0", width=5, command=lambda: add_char("0")).place(x=10, y=210)
Button(window, text="+", width=5, command=lambda: add_char("+")).place(x=190, y=60)
Button(window, text="-", width=5, command=lambda: add_char("-")).place(x=190, y=110)
Button(window, text="*", width=5, command=lambda: add_char("*")).place(x=190, y=160)
Button(window, text="/", width=5, command=lambda: add_char("/")).place(x=190, y=210)

Button(window, text="=", width=5, command=calculate).place(x=70, y=210)
Button(window, text="clear", width=5, command=clear).place(x=130, y=210)


window.mainloop()