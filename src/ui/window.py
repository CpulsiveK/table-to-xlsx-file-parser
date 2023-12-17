from tkinter import Tk, ttk

from ui.widgets import Builder
from utils.file_picker import pickFile


root: Tk = Tk()
root.title("Pdf to xlsx parser")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

main_window = ttk.Frame(root, padding=16)
main_window.grid()

ui_builder = Builder()
ui_builder.button(main_window, "Upload", pickFile, 5, 40, "blue", 2.5).build()
