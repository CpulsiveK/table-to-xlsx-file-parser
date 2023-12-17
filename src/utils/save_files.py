import os
from pathlib import Path

from openpyxl import Workbook


def save_output_file(directory: str, workbook: Workbook, filename) -> None:
    system_platform = os.name

    if (system_platform == "nt"):
        workbook.save(Path(os.path.expanduser('~')) / directory / filename)
    elif (system_platform == "posix"):
        workbook.save(Path(os.path.expanduser('~')) / directory / filename)
    else:
        raise NotImplementedError("Unsupported platform")
