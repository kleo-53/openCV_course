# отразить изображение по правой границе

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

result = cv2.flip(img, flipCode=1)

cv2.imwrite("../output_img/06/hard_right.jpg", result)
