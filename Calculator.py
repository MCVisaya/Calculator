# A simple calculator created using python's tkinter module
# @author Marco Visaya
# @vesion naive version

#region (imports)
from tkinter import Frame, Tk,Button,Label,StringVar,NSEW, Widget
from tkinter.constants import CENTER, END, N, W
from tkinter.font import Font
from time import sleep 
#endregion
#calculator app using tkinter

#region (MainView Configuration)
root  = Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(width=False,height=False)
root.configure(background="#fcf8e8")

root.grid_columnconfigure(0,weight =1)
root.grid_columnconfigure(1,weight =1)
root.grid_columnconfigure(2,weight =1)
root.grid_columnconfigure(3,weight =1)
root.grid_rowconfigure(0,weight =1)
root.grid_rowconfigure(1,weight =1)
root.grid_rowconfigure(2,weight =1)
root.grid_rowconfigure(3,weight =1)
root.grid_rowconfigure(4,weight =1)
root.grid_rowconfigure(5,weight =1)
#endregion

#region (styles)
result_font = Font(size=45,family="Calibri")
result_font_small = Font(size=25,family="Calibri")
equation_font = Font(size=13,family="Calibri Light")
button_font = Font(size=12,family="Calibri")
symbol_font = Font(size=13,family="Calibri")
btn_num_color = "#fdfaf6"
#endregion

#region (result frame)
resultFrame = Frame(root,background="#fdfbf1")
resultFrame.grid(row=0,column=0,columnspan=4,padx=0,pady=8,sticky="NSEW")

resultFrame.grid_columnconfigure(0,weight = 1)
resultFrame.grid_rowconfigure(0,weight = 1)
resultFrame.grid_rowconfigure(1,weight = 1)

equation = StringVar()
lbl_equation =Label(resultFrame,borderwidth=0,justify='right',bg="#fdfbf1",font=equation_font,textvariable=equation,anchor='se')
lbl_equation.grid(row=0,column=0,sticky="SEW",padx=10)

result = StringVar()
result.set("0")
lbl_screen =Label(resultFrame,borderwidth=0,justify='right',bg="#fdfbf1",font=result_font,textvariable=result,anchor='se')
lbl_screen.grid(row=1,column=0,sticky="NEW",padx=10)
#endregion

#region (global variables)
previous = None
isresult = False
previous_key = "0"
ignore = False
#endregion

#region (functions)
def insertNum(num):
    global isresult
    if result.get() == "0":
        result.set("")
    elif isresult:
        result.set("")
        isresult = False
    result.set(result.get() + str(num))

def check_number_overflow():
    global ignore
    # print(resultFrame.winfo_geometry())
    if len(result.get()) > 9:
        lbl_screen.configure(font=result_font_small,pady=16)
        if len(result.get()) > 16:
            ignore=True
    else:
        if len(result.get()) <= 16:
            ignore=False
        lbl_screen.configure(font=result_font,pady=0)

def event_handler(event="",key=""):
    global previous_key,operator,ignore
    if key == "Delete":
        clear()
        previous_key = key
        return
    elif key =="BackSpace":
        result.set(result.get()[0:len(result.get())-1]) if (len(result.get())>1) else result.set(0)
    check_number_overflow()
    if event in '0123456789':
        if ignore and previous_key.isnumeric():
            return
        previous_key = event
        insertNum(event)
    elif event in '+-*/':
        if previous_key in '+-*/':
            operator = event
            equation.set(equation.get()[0:len(equation.get())-1] + event)
            return
        elif previous_key.isnumeric():
            equals()
        operation(event)
        previous_key = event
    elif event == '=' or key == "Return":
        previous_key = event
        equals()
    elif event == ".":
        include_decimal()
    else:
        print(key)
    
def clear():
    global previous,isresult,operator
    result.set("0")
    previous = None
    equation.set("")
    check_number_overflow()
    
