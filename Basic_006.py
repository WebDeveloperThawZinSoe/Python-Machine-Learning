import cv2 as cv
import matplotlib.pyplot as pty 

def main():
    img = cv.imread("images/tzs1.jpeg",0)
    pty.imshow(img)
    pty.show()
    pty.imshow(img,cmap="gray")
    # pty.show()
    pty.title("MatPlotLib")
    pty.xticks([])
    pty.yticks([])
    pty.show()

if __name__ == "__main__":
    main()