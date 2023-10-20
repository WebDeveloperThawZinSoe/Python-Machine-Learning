##NegativeImage
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img1 = cv.imread("images/tzs1.jpeg")
    img2 = cv.imread("images/tzs2.jpg")

    img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

    img3 = 255 - img1
    img4 = 255 - img2

    images = [img1,img2,img3,img4]
    title = ["Image1","Image2","Image3","Image4"]


    for i in range(len(images)):
        plt.subplot(2,2,1+i)
        plt.imshow(images[i])
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])


    plt.show()

if __name__ == "__main__":
    main()