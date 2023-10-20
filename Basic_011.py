import cv2 as cv

def main():
    cap = cv.VideoCapture(0)

    cap.set(3,1280)
    cap.set(4,720)

    if not cap.isOpened() :
        print("Error >> Camera is not opened")
        return
    
    while True:
        ret , frame = cap.read()

        if not ret :
            print("Error >> Frame has error")
            return 
        
        cv.imshow("Live Video",frame)

        k = cv.waitKey(1)
        if k == 27 or k ==  ord("q"):
            break
    cap.release()
    cv.destroyAllWindows()
        

if __name__ == "__main__":
    main()