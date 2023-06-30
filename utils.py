import numpy as np
import imutils
import cv2

def gray_it_up(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('modified_image.jpg', image)