def equals():
    global previous,isresult,operator
    if previous is None:
        return
    equation.set(str(round(float(previous)) if float(previous)%1==0 else previous)+ " " + operator+ " "+result.get()+" =")
    if operator == "+":
            result.set(float(previous) + float(result.get()))
    elif operator == "-":
            result.set(float(previous) - float(result.get()))
    elif operator == "*":
            result.set(float(previous) * float(result.get()))
    elif operator == "/":
            result.set(float(previous) / float(result.get()))
    elif operator == "^":
            result.set(float(previous) ** float(result.get()))
    previous = None
    checkoutput()
    check_number_overflow()

def operation(opt):
    print("operation")
    global previous,isresult,operator
    operator = opt
    if previous is None:
        previous = result.get()
        result.set("0")
        equation.set(previous+" "+operator)
    checkoutput()
          
def checkoutput():
    if float(result.get())%1 == 0:
        result.set(round(float(result.get())))

def clicked_event(key_char,key):
    if key_char == "+":
        btn_plus.configure(background="#fdfaf6")
        root.update_idletasks()
        sleep(0.1)
        btn_plus.configure(background="#e1f1dd")
    elif key_char == "-":
        btn_minus.configure(background="#fdfaf6")
        root.update_idletasks()
        sleep(0.1)
        btn_minus.configure(background="#e1f1dd")
    elif key_char == "*":
        btn_multiply.configure(background="#fdfaf6")
        root.update_idletasks()
        sleep(0.1)
        btn_multiply.configure(background="#e1f1dd")
    elif key_char == "/":
        btn_divide.configure(background="#fdfaf6")
        root.update_idletasks()
        sleep(0.1)
        btn_divide.configure(background="#e1f1dd")
    elif key_char == ".":
        btn_decimal.configure(background="#fdfaf6")
        root.update_idletasks()
        sleep(0.1)
        btn_decimal.configure(background="#e1f1dd")
    elif key == "BackSpace":
        btn_backspace.configure(background="#fdfaf6")
        btn_backspace.configure(foreground="black")
        root.update_idletasks()
        sleep(0.1)
        btn_backspace.configure(background="#a2b29f")
        btn_backspace.configure(foreground="#e1f1dd")
    elif key == "Delete":
        btn_clear.configure(background="#fdfaf6")
        root.update_idletasks()
        sleep(0.1)
        btn_clear.configure(background="#e1f1dd")
    elif key_char == "=" or key == "Return":
        btn_equals.configure(background="#fdfaf6")
        btn_equals.configure(foreground="black")
        root.update_idletasks()
        sleep(0.1)
        btn_equals.configure(background="#a2b29f")
        btn_equals.configure(foreground="#e1f1dd")
    elif key_char == "^":
        btn_divide.configure(background="#fdfaf6")
        root.update_idletasks()
        sleep(0.1)
        btn_divide.configure(background="#e1f1dd")
    elif key_char.isnumeric():
        buttons[int(key_char)].configure(background="#f6e6cb")
        root.update_idletasks()
        sleep(0.1)
        buttons[int(key_char)].configure(background=btn_num_color)

def change_sign():
    if float(result.get()) == 0:
        return
    else:
        result.set(float(result.get())*-1)
        checkoutput()

def include_decimal():
    if "." in result.get():
        return
    else:
        result.set(result.get()+".")
#endregion

#region (buttons creation)
btn_1 = Button(root,text="1",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event="1"),font=button_font,activebackground="#f6e6cb")
btn_2 = Button(root,text="2",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event="2"),font=button_font,activebackground="#f6e6cb")
btn_3 = Button(root,text="3",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event="3"),font=button_font,activebackground="#f6e6cb")
btn_4 = Button(root,text="4",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event="4"),font=button_font,activebackground="#f6e6cb")
btn_5 = Button(root,text="5",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event="5"),font=button_font,activebackground="#f6e6cb")
btn_6 = Button(root,text="6",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event="6"),font=button_font,activebackground="#f6e6cb")
btn_7 = Button(root,text="7",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event='7'),font=button_font,activebackground="#f6e6cb")
btn_8 = Button(root,text="8",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event='8'),font=button_font,activebackground="#f6e6cb")
btn_9 = Button(root,text="9",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event='9'),font=button_font,activebackground="#f6e6cb")
btn_0 = Button(root,text="0",borderwidth=0,bg=btn_num_color,command=lambda: event_handler(event='0'),font=button_font,activebackground="#f6e6cb")

