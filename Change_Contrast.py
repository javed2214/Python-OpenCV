# GrayScale and Negative Image

import cv2

img_path = "C:\\Users\\JavedAnsari\\Desktop\\Images\\Lena.png"
img = cv2.imread(img_path)
cv2.imshow('Lena', img)

a = 2    # Contrast control (1.0-3.0)
b = 0    # Brightness control (0-100)

adjusted = cv2.convertScaleAbs(img, alpha = a, beta = b)

cv2.imshow('Contrast Image', adjusted)

cv2.waitKey(5000)
cv2.destroyAllWindows()