import os
import filecmp
from filecmp import dircmp
#curDir = os.getcwd()
path1 = "D:/Python Scripts"
path2 = "D:/CompareFolder"
folder1 = os.path.abspath(path1)
folder2 = os.path.abspath(path2)
filesListFolder1 = os.listdir(folder1)
filesListFolder2 = os.listdir(folder2)
#for f in filesListFolder1:
#	print f
#	for j in filesListFolder2:
#		print "-----"
#		print j
#		if(filecmp.cmp(f,j)):
#			print  "sameName"
dcmp = dircmp(folder1, folder2)


print (dcmp.diff_files)

#print filesList