from tkinter import *
from tkinter.filedialog import askopenfilename
import pyttsx3
import PyPDF2

class TextToSpeech:

    def __init__(self):
        self.window = Tk()
        self.window.title("Text-To-Speech Application")
        self.window.config(padx=30, pady=10)

        self.photo = PhotoImage(file="C:/Users/wired/Desktop/udemy/end-projects/pdf-to-audiobook/logo.png")
        self.canvas = Canvas(width=300, height=300)
        self.canvas.create_image(200, 200, image=self.photo)
        self.canvas.grid(row=0, column=2, columnspan=3, sticky="nsew")

        self.text = "Convert any pdf file or text to audio. ®"
        self.text_object = self.canvas.create_text(300, 180, text=self.text, anchor=W, width=200, font=("Arial", 12))

        self.text_entry = Text(width=80, height=15)
        self.text_entry.grid(row=1, column=1, columnspan=3, pady=10)

        self.file_btn = Button(text="Choose File", width=60, command=lambda: self.choose_file())
        self.file_btn.grid(row=2, column=2, pady=10)

        self.play_audio = Button(text="Play Audio", width=60, command=lambda: self.generate_audio())
        self.play_audio.grid(row=3, column=2, pady=10)

        self.window.mainloop()

    def choose_file(self):
        self.book = askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.book:
            pdf_text = self.extract_from_pdf()
            self.text_entry.delete(1.0, END)
            self.text_entry.insert(END, pdf_text)
            
    def generate_audio(self):
        pdf_text = self.text_entry.get(1.0, END)
        if pdf_text:
            player = pyttsx3.init()
            player.say(pdf_text)
            player.runAndWait()

    def extract_from_pdf(self):
        pdfreader = PyPDF2.PdfReader(self.book)
        pages = len(pdfreader.pages)
        extracted_text = ""
    
        for num in range(0, pages):
            page = pdfreader.pages[num]
            extracted_text += page.extract_text()

        return extracted_text.strip()


if __name__ == "__main__":
    TextToSpeech()
