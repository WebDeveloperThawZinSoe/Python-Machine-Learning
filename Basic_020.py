#RotationImage
import cv2  as cv
import numpy as np
import matplotlib.pyplot as pt

def main():
    img = cv.imread("images/tzs2.jpg")
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    row , col , ch = img.shape
    R = cv.getRotationMatrix2D((col/2,row/2),45,0.7)
    output = cv.warpAffine(img,R,(col,row))
    pt.imshow(output)
    pt.title("Rotation")
    pt.show()

if __name__ == "__main__":
    main()