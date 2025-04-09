# сделать фильтрацию изображения при помощи Фурье преобразоваия, оставить только медленные частоты

import cv2
import sys

import numpy as np

img = cv2.imread("../input_img/hard.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    sys.exit("Could not read the image.")

f_transform = np.fft.fft2(img)
f_transform_shifted = np.fft.fftshift(f_transform)
rows, cols = img.shape
mask = np.zeros((rows, cols), np.uint8)
r = 100
center = [rows // 2, cols // 2]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
mask[mask_area] = 1
f_transform_filtered = f_transform_shifted * mask
result = np.fft.ifft2(np.fft.ifftshift(f_transform_filtered)).real

cv2.imwrite("../output_img/23/hard_slow_f.jpg", result)
