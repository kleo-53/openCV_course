# перевести в grayscale

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    sys.exit("Could not read the image.")

cv2.imwrite("../output_img/04/hard_grayscale.jpg", img)
