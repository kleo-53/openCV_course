# изменить баланс белого, сделать более "теплую" картинку

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

result = np.clip(img * [0.6, 1, 1.4], 0, 255)

cv2.imwrite("../output_img/15/hard_warm.jpg", result)
