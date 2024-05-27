from tkinter import *
import random
import threading
import time

BGCOLOR = '#EEF7FF'

class TypeSpeed:

    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Application")
        self.window.config(padx=50, pady=50, bg=BGCOLOR)

        self.intro = Label(self.window, text="(Increase your Typing Speed & Accuracy.)", font=("Verdana", 10), bg=BGCOLOR)
        self.intro.grid(row=0, column=1)

        self.texts = open("path/to/your/data.txt", "r").read().split("\n")

        self.sample_label = Label(text=random.choice(self.texts), font=("Arial", 15), height=10, width=50, wraplength=550)
        self.sample_label.grid(row=1, column=0, columnspan=3, pady=50)

        self.input_entry = Entry(width=60, font=("Arial", 15))
        self.input_entry.grid(row=2, column=1, pady=50)
        self.input_entry.bind("<KeyRelease>", self.check_input)

        self.button = Button(text="Re-generate text", command=lambda: self.generate_text())
        self.button.grid(row=3, column=1)

        self.speed_label = Label(text="Speed range\nWords per sec: 0.00 \nCharacters per min: 0.00 \nWords per min: 0.00", 
                                 font=("Verdana", 10), bg=BGCOLOR)
        self.speed_label.grid(row=4, column=1, pady=20)

        self.counter = 0
        self.running = False

        self.window.mainloop()
        
    def generate_text(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed range\nWords per sec: 0.00 \nCharacters per min: 0.00 \nWords per min: 0.00")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, END)

    def check_input(self, event):
        if not self.running:
            if event.keycode not in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            char = self.input_entry.get()
            wps = len(char) / self.counter
            cpm = (len(char) / self.counter) * 60
            wpm = (len(char.split()) / self.counter) * 60
            self.speed_label.config(text=f"Speed range\nWords per sec: {wps:.2f} \nCharacters per min: {cpm:.2f} \nWords per min: {wpm:.2f}")


if __name__ == "__main__":     
    TypeSpeed()