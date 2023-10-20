import cv2 as cv
import numpy as np

drawing = False 
mode = True
(ix, iy) = (-1, -1)
window = "Drawing"
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow(window)

def MyMouseEvent(event, x, y, flags, params):
    global drawing, mode, ix, iy
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True 
        (ix, iy) = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(img, (x, y), 1, (0, 255, 0), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

cv.setMouseCallback(window, MyMouseEvent)

# Resize the image to 100x100 pixels
img = cv.resize(img, (1700, 800))

def main():
    global mode, drawing, img
    while True:
        cv.imshow(window, img)
        key = cv.waitKey(1)
        if key == ord("c") or key == ord("C"):
            # ClearDrawing
            img = np.zeros((512, 512, 3), np.uint8)  
            img = cv.resize(img, (1700, 800))# Reset the image to a blank one
        elif key == 27 or key == ord("z") or key == ord("Z"):
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
