import os
import shutil, sys  
import copy
from lxml.etree import Element, SubElement, tostring, ElementTree
import cv2
template_file = 'C:\\Users\\USER\\Desktop\\data_augmentation\\anno.xml'
dir='C:\\Users\\USER\\Desktop\\data_augmentation\\'
for filename in os.listdir(dir):
	if filename.endswith(".txt"):
		filename2=os.path.splitext(filename)[0]
		#f = open(filename,"r")
		
		with open(filename) as f:
			print(filename)
			trainfiles = f.readlines()  # 标注数据 格式(filename label x_min y_min x_max y_max)
 
		file_names = []
		tree = ElementTree()
 
		for line in trainfiles:
			trainFile = line.split()
			file_name = filename2+'.jpg'
			#print(file_name)
		 
			# 如果没有重复，则顺利进行。这给的数据集一张图片的多个框没有写在一起。
			if file_name not in file_names:
				file_names.append(file_name)
				lable = trainFile[0]
				xmin = trainFile[1]
				ymin = trainFile[2]
				xmax = trainFile[3]
				ymax = trainFile[4]
		 
				tree.parse(template_file)
				root = tree.getroot()
				root.find('filename').text = file_name
		 
				# size
				sz = root.find('size')
				im = cv2.imread(dir+'\\' + file_name)#读取图片信息
				print((dir +'\\'+ file_name),im)
		 
				sz.find('height').text = str(im.shape[0])
				sz.find('width').text = str(im.shape[1])
				sz.find('depth').text = str(im.shape[2])
		 
				# object 因为我的数据集都只有一个框
				obj = root.find('object')
		 
				obj.find('name').text = lable
				bb = obj.find('bndbox')
				bb.find('xmin').text = xmin
				bb.find('ymin').text = ymin
				bb.find('xmax').text = xmax
				bb.find('ymax').text = ymax
				# 如果重复，则需要添加object框
			else:
				lable = trainFile[0]
				xmin = trainFile[1]
				ymin = trainFile[2]
				xmax = trainFile[3]
				ymax = trainFile[4]
		 
				xml_file = file_name.replace('jpg', 'xml')
				tree.parse(dir + xml_file)#如果已经重复
				root = tree.getroot()
		 
				obj_ori = root.find('object')
		 
				obj = copy.deepcopy(obj_ori)  # 注意这里深拷贝
		 
				obj.find('name').text = lable
				bb = obj.find('bndbox')
				bb.find('xmin').text = xmin
				bb.find('ymin').text = ymin
				bb.find('xmax').text = xmax
				bb.find('ymax').text = ymax
				root.append(obj)
		 
			xml_file = file_name.replace('jpg', 'xml')
			tree.write(dir + xml_file, encoding='utf-8')
