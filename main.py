import tkinter
from tkinter import *

BLACK_BG = "#17161b"
BUTTON_BG = "#3697f5"
BUTTON_BG_2 = "#2a2d36"
WHITE = "#ffffff"
DEFAULT_FONT = "Arial"

root = Tk()
root.title("Pycalculator")
root.geometry("570x600")
root.resizable(False, False)
root.config(
    background=BLACK_BG,
)

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
).place(x=430, y=300)

root.mainloop()
