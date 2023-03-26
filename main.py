import cv2
import numpy as np

img_rgb = cv2.imread('gambar1.jpg')

img_ycb = np.zeros_like(img_rgb, dtype=np.float32)
for i in range(img_rgb.shape[0]):
    for j in range(img_rgb.shape[1]):
        R, G, B = img_rgb[i,j]
        Y = 0.299 * R + 0.587 * G + 0.114 * B
        Cb = 128 - 0.168736 * R - 0.331264 * G + 0.5 * B
        Cr = 128 + 0.5 * R - 0.418688 * G - 0.081312 * B
        img_ycb[i,j] = [Y, Cb, Cr]

img_ycb = np.uint8(img_ycb)
cv2.imshow('Origina Image', img_rgb)
cv2.imshow('YCbCr Image', img_ycb)
cv2.waitKey(0)
cv2.destroyAllWindows()
