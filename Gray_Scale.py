# GrayScale and Negative Image

import cv2

img_path = "C:\\Users\\JavedAnsari\\Desktop\\Images\\Lena.png"
img = cv2.imread(img_path)
cv2.imshow('Lena', img)

gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
neg = cv2.bitwise_not(img)

cv2.imshow('Grayscale', gs)
cv2.imshow('Negative', neg)

cv2.waitKey(0)
cv2.destroyAllWindows()