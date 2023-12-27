from tkinter import Frame, Tk, ttk

from ui.widgets import Builder
from utils.parser import Parser


root: Tk = Tk()
root.title("Pdf to xlsx parser")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

main_window: Frame = ttk.Frame(root, padding=16)
main_window.grid()

Builder().button(main_window, "Upload", Parser.pick_file, 5, 40, "blue", 2.5).build()
