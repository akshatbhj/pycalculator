import tkinter as tk

# Colors
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

# Font Style
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x567")
        self.window.wm_resizable(0, 0)
        self.window.title("PyCalcutor")

        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frames = self.create_display_frames()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1),
            8: (1, 2),
            9: (1, 3),
            4: (2, 1),
            5: (2, 2),
            6: (2, 3),
            1: (3, 1),
            2: (3, 2),
            3: (3, 3),
            0: (4, 2),
            ".": (4, 1),
        }

        self.buttons_frames = self.create_buttons_frames()
        self.create_digit_buttons()

    def create_display_labels(self):
        total_label = tk.Label(
            self.display_frames,
            text=self.total_expression,
            anchor=tk.E,
            bg=LIGHT_GRAY,
            fg=LABEL_COLOR,
            padx=24,
            font=SMALL_FONT_STYLE,
        )

        total_label.pack(expand=True, fill="both")

        label = tk.Label(
            self.display_frames,
            text=self.current_expression,
            anchor=tk.E,
            bg=LIGHT_GRAY,
            fg=LABEL_COLOR,
            padx=24,
            font=LARGE_FONT_STYLE,
        )

        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frames(
        self,
    ):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frames, text=str(digit),bg=WHITE, fg=LABEL_COLOR)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_buttons_frames(
        self,
    ):
        frame = tk.Frame(
            self.window,
        )
        frame.pack(expand=True, fill="both")
        return frame

    def run(
        self,
    ):
        self.window.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
