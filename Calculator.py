# A simple calculator created using python's tkinter module
# @author Marco Visaya
# @vesion 6/25/2021

#region - Imports
from tkinter import *
from time import sleep
from tkinter.font import Font
#endregion

#region - Root Configuration
root = Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False,False)
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

#region - Global Variables
equation = StringVar()
result = StringVar()
result.set("0")

previous_key = None
previous_value = None
previous_operator = None
operand2 = None

operators_key = {"plus":"+","minus":"-","asterisk":"x","x":"x","slash":"÷","asciicircum":"^"}
symbols_key = {"period":"."}
#endregion

#region - Styles
font_screen = Font(size=45,family="Calibri")
font_screen_small = Font(size=25,family="Calibri")
font_equation = Font(size=13,family="Calibri Light")
font_btns = Font(size=12,family="Calibri")
font_btns_symbols = Font(size=13,family="Calibri")

bg_frame_result = "#fdfbf1"
bg_btns_num = "#fdfaf6"
bg_btns_light = "#e1f1dd"
bg_btns_dark = "#a2b29f"
bg_btns_dark_clicked = "#c3ccc2"

fg_btns_dark = "#212430"
fg_btns_light = "#f4fbe6"

bg_active = "#f0f0f0"
#endregion

#region - Result Frame Configuration
resultFrame = Frame(root,background=bg_frame_result)
resultFrame.grid(row=0,column=0,columnspan=4,padx=0,pady=8,sticky="NSEW")

resultFrame.grid_columnconfigure(0,weight = 1)
resultFrame.grid_rowconfigure(0,weight = 1)
resultFrame.grid_rowconfigure(1,weight = 1)

lbl_equation =Label(resultFrame, borderwidth=0, justify='right', bg="#fdfbf1", font=font_equation, textvariable=equation, anchor='se')
lbl_equation.grid(row=0,column=0,sticky="SEW",padx=10)

lbl_screen =Label(resultFrame, borderwidth=0, justify='right', bg="#fdfbf1",font=font_screen, textvariable=result, anchor='se')
lbl_screen.grid(row=1,column=0,sticky="NEW",padx=10)
#endregion

#region - Functions

def event_handler(key: str, isMouseClick: bool = False) -> None:
    global previous_key, previous_value, previous_operator, operand2
    event_clicked_feedback(key) if not isMouseClick else None

    screen_overflow()

    if key == "Delete":
        clear()
        return

    if key == "BackSpace":
        if (len(result.get())>1) and result.get().isnumeric():
            result.set(result.get()[0:len(result.get())-1])        
        else:
            result.set("0")
        return

    if key.isnumeric():
        if len(result.get().replace(",","")) > 15:
            return
        if result.get() == "0":
            result.set("")
        result.set(result.get()+key)
        format_result()

    elif key in "Return,Equal":
        if previous_value is not None:
            if previous_key in "Return,Equal":
                previous_value = result.get()

                equation.set(result.get()+" "+operators_key[previous_operator]+" "+operand2+" = ")
                solve(previous_operator,operand2)
                return
            else:
                equation.set(previous_value+" "+operators_key[previous_operator]+" "+result.get()+" = ")
                solve(previous_operator)
            
    elif key.lower() in operators_key :
        if previous_key.lower() in operators_key:
            previous_key = key
            previous_operator = key
            equation.set(equation.get().replace(equation.get()[-1],operators_key[previous_key]))
            return
        if previous_value is not None and previous_key.isnumeric():
            solve(previous_operator)    
        previous_value = result.get()
        result.set("0")
        screen_overflow()
        equation.set(previous_value+" "+operators_key[key])
        previous_operator = key

    elif key == "period":
        if symbols_key[key] not in result.get():
            result.set(result.get()+symbols_key[key])
        else:
            return

    elif key == "sign":
        None if result.get()=="0" else result.set(float(result.get()) * -1), format_result()
        
    else:
        print(key)
        
    previous_key = key 
    
