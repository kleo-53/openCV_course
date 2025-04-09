# повернуть изображение на 45 градусов

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

h, w = img.shape[:2]
image_center = [w // 2, h // 2]
rot_mat = cv2.getRotationMatrix2D(image_center, 45, 0.7)
result = cv2.warpAffine(img, rot_mat, img.shape[1::-1])

cv2.imwrite("../output_img/08/hard_45.jpg", result)
