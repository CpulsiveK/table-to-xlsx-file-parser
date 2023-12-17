from tkinter import filedialog
from PyPDF2 import PdfReader
from openpyxl import *

from utils.save_files import save_output_file


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

    save_output_file("Documents", workbook, output_excel_file)
