import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    img1 = cv.imread("images/tzs1.jpeg")
    img2 = cv.imread("images/tzs2.jpg")

    # Resize both images to the same shape
    img1 = cv.resize(img1, (img2.shape[1], img2.shape[0]))

    img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

    img3 = img1 + img2
    img4 = img1 - img2
    img4 = img1 * img2
    img5 = img1 / img2
    img6 = img1 % img2

    img7 = img1 + 50
    img8 = img1 - 50 
    img9 = img1 * 50
    img10 = img1 / 50

    images = [img1, img2, img3, img4, img5, img6,img7,img8,img9,img10]
    title = ["Image1", "Image2", "Image3", "Image4", "Image5", "Image6","Image7","Image8","Image9","Image10"]

    for i in range(len(images)):
        plt.subplot(5, 4, 1 + i)
        plt.imshow(images[i])
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

if __name__ == "__main__":
    main()