def solve(operator: str, continuous:str = None) -> None:
    global previous_value, operand2

    result.set(result.get().replace(",",""))
    previous_value = previous_value.replace(",","")
    if continuous is not None:
        result.set(continuous)

    operand2 = result.get()

    if operator == "plus":
        result.set((float(previous_value) + float(result.get())))
    elif operator == "minus":
        result.set(float(previous_value) - float(result.get()))
    elif operator.lower() in ["asterisk","x"]:
        result.set(float(previous_value) * float(result.get()))
    elif operator == "slash":
        result.set(float(previous_value) / float(result.get()))
    elif operator == "^" or operator == "asciicircum":
        result.set(float(previous_value) ** float(result.get()))

    format_result()

def format_result() -> None:
    result.set(result.get().replace(",",""))
    if float(result.get())%1 == 0:
        result.set(result.get().removesuffix(".0"))
    if (float(result.get()) > 999) or (float(result.get()) < 999):
        for i in range(len(str(int(result.get())))-3,0,-3):
            temp = list(result.get())
            temp.insert(i,",")
            result.set("".join(temp)) 
    screen_overflow()

def screen_overflow() -> None:
    if len(result.get()) > 9:
        lbl_screen.configure(font=font_screen_small)
        lbl_screen.grid_configure(pady=(0,18))
        lbl_equation.grid_configure(pady=(14,0))
        # root.geometry("{}x450".format(root.winfo_width() + 20))
    else:
        lbl_screen.configure(font=font_screen)
        lbl_screen.grid_configure(pady=(0,0))
        lbl_equation.grid_configure(pady=(0,0))

def clear() -> None:
    global previous_value
    result.set("0")
    equation.set("")
    previous_value = None

    screen_overflow()


def event_clicked_feedback(key: str) -> None:
    def visual_feedback(button: Button) -> None:
        if key.lower() in "backspace,equal,return":
            button.configure(background = bg_btns_dark_clicked, relief = "sunken")
            root.update()
            sleep(0.1)
            button.configure(background = bg_btns_dark, relief = "raised")
            return
        button.configure(background = bg_active, relief = "sunken")
        root.update()
        sleep(0.1)
        if key.isnumeric():
            button.configure(background = bg_btns_num, relief = "raised")
        else:
            button.configure(background = bg_btns_light, relief = "raised")

    if key.isnumeric():
        visual_feedback(btns_num[int(key)])
    elif key == "BackSpace":
        visual_feedback(btn_backspace)
    elif key == "Delete":
        visual_feedback(btn_clear)
    elif key.lower() in "return,equal":
        visual_feedback(btn_equals)
    else:
        visual_feedback(btn_plus) if key=="plus" else None
        visual_feedback(btn_minus) if key=="minus" else None
        visual_feedback(btn_multiply) if key=="asterisk" else None
        visual_feedback(btn_divide) if key=="slash" else None
        visual_feedback(btn_exponent) if key=="asciicircum" else None
        visual_feedback(btn_decimal) if key=="period" else None
        visual_feedback(btn_sign) if key=="sign" else None

#endregion

#region - Buttons
btns_num = []

for i in range(10):
    btns_num.append(Button(root, background=bg_btns_num, font= font_btns, borderwidth=0, text=str(i), foreground=fg_btns_dark))

btn_plus = Button(root, text="+", borderwidth=0, bg=bg_btns_light, font=font_btns_symbols, foreground=fg_btns_dark)
btn_minus = Button(root, text="-", borderwidth=0, bg=bg_btns_light, font=font_btns_symbols, foreground=fg_btns_dark)
btn_multiply = Button(root, text="x", borderwidth=0, bg=bg_btns_light, font=font_btns_symbols, foreground=fg_btns_dark)
btn_divide = Button(root, text="÷", borderwidth=0, bg=bg_btns_light, font=font_btns_symbols, foreground=fg_btns_dark)

btn_clear = Button(root, text="clr", borderwidth=0, bg=bg_btns_light, font=font_btns, foreground=fg_btns_dark)
btn_decimal = Button(root, text=".", borderwidth=0, bg=bg_btns_light, font=font_btns_symbols, foreground=fg_btns_dark)
btn_sign = Button(root, text="+/-", borderwidth=0, bg=bg_btns_light, font=font_btns_symbols, foreground=fg_btns_dark)
btn_exponent = Button(root, text="xʸ", borderwidth=0, bg=bg_btns_light,font=font_btns_symbols, foreground=fg_btns_dark)

