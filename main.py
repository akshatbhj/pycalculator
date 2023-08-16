import tkinter as tk

# Color Palette
BLACK_BG = "#000000"
BUTTON_BG = "#F4F4F4"
BUTTON_BG_2 = "#E0E0E0"
WHITE = "#FFFFFF"
ORANGE = "#F89F17"
DEFAULT_FONT = "Segoe UI"

root = tk.Tk()
root.title("Pycalculator")
root.geometry("350x600")
root.resizable(False, False)
root.config(background=BLACK_BG)

equation = ""


def show(value):
    global equation
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def clear_all():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation:
        try:
            result = str(eval(equation))
        except Exception:
            result = "Error"
        label_result.config(text=result)
        equation = result


def on_key(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":
        show(key)
    elif key == "\r":
        calculate()
    elif key == "\x08":
        clear()
    elif key.lower() == "c":
        clear_all()


# Result Label
label_result = tk.Label(
    root,
    width=12,
    height=2,
    text="",
    font=(DEFAULT_FONT, 24),
    anchor="e",
    background=BLACK_BG,
    foreground=WHITE,
)
label_result.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

# Button Layout
button_texts = [
    ("", 1, 0),
    ("%", 1, 1),
    ("/", 1, 2),
    ("C", 1, 3),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("*", 2, 3),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("-", 3, 3),
    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("+", 4, 3),
    ("0", 5, 0),
    (".", 5, 1),
    ("=", 5, 2, 1, 3),
]

for text, row, col, *args in button_texts:
    rowspan, colspan = args or (1, 1)
    if text == "C":
        tk.Button(
            root,
            text=text,
            width=5,
            height=2,
            font=(DEFAULT_FONT, 18),
            bd=0,
            bg=BUTTON_BG_2,
            fg=BLACK_BG,
            command=clear,
        ).grid(
            row=row,
            column=col,
            rowspan=rowspan,
            columnspan=colspan,
            padx=5,
            pady=5,
            sticky="nsew",
        )
    else:
        tk.Button(
            root,
            text=text,
            width=5,
            height=2,
            font=(DEFAULT_FONT, 18),
            bd=0,
            bg=BUTTON_BG,
            fg=BLACK_BG,
            command=lambda t=text: show(t) if t != "=" else calculate(),
        ).grid(
            row=row,
            column=col,
            rowspan=rowspan,
            columnspan=colspan,
            padx=5,
            pady=5,
            sticky="nsew",
        )

# Configure grid weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Bind keyboard events
root.bind("<Key>", on_key)

root.mainloop()
