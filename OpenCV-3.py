# Program to Print Image Matrix Using OpenCV

import cv2

imgpath = "C:\\Users\\hp\\Desktop\\Python-OpenCV\\Dataset\\Lena.jpg"
img = cv2.imread(imgpath)

print(img)  # Print Image
print(img.shape)  # Print Shape
print(img.ndim)   # Print Dimenssion
print(type(img))  # Print Type of Image

cv2.imshow('Lena',img)

cv2.waitKey(0)
cv2.destroyAllWindows()