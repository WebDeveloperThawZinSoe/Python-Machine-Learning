#image motion
import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np
import time

def main():
    img1 = cv.imread("images/tzs1.jpeg")
    img2 = cv.imread("images/tzs2.jpg")

    img1 = cv.resize(img1, (img2.shape[1], img2.shape[0]))

    img1 =  cv.cvtColor(img1,cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img2,cv.COLOR_BGR2RGB)
    
    alpha = 0.0
    gama = 1.0
    bata = 0.0

    # output1 = img1 + img2 
    # output2 = cv.addWeighted(img1,alpha,img2,gama,bata)


    # images = [img1,img2,output1,output2]
    # titles = ["Imge1","Image2","Image3","Image4"]

    # for i in range(len(images)):
    #     plt.subplot(5,4,1+i)
    #     plt.imshow(images[i])
    #     plt.title(titles[i])
    #     plt.xticks([])
    #     plt.yticks([])

    # plt.show()

    for i in np.linspace(0,1,100):
        alpha = i 
        bata  = 1 - i 
        output2 = cv.addWeighted(img1,alpha,img2,bata,gama)
        cv.imshow("My Frame",output2)
        time.sleep(0.05)
        if cv.waitKey(1) == 27:
            break

    cv.destroyAllWindows()


if __name__ == "__main__":
    main()