import cv2 as cv
import numpy as np

drawing = False 
mode = True
(ix,iy) = (-1,-1)
window = "Lesson 5 - Drawing "
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow(window)

def MyMouseEvent(event,x,y,flags,params):
    global drawing , mode , ix , iy
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True 
        (ix , iy) = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)
            else:
                cv.circle(img,(x,y),30,(0,255,0),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False


cv.setMouseCallback(window,MyMouseEvent)

def main():
    global mode , drawing
    while True:
        cv.imshow(window,img)
        if cv.waitKey(1) == ord("m") or cv.waitKey(1) == ord("M"):
            mode = not mode
        elif cv.waitKey(1) == 27:
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()