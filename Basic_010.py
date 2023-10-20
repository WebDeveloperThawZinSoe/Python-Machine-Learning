import cv2 as cv

def main():
    cap = cv.VideoCapture(0)
    
    # Set the resolution to 1280x720
    cap.set(3, 1280)
    cap.set(4, 720)
    
    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        return
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Can't receive frame. Exiting ...")
            break
        
        cv.imshow("Live Video Frame", frame)

        # Check for key press (use 'q' to exit)
        key = cv.waitKey(1)
        if key == ord('q') or key == 27:
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
