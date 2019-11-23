from tkinter import *

root = Tk()

calc = 0.0
math_op = ''

root.title("Calculator")
root.geometry("200x225")
root.resizable(width=False, height=False)


def num_btn_click(value):
    global calc
    if value != 'AC':
        var = inp.get() + value
        inp.delete(0, "end")
        inp.insert(0, var)
    else:
        inp.delete(0, "end")
        calc = 0.0


def math_btn_click(value):
    global calc
    global math_op
    try:
        if value != '=':
            calc = float(inp.get())
            print("cals is", calc)
            inp.delete(0, "end")

        if value == '+':
            math_op = '+'
        elif value == '-':
            math_op = '-'
        elif value == '*':
            math_op = '*'
        elif value == '/':
            math_op = '/'
        elif value == '=':
            print("value1:", calc, "value2:", inp.get())
            if math_op == '+':
                ans = calc + float(inp.get())
            elif math_op == '-':
                ans = calc - float(inp.get())
            elif math_op == '*':
                ans = calc * float(inp.get())
            elif math_op == '/':
                ans = calc / float(inp.get())
            inp.delete(0, "end")
            if math_op != '':
                inp.insert(0, str(ans))

    except ValueError:
        print("wrong value", "calc=", calc, "mathop=", math_op)
        inp.delete(0, "end")


inp = Entry(width="32")
inp.grid(row=0, columnspan=4, padx=2, pady=2)

btn7 = Button(root, height=2, width=5, text="7", command=lambda: num_btn_click('7'))
btn7.grid(row=2, column=0, padx=2, pady=5)
btn8 = Button(root, height=2, width=5, text="8", command=lambda: num_btn_click('8'))
btn8.grid(row=2, column=1, padx=2, pady=5)
btn9 = Button(root, height=2, width=5, text="9", command=lambda: num_btn_click('9'))
btn9.grid(row=2, column=2, padx=2, pady=5)
btndiv = Button(root, height=2, width=5, text="/", command=lambda: math_btn_click('/'))
btndiv.grid(row=2, column=3, padx=2, pady=5)

btn4 = Button(root, height=2, width=5, text="4", command=lambda: num_btn_click('4'))
btn4.grid(row=3, column=0, padx=2, pady=5)
btn5 = Button(root, height=2, width=5, text="5", command=lambda: num_btn_click('5'))
btn5.grid(row=3, column=1, padx=2, pady=5)
btn6 = Button(root, height=2, width=5, text="6", command=lambda: num_btn_click('6'))
btn6.grid(row=3, column=2, padx=2, pady=5)
btnmul = Button(root, height=2, width=5, text="*", command=lambda: math_btn_click('*'))
btnmul.grid(row=3, column=3, padx=2, pady=5)

btn1 = Button(root, height=2, width=5, text="1", command=lambda: num_btn_click('1'))
btn1.grid(row=4, column=0, padx=2, pady=5)
btn2 = Button(root, height=2, width=5, text="2", command=lambda: num_btn_click('2'))
btn2.grid(row=4, column=1, padx=2, pady=5)
btn3 = Button(root, height=2, width=5, text="3", command=lambda: num_btn_click('3'))
btn3.grid(row=4, column=2, padx=2, pady=5)
btnsub = Button(root, height=2, width=5, text="-", command=lambda: math_btn_click('-'))
btnsub.grid(row=4, column=3, padx=2, pady=5)

btnAc = Button(root, height=2, width=5, text="AC", command=lambda: num_btn_click('AC'))
btnAc.grid(row=5, column=0, padx=2, pady=5)
btn0 = Button(root, height=2, width=5, text="0", command=lambda: num_btn_click('0'))
btn0.grid(row=5, column=1, padx=2, pady=5)
btnequal = Button(root, height=2, width=5, text="=", command=lambda: math_btn_click('='))
btnequal.grid(row=5, column=2, padx=2, pady=5)
btnplus = Button(root, height=2, width=5, text="+", command=lambda: math_btn_click('+'))
btnplus.grid(row=5, column=3, padx=2, pady=5)

root.mainloop()
