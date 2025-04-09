# изменить баланс белого, сделать более "холодную" картинку

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

result = np.clip(img * [1.4, 1, 0.6], 0, 255)

cv2.imwrite("../output_img/16/hard_cold.jpg", result)
