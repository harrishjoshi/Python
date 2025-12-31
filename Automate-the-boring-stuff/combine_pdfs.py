#! python3

# combine_pdfs.py - Combines all the PDFs in the working directory into
# into a single PDF.

import os

import PyPDF2

# Get all the PDF filenames.
pdf_files = []
for filename in os.listdir("files"):
    if filename.endswith(".pdf"):
        pdf_files.append(filename)

pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfWriter()

# Loop through all the PDF files.
for filename in pdf_files:
    pdf_file_obj = open(f"files/{filename}", "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

    # Loop through all the pages (except the first) and add them.
    for page_no in range(1, len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_no]
        pdf_writer.add_page(page_obj)

# Save the resulting PDF to a file.
pdf_output = open("files/allminutes.pdf", "wb")
pdf_writer.write(pdf_output)
pdf_output.close()
