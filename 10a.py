from PyPDF2 import PdfWriter, PdfReader

num = int(input("Enter no of pages you want to combine from different pdfs: "))
pdf1 = open("D:\coverzz_python raghav.pdf",'rb')
pdf2 = open("D:\coverzz_python udit.pdf",'rb')


pdf_writer = PdfWriter()
pdf1_reader = PdfReader(pdf1)
page = pdf1_reader.pages[num-1]
pdf_writer.add_page(page)

pdf2_reader = PdfReader(pdf2)
page = pdf2_reader.pages[num-1]
pdf_writer.add_page(page)

with open('output.pdf','wb') as output:
    pdf_writer.write(output)


