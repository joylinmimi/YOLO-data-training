from xml.etree import ElementTree as et
import os
for filename in os.listdir('./'):
	if filename.endswith(".xml"):
		tree = et.parse(filename)
		filename2=filename.split("/",-1)[0]
		#print(filename2)
		filename3=filename2.split(".", 1)[0]+".JPG"
		#print(filename3)
		tree.find('path').text = '../AUG_IMG_DIR/'+filename3
		#tree.find('filename').text = filename
		#print()
		tree.write(filename)
		continue
	else:
		continue
		