btn_backspace = Button(root, text="del", borderwidth=0, bg=bg_btns_dark, font=font_btns, foreground=fg_btns_light)
btn_equals = Button(root, text="=", borderwidth=0, bg=bg_btns_dark, font=font_btns_symbols, foreground=fg_btns_light)

#grid assignment
btn_sign.grid(row=1,column=0,sticky="NSEW",padx=3,pady=3)
btn_exponent.grid(row=1,column=1,sticky="NSEW",padx=3,pady=3)
btn_clear.grid(row=1,column=2,sticky="NSEW",padx=3,pady=3)
btn_backspace.grid(row=1,column=3,sticky="NSEW",padx=3,pady=3)

btns_num[7].grid(row=2,column=0,sticky="NSEW",padx=3,pady=3)
btns_num[8].grid(row=2,column=1,sticky="NSEW",padx=3,pady=3)
btns_num[9].grid(row=2,column=2,sticky="NSEW",padx=3,pady=3)
btn_multiply.grid(row=2,column=3,sticky="NSEW",padx=3,pady=3)

btns_num[4].grid(row=3,column=0,sticky="NSEW",padx=3,pady=3)
btns_num[5].grid(row=3,column=1,sticky="NSEW",padx=3,pady=3)
btns_num[6].grid(row=3,column=2,sticky="NSEW",padx=3,pady=3)
btn_minus.grid(row=3,column=3,sticky="NSEW",padx=3,pady=3)

btns_num[1].grid(row=4,column=0,sticky="NSEW",padx=3,pady=3)
btns_num[2].grid(row=4,column=1,sticky="NSEW",padx=3,pady=3)
btns_num[3].grid(row=4,column=2,sticky="NSEW",padx=3,pady=3)
btn_plus.grid(row=4,column=3,sticky="NSEW",padx=3,pady=3)

btn_decimal.grid(row=5,column=0,sticky="NSEW",padx=3,pady=3)
btns_num[0].grid(row=5,column=1,sticky="NSEW",padx=3,pady=3)
btn_divide.grid(row=5,column=2,sticky="NSEW",padx=3,pady=3)
btn_equals.grid(row=5,column=3,sticky="NSEW",padx=3,pady=3)

#key_bindings
root.bind('<Key>',lambda event: event_handler(event.keysym))

#click_bindings
btns_num[0].configure(command = lambda: event_handler("0"))
btns_num[1].configure(command = lambda: event_handler("1"))
btns_num[2].configure(command = lambda: event_handler("2"))
btns_num[3].configure(command = lambda: event_handler("3"))
btns_num[4].configure(command = lambda: event_handler("4"))
btns_num[5].configure(command = lambda: event_handler("5"))
btns_num[6].configure(command = lambda: event_handler("6"))
btns_num[7].configure(command = lambda: event_handler("7"))
btns_num[8].configure(command = lambda: event_handler("8"))
btns_num[9].configure(command = lambda: event_handler("9"))

btn_backspace.configure(command=lambda: event_handler("BackSpace",True), activebackground= bg_btns_dark_clicked, activeforeground=fg_btns_light)
btn_equals.configure(command=lambda: event_handler("Return",True), activebackground= bg_btns_dark_clicked, activeforeground=fg_btns_light)

btn_plus.configure(command=lambda: event_handler("plus",True))
btn_minus.configure(command=lambda: event_handler("minus",True))
btn_multiply.configure(command=lambda: event_handler("asterisk",True))
btn_divide.configure(command=lambda: event_handler("slash",True))
btn_exponent.configure(command=lambda: event_handler("asciicircum",True))

btn_clear.configure(command=lambda: event_handler("Delete",True))
btn_decimal.configure(command=lambda: event_handler("period",True))
btn_sign.configure(command=lambda: event_handler("sign", True))

#endregion

root.mainloop()
