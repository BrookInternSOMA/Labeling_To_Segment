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

	xlength = int(label_split[1])
	ylength = int(label_split[2])
	plus = xlength / 110 #border 을 넣기 위해 

	xmin = int(label_split[4])
	ymin = int(label_split[5])
	xmax = int(label_split[6])
	ymax = int(label_split[7])
	
	sig = True
	numsig = 0

	xmm = xmax - xmin
	ymm = ymax - ymin
	div = ymm/xmm

	incount = 0

	for width in range(xmin,xmax):
		numsig = numsig + 1
		incount = incount + 1

		if numsig > plus:
				sig = not sig
				numsig = 0

		for height in range(ymin,ymax):
			
			if height - ymin < div * incount:
				#if :
				img[height,width]=[255,0,0]
				continue
			img[height,width]=[0,255,0]


	cv.imwrite(RESULT_DIR+name,img)
	#cv.imshow('show',img)
	#cv.waitKey(0)
