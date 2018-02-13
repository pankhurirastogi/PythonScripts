import PyPDF2


file_1 = raw_input("enter the file name to be rotated")

pdf_in = open(file_1, 'rb')
angle = input("enter the angle by which to be rotated")
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()
 

page = pdf_reader.getPage(0)
page.rotateClockwise(angle)
pdf_writer.addPage(page)

newfile = raw_input("enter the new file name ")
 
pdf_out = open(newfile, 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()