from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os 

root = Tk()
root.title("Clement Wiredu - Custom watermarker")
root.config(padx=100, pady=70)
logo_file_path = "path/to/your/logo.png"
selected_filename = ""


def load_image(file_entry):
    global selected_filename
    filename = filedialog.askopenfilename()
    if filename:
        selected_filename = filename
        img = Image.open(filename)
        file_entry.insert(0, filename)


def add_watermark():
    global selected_filename
    if selected_filename:
        img = Image.open(selected_filename)
        text_font = ImageFont.truetype("arial.ttf", 60)
        add_text = name_entry.get()
        if add_text:
            full_text = f"© {add_text} | {datetime.now().year}"

            save_path = "C:/Users/wired/Desktop/udemy/end-projects/watermark-app/"
            base_name = "watermarked_img"
            extension = ".png"
            counter = 1
            new_filename = f"{base_name}_{counter}{extension}"
            while os.path.exists(os.path.join(save_path, new_filename)):
                counter += 1
                new_filename = f"{base_name}_{counter}{extension}"

            drawing = ImageDraw.Draw(img)
            drawing.text((700, 500), full_text, fill="whitesmoke", font=text_font)

            img.save(os.path.join(save_path, new_filename))
            name_entry.delete(0, END)
            load_entry.delete(0, END)
        else:
            messagebox.showerror(title="Error", message="Please enter text for the watermark.")
    else:
        messagebox.showerror(title="Error", message="No image selected.")
        


photo = PhotoImage(file=logo_file_path)
canvas = Canvas(width=300, height=300)
canvas.create_image(150, 150, image=photo)
canvas.grid(row=0, column=1, columnspan=2, sticky="nsew") 

load_label = Label(text="Image path: ", font=("Arial", 10))
load_label.grid(row=1, column=0, pady=10)

load_entry = Entry(width=35)
load_entry.grid(row=1, column=1)

load_button = Button(text="Load Image", width=15, command=lambda: load_image(load_entry))
load_button.grid(row=1, column=2, padx=10, pady=10)


name_label = Label(text="Your text: ", font=("Arial", 10))
name_label.grid(row=2, column=0)

name_entry = Entry(width=35)
name_entry.grid(row=2, column=1)

add_button = Button(text="Add watermark", width=15, command=add_watermark)
add_button.grid(row=2, column=2, padx=10, pady=10)


root.mainloop()