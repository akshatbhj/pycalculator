import tkinter
from tkinter import *

BLACK_BG = "#17161b"
BUTTON_BG = "#3697f5"
BUTTON_BG_2 = "#2a2d36"
WHITE = "#ffffff"
ORANGE = "#fe9037"
DEFAULT_FONT = "Arial"

root = Tk()
root.title("Pycalculator")
root.geometry("570x600")
root.resizable(False, False)
root.config(
    background=BLACK_BG,
)

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except Exception:
            result = "error"
            equation = ""
    label_result.config(text=result)


label_result = Label(root, width=25, height=2, text="", font=(DEFAULT_FONT, 30))
label_result.pack()


# First Row

Button(
    root,
    text="C",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG,
    fg=WHITE,
    command=lambda: clear(),
).place(x=10, y=100)

Button(
    root,
    text="/",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("/"),
).place(x=150, y=100)

Button(
    root,
    text="%",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("%"),
).place(x=290, y=100)

Button(
    root,
    text="*",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("*"),
).place(x=430, y=100)


# Second Row

Button(
    root,
    text="7",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("7"),
).place(x=10, y=200)

Button(
    root,
    text="8",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("8"),
).place(x=150, y=200)

Button(
    root,
    text="9",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("9"),
).place(x=290, y=200)

Button(
    root,
    text="-",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("-"),
).place(x=430, y=200)

# Third Row

Button(
    root,
    text="4",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("4"),
).place(x=10, y=300)

Button(
    root,
    text="5",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("5"),
).place(x=150, y=300)

Button(
    root,
    text="6",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("6"),
).place(x=290, y=300)

Button(
    root,
    text="+",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("+"),
).place(x=430, y=300)

# Fourth Row

Button(
    root,
    text="1",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("1"),
).place(x=10, y=400)

Button(
    root,
    text="2",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("2"),
).place(x=150, y=400)

Button(
    root,
    text="3",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("3"),
).place(x=290, y=400)

Button(
    root,
    text="0",
    width=11,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("0"),
).place(x=10, y=500)

Button(
    root,
    text=".",
    width=5,
    height=1,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=BUTTON_BG_2,
    fg=WHITE,
    command=lambda: show("."),
).place(x=290, y=500)

Button(
    root,
    text="=",
    width=5,
    height=3,
    font=(DEFAULT_FONT, 30, "bold"),
    bd=1,
    bg=ORANGE,
    fg=WHITE,
    command=lambda: calculate(),
).place(x=430, y=400)

root.mainloop()
