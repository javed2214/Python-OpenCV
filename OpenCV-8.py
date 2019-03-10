# Program to Convert BGR Image into GrayScale Image

import cv2

imgPath = "C:\\Users\\hp\\Desktop\\Python-OpenCV\\Dataset\\Lena.jpg"
img = cv2.imread(imgPath)
cv2.imshow("Orignal Image", img)

cv2.waitKey(0)

grayScaleImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image", grayScaleImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Another Way to Convert into GrayScale Image
# img = cv2.imread(imgPath, 0)
