# изменить яркость изображения

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

result = cv2.convertScaleAbs(img, alpha=1, beta=80)

cv2.imwrite("../output_img/11/hard_bright.jpg", result)
