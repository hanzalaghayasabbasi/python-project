# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.


import PyPDF2

# Open the first PDF file
pdf_file1 = open('a.pdf', 'rb')

# Open the second PDF file
pdf_file2 = open('b.pdf', 'rb')


# Open the 3 PDF file
pdf_file3 = open('c.pdf', 'rb')

# Create a PDF merger
pdf_merger = PyPDF2.PdfFileMerger()

# Add the first PDF file
pdf_merger.append(pdf_file1)

# Add the second PDF file
pdf_merger.append(pdf_file2)

# Add the 3 PDF file
pdf_merger.append(pdf_file2)
# Merge the PDF files

pdf_merger.write('merged_all.pdf')

# Close the PDF files
pdf_file1.close()
pdf_file2.close()
pdf_file3.close()