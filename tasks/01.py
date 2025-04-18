# найти все orb features точки на изображении

import cv2
import sys

img = cv2.imread("../input_img/hard.jpg")
if img is None:
    sys.exit("Could not read the image.")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB.create()
keys = orb.detect(img_gray, None)
result = cv2.drawKeypoints(img, keys, img_gray, color=(0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite("../output_img/01/hard_orb_features.jpg", result)
