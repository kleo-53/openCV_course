# изменить цветовую палитру по заданному шаблону

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue_shift = 100  # change this parameter to get different pallet
img_hsv[:, :, 0] = (img_hsv[:, :, 0] + hue_shift) % 180
result = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

cv2.imwrite("../output_img/17/hard_pallet.jpg", result)
