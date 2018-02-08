import os
from PyPDF2 import PdfFileReader, PdfFileMerger
files_dir = os.getcwd()
all_files = list()

#input the file name 
file_1 = raw_input("enter the file name to be merged")



#input the second file name 
file_2 = raw_input("enter the second file name")

file1_det = [f for f in os.listdir(files_dir) if file_1 in f and 'pdf' in f]
all_files.extend(file1_det)


file2_det = sorted([f for f in os.listdir(files_dir) if file_2 in f and 'pdf' in f])
all_files.extend(file2_det)



# Merge the files
merger = PdfFileMerger()
for f in all_files:
	merger.append(PdfFileReader(f), 'rb')

newfile = raw_input("enter the name of the new file required")
newfilename = newfile + '.pdf'

#merger.write('mergedNew.pdf')
merger.write(newfilename)