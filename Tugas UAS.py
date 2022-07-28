import numpy as np
import cv2

img = cv2.imread('capture.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gambar 1', img)
cv2.imshow('gambar 2', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()