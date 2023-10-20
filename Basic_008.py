import cv2 as cv
import numpy as np
import matplotlib.pyplot as ptl 

def main():
    cap = cv.VideoCapture(0)
    ref , frame = cap.read()
    
    if cap.isOpened():
        ref , frame = cap.read()
        print(frame)

    img = cv.cvtColor(frame,cv.COLOR_BGR2RGB)

    ptl.imshow(img)
    ptl.show()

    cap.release()

if __name__ == "__main__":
    main()