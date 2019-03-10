# Edge Detection through WebCam using OpenCV

import cv2


def sketch(img):

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    grayImgBlur = cv2.GaussianBlur(grayImg,(5,5),0)

    cannyEdge = cv2.Canny(grayImgBlur, 10, 70)

    ret, mask = cv2.threshold(cannyEdge, 70, 255, cv2.THRESH_BINARY)

    return mask



cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Live WebCam", sketch(frame))

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()