# отразить изображение по нижней границе

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

result = cv2.flip(img, flipCode=0)

cv2.imwrite("../output_img/07/hard_down.jpg", result)
