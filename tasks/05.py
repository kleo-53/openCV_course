# перевести изорбражение в hsv

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

result = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imwrite("../output_img/05/hard_hsv.jpg", result)
