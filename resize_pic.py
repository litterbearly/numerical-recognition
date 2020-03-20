import cv2
import os

for i in range(10):
	print(i)
    for j in range(0, 2500):
		input = cv2.imread("thresh_natural/"+str(i)+'_'+str(j+1)+'.jpg', 0)
		ret, thresh = cv2.threshold(input, 10, 255, cv2.THRESH_BINARY)
		print("thresh_natural/"+str(i)+'_'+str(j+1)+'.jpg')
        if j<1500:
		cv2.imwrite("./images/train/"+str(i)+'_'+str(j+1)+'.jpg', cv2.resize(thresh, (28,28)))
        else:
		cv2.imwrite("./images/test/"+str(i)+'_'+str(j+1)+'.jpg', cv2.resize(thresh, (28,28)))