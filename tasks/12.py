# изменить контрасть изображения

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

result = cv2.convertScaleAbs(img, alpha=2.5, beta=0)

cv2.imwrite("../output_img/12/hard_contrast.jpg", result)