btn_clear = Button(root,text="clr",borderwidth=0,bg="#e1f1dd",command=lambda: event_handler(key="Delete"),font=button_font,activebackground="#fdfaf6")
btn_plus = Button(root,text="+",borderwidth=0,bg="#e1f1dd",command=lambda: operation("+"),font=symbol_font,activebackground="#fdfaf6")
btn_minus = Button(root,text="-",borderwidth=0,bg="#e1f1dd",command=lambda: operation("-"),font=symbol_font,activebackground="#fdfaf6")
btn_multiply = Button(root,text="x",borderwidth=0,bg="#e1f1dd",command=lambda: operation("*"),font=symbol_font,activebackground="#fdfaf6")
btn_divide = Button(root,text="÷",borderwidth=0,bg="#e1f1dd",command=lambda: operation("/"),font=symbol_font,activebackground="#fdfaf6")
btn_equals = Button(root,text="=",borderwidth=0,bg="#a2b29f",foreground="#fcf8e8",command=equals,font=symbol_font,activebackground="#fdfaf6")

btn_decimal = Button(root,text=".",borderwidth=0,bg="#e1f1dd",font=symbol_font,activebackground="#fdfaf6",command=include_decimal)
btn_sign = Button(root,text="+/-",borderwidth=0,bg="#e1f1dd",font=button_font,activebackground="#fdfaf6",command=change_sign)
btn_backspace = Button(root,text="del",borderwidth=0,bg="#a2b29f",font=button_font,foreground="#fcf8e8",activebackground="#fdfaf6",command=lambda:event_handler("","BackSpace"))
btn_exponent = Button(root,text="xʸ",borderwidth=0,bg="#e1f1dd",font=button_font,activebackground="#fdfaf6",command=lambda:operation("^"))
#endregion

buttons = [btn_0,btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9]

#region (keybindings)
root.bind('<Key>',lambda event: event_handler(event.char,event.keysym))
root.bind('<Key>',lambda e: clicked_event(e.char,e.keysym),add="+" )
#endregion

#region (buttons assigned to grid)
btn_sign.grid(row=1,column=0,sticky="NSEW",padx=3,pady=3)
btn_exponent.grid(row=1,column=1,sticky="NSEW",padx=3,pady=3)
btn_clear.grid(row=1,column=2,sticky="NSEW",padx=3,pady=3)
btn_backspace.grid(row=1,column=3,sticky="NSEW",padx=3,pady=3)

btn_7.grid(row=2,column=0,sticky="NSEW",padx=3,pady=3)
btn_8.grid(row=2,column=1,sticky="NSEW",padx=3,pady=3)
btn_9.grid(row=2,column=2,sticky="NSEW",padx=3,pady=3)
btn_multiply.grid(row=2,column=3,sticky="NSEW",padx=3,pady=3)

btn_4.grid(row=3,column=0,sticky="NSEW",padx=3,pady=3)
btn_5.grid(row=3,column=1,sticky="NSEW",padx=3,pady=3)
btn_6.grid(row=3,column=2,sticky="NSEW",padx=3,pady=3)
btn_minus.grid(row=3,column=3,sticky="NSEW",padx=3,pady=3)

btn_1.grid(row=4,column=0,sticky="NSEW",padx=3,pady=3)
btn_2.grid(row=4,column=1,sticky="NSEW",padx=3,pady=3)
btn_3.grid(row=4,column=2,sticky="NSEW",padx=3,pady=3)
btn_plus.grid(row=4,column=3,sticky="NSEW",padx=3,pady=3)

btn_decimal.grid(row=5,column=0,sticky="NSEW",padx=3,pady=3)
btn_0.grid(row=5,column=1,sticky="NSEW",padx=3,pady=3)
btn_divide.grid(row=5,column=2,sticky="NSEW",padx=3,pady=3)
btn_equals.grid(row=5,column=3,sticky="NSEW",padx=3,pady=3)
#endregion

root.mainloop()