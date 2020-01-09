# Edge Detection

import cv2

img_path = "C:\\Users\\JavedAnsari\\Desktop\\Images\\qq.png"
img = cv2.imread(img_path)
cv2.imshow('Lena', img)

edges = cv2.Canny(img, 100, 200)
cv2.imshow("Edge Detected Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()