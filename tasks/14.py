# сделать гистограмную эквайлизацию

import cv2
import sys

img = cv2.imread("../input_img/medium.jpg")
if img is None:
    sys.exit("Could not read the image.")

channels = cv2.split(img)
eq_channels = [cv2.equalizeHist(ch) for ch in channels]
result = cv2.merge(eq_channels)

cv2.imwrite("../output_img/14/medium_equalize.jpg", result)
