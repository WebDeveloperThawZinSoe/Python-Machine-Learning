#logical_operator
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img1 = cv.imread("images/tzs1.jpeg")
    img2 = cv.imread("images/tzs2.jpg")

    # Ensure both images have the same shape by resizing img2 to match img1's dimensions
    img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))

    img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

    img3 = cv.bitwise_not(img1)
    img4 = cv.bitwise_or(img1, img2)
    img5 = cv.bitwise_and(img1, img2)
    img6 = cv.bitwise_xor(img1, img2)

    images = [img3, img4, img5, img6]
    titles = ["Image1 (NOT)", "Image1 OR Image2", "Image1 AND Image2", "Image1 XOR Image2"]

    for i in range(len(images)):
        plt.subplot(2, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

if __name__ == "__main__":
    main()
