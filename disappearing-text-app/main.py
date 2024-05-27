from tkinter import *

BG1 = "#E3FEF7"
BG2 = "#FEFAF6"
PADX = 50
PADY = 10
FONT = ("Courier", 10, "bold")

class TextDisappear:

    def __init__(self):
        self.window = Tk()
        self.window.title("Disappearing Text Application")
        self.window.geometry("900x700")
        self.window.config(bg=BG1)

        self.intro_label = Label(text="Type below..", font=FONT, bg=BG1)
        self.intro_label.grid(row=0, column=1, columnspan=2, pady=PADY, padx=PADX)

        self.writing_input = Text(width=80, height=20, bg=BG2)
        self.writing_input.grid(row=1, column=1, pady=PADY, padx=PADX)
        self.writing_input.bind("<KeyRelease>", self.reset_timer)

        self.caution_label = Label(text="The Most Dangerous Writing App. Don't stop writing, " 
                                      "or all progress will be lost after 5 seconds of no input.", 
                                      font=FONT, wraplength=800, fg="red", bg=BG1)
        self.caution_label.grid(row=2, column=1, columnspan=2, pady=PADY, padx=PADX)

        self.timer_label = Label(text="Timer: 5", font=FONT, wraplength=800, fg="red", bg=BG1)
        self.timer_label.grid(row=5, column=1, columnspan=2, pady=PADY, padx=PADX)

        self.text = Label(text="Designed By Wiredu Clement ®", fg="lightgrey", bg=BG1)
        self.text.grid(row=6, column=1, columnspan=2, pady=PADY, padx=PADX)

        self.timer_id = None
        self.time_left = 5
        self.window.bind("<KeyPress>", self.reset_timer)

        self.window.mainloop()

    def start_timer(self):
        self.time_left = 5
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Timer: {self.time_left}")
            self.time_left -= 1
            self.timer_id = self.window.after(1000, self.update_timer)
        else:
            self.make_text_disappear()

    def reset_timer(self, event):
        if self.timer_id:
            self.window.after_cancel(self.timer_id) 
        self.start_timer()

    def make_text_disappear(self):
        self.timer_label.config(text="Your Text Has Been Deleted!")
        self.writing_input.delete(1.0, END)


if __name__ == "__main__":
    TextDisappear()