import os
from os import listdir
from os.path import isfile, join

imgdir = os.path.join(os.getcwd(),"images_shareable/") #path to image files

class Imageinfo:
	def __init__(self,_filename):
		self.filename=_filename
		#print("filename: ",self.filename)
		self.title = self.extractTitle()
		self.hint= self.extractHint()
		self.cat = self.extractCat()
		self.erroneous_filename=False
		self.print()

	def extractTitle(self):
		return self.filename.split("_",1)[0].split("$")[0].replace("$","%23") #%23 is hashtag for html or url

	def extractCat(self):
		_cat=""
		try:
			filename_after_initial_underscore=self.filename.split("_",1)[1]
			#print("trying to parse: ",filename_after_initial_underscore)
			if("infl" in filename_after_initial_underscore):
				_cat+="infl"
			if("infx" in filename_after_initial_underscore):
				_cat+="infx"
			if("neo" in filename_after_initial_underscore):
				_cat+="neo"
			if("gene" in filename_after_initial_underscore):
				_cat+="gene"
			if("other" in filename_after_initial_underscore):
				_cat+="other"
			if("hn" in filename_after_initial_underscore):
				_cat+="hn"
			print("_cat:",self.cat)
		except:
			#self._cat=""
			self.erroneous_filename=True
		#print("\n category: ",_cat,"\n")
		return _cat

	def extractHint(self):
		_hint=""
		try:
			_hint=self.filename.split("$")[1]
			#print("self.hint: ",self.hint)
		except:
			_hint="No hint"
		return _hint

	def print(self):
		print("\nfilename: ",self.filename, "\ntitle: ", self.title, "\ncat: ", self.cat, "\nhint: ", self.hint, "\n")

	def getRepresentationalString(self):
		return "[\""+self.filename+"\",\""+self.title+"\",\""+self.cat+"\",\""+self.hint+"\"],\n"

#get list of files in image directory as Imageinfo objects
filesInfoList = [Imageinfo(f) for f in listdir(imgdir) if isfile(join(imgdir, f))]

for f in filesInfoList:
	print(f.getRepresentationalString())


#Part 2: create .js file using information gathered for each file 
#remove any existing version within target folder
try:
	os.remove("img_data.js")
except:
	print("no previous img_data.js found, no file deleted")

js_file = open("img_data.js", "w")
js_file.write("image_data_array = [ \n")
for file_info in [f.getRepresentationalString() for f in filesInfoList]:
	js_file.write(file_info)
	print(file_info)
js_file.write("\n ];")



'''


#arrays, strings
representational_strings_for_js_array = []
f_list = [] #file list
diag_list=[] #diagnosis list
cats_list=[] #categories list
hints_list=[]
imgdir = os.path.join(os.getcwd(),"images/") #path to image files


#get list of files in image directory
f_list = [f for f in listdir(imgdir) if isfile(join(imgdir, f))]

#next loop is to make array where each entry is [img_filename, diagnosis, "category"]
#for ease of use, will use f_list, diag_list, cats_list as separate arrays

for x in range(len(f_list)):
	try:
		#extract diagnosis from first part of filename
		#preceding initial underscore
		diag_list.append(f_list[x].split("_",1)[0]) #get all text prior to intial underscore as diagnosis
		print("split (_ 1): ", f_list[x].split("_",1))
		#extract categories by searching for key strings
		cats_list.append("")
		filename_after_initial_underscore=f_list[x].split("_",1)[1]
		#try:
		if("inflam" in filename_after_initial_underscore):
			cats_list[x]+=("inflam")
		if("infx" in filename_after_initial_underscore):
			cats_list[x]+=("infx")
		if("neo" in filename_after_initial_underscore):
			cats_list[x]+=("neo")
		if("gene" in filename_after_initial_underscore):
			cats_list[x]+=("gene")
		if("other" in filename_after_initial_underscore):
			cats_list[x]+=("other")
		else:
			print("no cats found")

		#extract hints by getting middle string between hashtags
		hints_list.append("")#append blank string even if no hint present so question info in arrays are at matching indices
		hint=f_list[x].split("$")[1]
		try:
			hints_list[-1]=hint #place the newly detected hint in hint array
		except:
			print("no acceptable hint found")
		print("hint for ", f_list, " is: ", hint)

		print("new,\n file:", f_list[x], ", \n diag:", diag_list[x], ", \n cats:", cats_list[x], " \n hint:", hints_list[x])
		representational_strings_for_js_array.append("[\""+f_list[x]+"\",\""+diag_list[x]+"\",\""+cats_list[x]+"\"],\""+hints_list[x]+"\"],\n")
		#print(representational_strings_for_js_array[x])
	except:
		print("error processing file ",x)

#Part 2: create .js file using information gathered for each file 
#remove any existing version within target folder
try:
	os.remove("img_data.js")
except:
	print("no previous img_data.js found, no file deleted")

js_file = open("img_data.js", "w")
js_file.write("image_data_array = [ \n")
for file_info in representational_strings_for_js_array:
	js_file.write(file_info)
	print(file_info)
js_file.write("\n ];")

'''
