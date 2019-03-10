# Program to Resize an Image Using OpenCV

import cv2

imgpath = "C:\\Users\\hp\\Desktop\\Python-OpenCV\\Dataset\\Lena.jpg"
img = cv2.imread(imgpath)

resized = cv2.resize(img,(200,200))

cv2.imshow('Lena',resized)

cv2.waitKey(0)
cv2.destroyAllWindows()