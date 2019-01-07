from xml.etree import ElementTree as et
import os
for filename in os.listdir('C:\\Users\\joy\\Desktop\\xml'):
	if filename.endswith(".xml"):
		tree = et.parse(filename)
		tree.find('path').text = 'C:\\USER\\Desktop\\302_000_crhg.JPG'
		tree.write(filename)
		continue
	else:
		continue
		