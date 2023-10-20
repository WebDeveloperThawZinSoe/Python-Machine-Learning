import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
window = "Mouse Event Lesson"
cv.namedWindow(window)

def MyMouseEvent(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),40,(0,255,0),1)
    elif event == cv.EVENT_MBUTTONDBLCLK:
        cv.circle(img,(x,y),20,(255,0,0),-1)

cv.setMouseCallback(window,MyMouseEvent)

def main():
    while True :
        cv.imshow(window,img)
        if cv.waitKey(1) == 27:
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()