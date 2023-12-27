import os
from pathlib import Path
from tkinter import filedialog

from PyPDF2 import PdfReader
from openpyxl import Workbook


class Parser:
    @staticmethod
    def pick_file() -> None:
        file_path: str = filedialog.askopenfilename(
            initialdir=Path.home(),
            title="Select a file",
            filetypes=(
                ("pdf files", "*.pdf"),
            )
        )

        if file_path:
            Parser()._excel_parser(file_path)

    def _excel_parser(self, file_path: str) -> None:
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

        self._save_output_file("Documents", workbook, output_excel_file)

    def _save_output_file(self, directory: str, workbook: Workbook, filename: str) -> None:
        system_platform: str = os.name

        if (system_platform == "nt"):
            workbook.save(Path.home() / directory / filename)
        elif (system_platform == "posix"):
            workbook.save(Path.home() / directory / filename)
        else:
            raise NotImplementedError("Unsupported platform")
