import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 

def main():
    img = cv.imread("images/tzs2.jpg")
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Normal")
    plt.xticks([])
    plt.yticks([])


    plt.subplot(1, 2, 2)
    plt.hist(img.ravel(),256,[0,255])
    plt.title("Histogram")
    plt.xlim(xmin=0,xmax=256)
    plt.show()

if __name__ == "__main__":
    main()