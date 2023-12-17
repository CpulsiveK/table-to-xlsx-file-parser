from tkinter import filedialog
from openpyxl import *
from utils.excel_parser import excelParser


def pickFile():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select a file",
        filetypes=(
            ("pdf files", "*.pdf"),
        )
    )

    if file_path:
        excelParser(file_path)
