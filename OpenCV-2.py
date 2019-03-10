# Program to Open an Image in GrayScale Mode Using OpenCV

import cv2

imgpath = "C:\\Users\\hp\\Desktop\\Python-OpenCV\\Dataset\\Lena.jpg"
img = cv2.imread(imgpath, 0)

cv2.imshow('Lena',img)

cv2.waitKey(0)
cv2.destroyAllWindows()