# сделать размытие изображения

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

result = cv2.GaussianBlur(img, (21, 21), 0)

cv2.imwrite("../output_img/21/hard_blur.jpg", result)
