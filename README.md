## table-to-xlsx-file-parser
This repository contains a python application that takes a pdf with table content and converts it to an excel file.


## Prerequisites
Clone the repository.
Before running the tool make sure the below python libraries are installed
1. [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/)
2. [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

Run the commands below in your terminal to install the above libraries
```bash
pip install PyPDF2
```
```bash
pip install openpyxl
```

NB:
For better result make sure each pdf file contains a single table as having multiple tables in one file will have all the contents of it parsed to one excel worksheet.
Only pdf files are supported for now.


## How to use the tool
To run the tool navigate to the ```src``` directory in your cloned repository and run:
```bash
python main.py
```

A GUI window will open in a minimized state, double tap on the title bar to maximize it. To parse a pdf, click on the button in the middle of the screen with a description ```Upload file``` as show below.
![Screenshot from 2023-08-01 16-11-20](https://github.com/CpulsiveK/table-to-xlsx-file-parser/assets/78286658/b7c125de-2136-4193-9abc-73ed49e7d321)

A dialogue box will pop allowing you to navigate your directory to select the pdf you want to parse.
![Screenshot from 2023-08-01 16-15-58](https://github.com/CpulsiveK/table-to-xlsx-file-parser/assets/78286658/490ab9fd-1790-4c80-96cd-15175fc613af)

After selecting a file you will be navigated back to the main window, this means the parsing process is complete. To view the output file navigate to the ```src``` directory in the cloned repository and you should see the output file with name ```converted_file.xlsx``` as shown.
![Screenshot from 2023-08-01 16-22-47](https://github.com/CpulsiveK/table-to-xlsx-file-parser/assets/78286658/e92927d2-3fd8-4d01-856d-1e85fd557ea9)
