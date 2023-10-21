import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread("images/tzs1.jpeg")
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    row , col , channel = img.shape
    T = np.float32([[1,0,50],[0,1,50]])
    output = cv.warpAffine(img,T,(col,row))
    plt.imshow(output)
    plt.title("Image")
    plt.show()

if __name__ == "__main__":
    main()