
import cv2

image_path = "C:\\Users\\JavedAnsari\\Desktop\\Lena.png"
img = cv2.imread(image_path)

x = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
y = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('RGB', x)
cv2.imshow('HSV', y)

cv2.waitKey(1000)
cv2.destroyAllWindows()