
import cv2

img_path = "C:\\Users\\JavedAnsari\\Desktop\\Images\\Lena.png"
img = cv2.imread(img_path)

r_1 = cv2.resize(img,(200,200))
r_2 = cv2.resize(img,(100,200))
r_3 = cv2.resize(img,(200,500))
r_4 = cv2.resize(img,(600,250))

cv2.imshow('Lena 1', r_1)
cv2.imshow('Lena 2', r_2)
cv2.imshow('Lena 3', r_3)
cv2.imshow('Lena 4', r_4)

cv2.waitKey(5000)
cv2.destroyAllWindows()