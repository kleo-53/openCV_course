# применить операцию эрозии к изображению

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    sys.exit("Could not read the image.")

kernel = np.ones((10, 10))
result = cv2.erode(img, kernel, iterations=1)

cv2.imwrite("../output_img/24/hard_erosion.jpg", result)
