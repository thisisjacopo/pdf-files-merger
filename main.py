import PyPDF2
import os

merger = PyPDF2.PdfMerger()
directory = './pdfs'

for file in os.listdir(directory):
    if file.endswith('.pdf'):
        merger.append(f'{directory}/{file}')
    merger.write('merged.pdf')
    