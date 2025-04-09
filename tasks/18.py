# сделать бинаризацию изображения

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, result = cv2.threshold(img_gray, 140, 255, 0)

cv2.imwrite("../output_img/18/hard_bin.jpg", result)
