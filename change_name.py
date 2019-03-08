import os
import shutil, sys  
dir='C:\\Users\\USER\\Desktop\\data20181226 - 複製\\more_samples\\'
for filename in os.listdir(dir):
	if filename.endswith(".txt" ):
		new_name=str(filename.split("_", 2)[0]+'_'+filename.split("_", 2)[1]+".txt")
		print(filename, new_name)
		os.rename(dir+filename, dir+new_name)

for filename2 in os.listdir(dir):
	if filename2.endswith(".JPG" ):
		new_name2=str(filename2.split("_", 2)[0]+'_'+filename2.split("_", 2)[1]+".JPG")
		print(filename2, new_name2)
		os.rename(dir+filename2, dir+new_name2)