import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	img = cv2.flip(img, 1) 
	x=350
	y=50
	h=250
	w=250
	cv2.rectangle( img, (x,y) , (x+w,y+h) ,(255,0,0),2)

	gray = cv2.cvtColor(img[y:y+h,x:x+w], cv2.COLOR_BGR2GRAY)
	_,gray = cv2.threshold(gray,210,255,cv2.THRESH_BINARY)
	_,gray2 = cv2.threshold(gray,210,255,cv2.THRESH_BINARY_INV)
	gray3 = cv2.flip(gray,1)
	gray4 = cv2.flip(gray2,1)
	#gray = cv2.Canny(gray,100,200)
	cv2.imshow('gray',gray)
	cv2.imshow('img',img)
	gray = cv2.resize(gray,(50,50))
	gray2 = cv2.resize(gray2,(50,50))
	gray3 = cv2.resize(gray3,(50,50))
	gray4 = cv2.resize(gray4,(50,50))
	
	k = cv2.waitKey(30) & 0xff
	if k==27:
		break;
	elif k!=255:	
		path = os.path.join("img/", str(k))
		if not os.path.exists(path):
			os.mkdir(path)
		if len(os.listdir(path))<1598:
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+1)+".jpg"
			cv2.imwrite(filename, gray)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+2)+".jpg"
			cv2.imwrite(filename, gray)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+3)+".jpg"
			cv2.imwrite(filename, gray)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+4)+".jpg"
			cv2.imwrite(filename, gray)

			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+401)+".jpg"
			cv2.imwrite(filename, gray2)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+402)+".jpg"
			cv2.imwrite(filename, gray2)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+403)+".jpg"
			cv2.imwrite(filename, gray2)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+404)+".jpg"
			cv2.imwrite(filename, gray2)

			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+801)+".jpg"
			cv2.imwrite(filename, gray3)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+802)+".jpg"
			cv2.imwrite(filename, gray3)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+803)+".jpg"
			cv2.imwrite(filename, gray3)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+804)+".jpg"
			cv2.imwrite(filename, gray3)

			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+1201)+".jpg"
			cv2.imwrite(filename, gray4)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+1202)+".jpg"
			cv2.imwrite(filename, gray4)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+1203)+".jpg"
			cv2.imwrite(filename, gray4)
			filename = "img/"+str(k)+"/"+str(int(len(os.listdir(path))/4)+1204)+".jpg"
			cv2.imwrite(filename, gray4)
		print(len(os.listdir(path)))
	
	
	
cap.release()
cv2.destroyAllWindows()