# сместить изображение но 10 пикселей вправо

import cv2
import sys
import numpy as np

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

h, w = img.shape[:2]
move_hor, move_vert = 10, 0
trans_mat = np.float32([[1, 0, move_hor], [0, 1, move_vert]])
result = cv2.warpAffine(img, trans_mat, img.shape[1::-1])

cv2.imwrite("../output_img/10/hard_10_right.jpg", result)
