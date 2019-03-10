# Program to Convert GrayScale into Binary Image
# Pure Black and White Image is Called Binary Image

import cv2

imgPath = "C:\\Users\\hp\\Desktop\\Python-OpenCV\\Dataset\\Lena.jpg"
img = cv2.imread(imgPath, 0)
cv2.imshow("GrayScale Image", img)

cv2.waitKey(0)

ret, binImage = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# Value Below 100 is Set to Black and Above 100 is Set to White
cv2.imshow("Binary Image", binImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
