# Program to Save an Image in Another Format in Another Directory Using OpenCV

import cv2

imgpath = "C:\\Users\\hp\\Desktop\\Python-OpenCV\\Dataset\\Lena.jpg"
img = cv2.imread(imgpath)
cv2.imshow('Lena', img)

outpath = "C:\\Users\\hp\\Desktop\\Python-OpenCV\\Output\\Lena.png"
cv2.imwrite(outpath, img)

cv2.waitKey(0)
cv2.destroyAllWindows()