from tkinter import *
from tkinter import ttk
from utils import pickFile


root = Tk()
root.title("Pdf to xlsx parser")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

main_window = ttk.Frame(root, padding=16)
main_window.grid()

file_upload_button = Button(
        main_window, 
        text="Upload file", 
        command=pickFile, 
        height=5, 
        width=40, 
        highlightbackground="blue", 
        highlightthickness=2.5
    )

file_upload_button.grid(row=0, column=0)


