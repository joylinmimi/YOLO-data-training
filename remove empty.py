import os
import shutil, sys  
dir='C:\\Users\\USER\\Desktop\\data20181226 - 複製\\data\\img'
for filename in os.listdir(dir):
	if filename.endswith(".txt"):
		size=os.stat(filename).st_size
		print(size, filename)
		if size==0:
			os.remove(filename)
			os.remove(os.path.splitext(filename)[0]+".jpg")
		
