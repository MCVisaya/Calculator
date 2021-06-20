# A simple calculator created using python's tkinter module
# @author Marco Visaya
# @vesion 6/19/2021

#region - Imports
from tkinter import *
from time import sleep
from tkinter import font
from tkinter.font import Font
#endregion

#region - Root Configuration
root = Tk()
root.title("Calculator")
root.geometry("320x450")
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

bg_active = "#e5e8e4"
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
    event_clicked_feedback(key) if not isMouseClick else None
    if key.isnumeric():
        if result.get() == "0":
            result.set("")
        result.set(result.get()+key)
    elif key == "Delete":
        result.set("0")
    elif key == "BackSpace":
        result.set(result.get()[0:len(result.get())-1]) if (len(result.get())>1) else result.set("0")
    elif key in "Return,Equal":
        pass

def event_clicked_feedback(key: str) -> None:
    print(key)
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

btn_backspace = Button(root, text="del", borderwidth=0, bg=bg_btns_dark, font=font_btns, foreground=fg_btns_light, 
                command= lambda: event_handler("BackSpace",True), activebackground= bg_btns_dark_clicked, activeforeground=fg_btns_light)
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

#endregion

root.mainloop()