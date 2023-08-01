from tkinter import filedialog
from PyPDF2 import PdfReader
from openpyxl import *


def pickFile():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select a file",
        filetypes=(
            ("pdf files", "*.pdf"),
            ("docx files", "*.docx"),
            ("odt files", "*.odt")
        )
    )

    if file_path:
        print(file_path)
        excelParser(file_path)


def excelParser(file_path):
    pdf_reader = PdfReader(file_path)
    text = ''''''

    for page in pdf_reader.pages:
        text += page.extract_text()

    lines = text.split('\n')

    data = []

    for line in lines:
        data.append(line.split())

    workbook = Workbook()
    worksheet = workbook.active

    for row in data:
        worksheet.append(row)

    output_excel_file = "converted_file.xlsx"

    workbook.save(output_excel_file)
