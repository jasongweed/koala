import os
from os import listdir
from os.path import isfile, join

imgdir = os.path.join(os.getcwd(),"images_shareable_toDollas/") #path to image filesos.rename(f,r'')

fileList = [f for f in listdir(imgdir) if isfile(join(imgdir, f))]
print(fileList)
for f in fileList:
	os.rename(join(imgdir, f),join(imgdir,"$".join(f.split("#"))))