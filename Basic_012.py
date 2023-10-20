import cv2 as cv
import numpy as np
import matplotlib.pyplot as ptl

def main():
    
    img1 = cv.imread("images/tzs1.jpeg",1)
    img2 = cv.imread("images/tzs2.jpg",1)

    img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img2,cv.COLOR_BGR2RGB)

    ptl.subplot(1,2,1)
    ptl.imshow(img1)
    ptl.title("Thaw Zin Soe")
    ptl.show()
    ptl.xticks([])
    ptl.yticks([])


    ptl.subplot(1,2,1)
    ptl.imshow(img2)
    ptl.title("Thaw Zin Soe")
    ptl.show()
    ptl.xticks([])
    ptl.yticks([])


if __name__ == "__main__":
    main()