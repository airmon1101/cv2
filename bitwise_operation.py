"""
1- cv2.bitwise_and(ing_1, img_2)
2- cv2.bitwise_or(ing_1, img_2)
3- cv2.bitwise_and(ing_1)

* img1 img2 height width same
** use only black and white 
*** create a mask first

"""
import cv2

import numpy as np

img_1 = np.zeros((300,300), dtype="uint8")
img_2 = np.zeros((300,300), dtype="uint8")

cv2.circle(img_1, (150,150), 100, 255, -1)
cv2.rectangle(img_2, (100, 100), (250, 250), 255, -1)

bitwise_and = cv2.bitwise_and(img_1, img_2)
bitwise_or = cv2.bitwise_or(img_1, img_2)
bitwise_not = cv2.bitwise_not(img_1)


cv2.imshow('Circle', img_1)
cv2.imshow('Rectrangle', img_2)
cv2.imshow('AND', bitwise_and)
cv2.imshow('OR', bitwise_or)
cv2.imshow('NOT', bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()

