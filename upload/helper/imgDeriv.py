import cv2
import numpy as np
from pathlib import Path


def image_deriv(image_name):
    img = cv2.imread(image_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

    #canny
    img_canny = cv2.Canny(img,100,200)

    #sobel
    img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
    img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
    img_sobel = img_sobelx + img_sobely


    #prewitt
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

    location = image_name.split('.')[0]
    cv2.imwrite(location + "-canny.jpg", img_canny)
    cv2.imwrite(location + "-sobelx.jpg", img_sobelx)
    cv2.imwrite(location + "-sobely.jpg", img_sobely)
    cv2.imwrite(location + "-sobel.jpg", img_sobel)
    cv2.imwrite(location + "-prewitt_x.jpg", img_prewittx)
    cv2.imwrite(location + "-prewitt_y.jpg", img_prewitty)
    cv2.imwrite(location + "-prewitt.jpg", img_prewittx + img_prewitty)

    cv2.destroyAllWindows()
