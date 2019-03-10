# Program to Capture Image from WebCam Using OpenCV

import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if(cap.isOpened()):
    ret, frame = cap.read()
    print(ret)
    print(frame)

else:
    ret = False

img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.title("Camera Image")
plt.xticks([])
plt.yticks([])
plt.show()

cap.release()