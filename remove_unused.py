import os
import shutil, sys  
dir='C:\\Users\\USER\\Desktop\\data20181226 - 複製\\data\\img'
for filename in os.listdir(dir):
	if filename.endswith(".txt"):
		filename2=os.path.splitext(filename)[0]
		f = open(filename,"r")
		f2 = open(filename2+'-2.txt',"w")
		for line in f:
			print(line[0])
			if line[0]=='4':
				f2.write(line)
		f.close()	
		f2.close()
		shutil.move(os.path.join(dir, filename2+'-2.txt'), os.path.join(dir, filename))
