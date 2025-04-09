# найти контуры на изображении, применив фильтры (Собеля или Лапласиан)

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobel_x, sobel_y)
sobel_res = np.uint8(np.clip(sobel, 0, 255))
cv2.imwrite("../output_img/20/hard_laplasian.jpg", sobel_res)

laplacian = cv2.Laplacian(img_gray, cv2.CV_64F)
laplacian_res = np.uint8(np.clip(np.abs(laplacian), 0, 255))
cv2.imwrite("../output_img/20/hard_sobel.jpg", laplacian_res)
