import cv2 as cv

def main():
    img1 = cv.imread("images/tzs1.jpeg")
    img2 = cv.imread("images/tzs2.jpg")

    img0 = cv.resize(img1, None, fx=1.0, fy=1.0, interpolation=cv.INTER_LINEAR)
    img2 = cv.resize(img1, None, fx=1.0, fy=1.5, interpolation=cv.INTER_CUBIC)
    img3 = cv.resize(img1, None, fx=1.5, fy=1.0, interpolation=cv.INTER_AREA)
    img4 = cv.resize(img1, None, fx=0.5, fy=1.0, interpolation=cv.INTER_NEAREST)
    
    cv.imshow("Image0", img0)
    cv.imshow("Image2", img2)
    cv.imshow("Image3", img3)
    cv.imshow("Image4", img4)

    cv.waitKey(0)  # Wait for a key event (infinite wait)

    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
