# найти контуры на бинаризированном изображении

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_threshed = cv2.threshold(img_gray, 140, 255, 0)
contours, _ = cv2.findContours(img_threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
result = np.zeros(img.shape)
cv2.drawContours(result, contours, -1, (255, 255, 255), 1)
cv2.imwrite("../output_img/19/hard_bin_contouring.jpg", result)
