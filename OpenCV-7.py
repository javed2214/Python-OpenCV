# OpenCV BGR Palette with TrackBars

def emptyFunction(n):
    pass

import cv2
import numpy

img = numpy.zeros((512, 512, 3), numpy.uint8)
windowName = "OpenCV BGR Color Palette"
cv2.namedWindow(windowName)

cv2.createTrackbar('B', windowName, 0, 255, emptyFunction)
cv2.createTrackbar('G', windowName, 0, 255, emptyFunction)
cv2.createTrackbar('R', windowName, 0, 255, emptyFunction)

while(True):

    cv2.imshow(windowName, img)

    if(cv2.waitKey(1)==27):     # Escape ASCII Value
        break

    blue = cv2.getTrackbarPos('B', windowName)
    green = cv2.getTrackbarPos('G', windowName)
    red = cv2.getTrackbarPos('R', windowName)

    print(blue, green, red)

    img[:] = [blue, green, red]

cv2.destroyAllWindows()
