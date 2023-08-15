import tkinter
from tkinter import *

BLACK_BG = "#17161b"
BUTTON_BG = "#3697f5"
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

root.mainloop()
