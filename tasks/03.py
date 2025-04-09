# найти canny edges на изображении

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

result = cv2.Canny(img, 100, 200)

cv2.imwrite("../output_img/03/hard_canny_edges.jpg", result)
