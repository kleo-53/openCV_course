# сделать гамма-перобразование

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

gamma = 2.5
gamma_table = np.array([((i / 255.0) ** (1.0 / gamma)) * 255 for i in np.arange(0, 256)]).astype(np.uint8)
result = cv2.LUT(img, gamma_table)

cv2.imwrite("../output_img/13/hard_gamma.jpg", result)
