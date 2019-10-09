import cv2

def resize(file, height, width):
    filename = file
    oriimg = cv2.imread(filename)
    newimg = cv2.resize(oriimg,(int(height),int(height)))
    cv2.waitKey(0)
    cv2.imwrite("resizeimg_{}".format(file),newimg)
