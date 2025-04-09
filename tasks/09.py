# повернуть изображение на 30 градусов вокруг заданной точки

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

h, w = img.shape[:2]
point = [w // 10, h // 4]  # edit this to see different rotations
rot_mat = cv2.getRotationMatrix2D(point, 35, 0.4)
result = cv2.warpAffine(img, rot_mat, img.shape[1::-1])

cv2.imwrite("../output_img/09/hard_30_with_point.jpg", result)
