import cv2
import numpy as np

# Load YCbCr image
img_ycb = cv2.imread('img.png')

# Convert YCbCr to RGB
img_rgb = np.zeros_like(img_ycb, dtype=np.float32)
for i in range(img_ycb.shape[0]):
    for j in range(img_ycb.shape[1]):
        Y, Cb, Cr = img_ycb[i,j]
        R = Y + 1.402 * (Cr - 128)
        G = Y - 0.344136 * (Cb - 128) - 0.714136 * (Cr - 128)
        B = Y + 1.772 * (Cb - 128)
        img_rgb[i,j] = [R, G, B]

# Display RGB image
img_rgb = np.uint8(img_rgb)
cv2.imshow('YCbCr Image', img_ycb)
cv2.imshow('RGB Image', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
