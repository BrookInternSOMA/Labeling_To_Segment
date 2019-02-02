import os
import cv2 as cv




'''

4,5,6,7 번이 xmin,ymin,xmax,ymax
'''

FILENAME = "label.txt"
DIR = "original_img/"
RESULT_DIR = "result_img/"

Flabel = open(FILENAME,'r')
label_list = Flabel.readlines()

print(label_list)
print(len(label_list))
count = 0

for label_row in label_list:
	count=count+1
	if count == 1:
		continue
	
	#if count == 3: #for test
	#	break

	label_split = label_row.split(',')
	print(label_split)

	name = label_split[0]
	img_name = DIR + label_split[0]
	print(img_name)
	img = cv.imread(img_name)
	print(img)

	xmin = int(label_split[4])
	ymin = int(label_split[5])
	xmax = int(label_split[6])
	ymax = int(label_split[7])
	
	for width in range(xmin,xmax):
		for height in range(ymin,ymax):
			img[height,width]=[255,255,255]

	cv.imwrite(RESULT_DIR+name,img)
	#cv.imshow('show',img)
	#cv.waitKey(0)
