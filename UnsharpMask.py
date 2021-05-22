# Python program to sharpening an image
# Sharpened Image = Main Image + (Masked Image - Main Image)
# Note: Output image will be in BW format.
import cv2
import numpy as np

# Read and resize image
img = cv2.imread("images/Einstein.jpg", 0)
img = cv2.resize(img, (500, 500))

# Creating Mask
mask_size_length = 5
kernel = np.ones([mask_size_length, mask_size_length]) / (mask_size_length ** 2)
i_size = img.shape
k_size = kernel.shape

img2 = np.zeros([i_size[0], i_size[1]])

R = i_size[0] + k_size[0] - 1
C = i_size[1] + k_size[1] - 1
Z = np.zeros([R, C])

# Padding image to apply mask
for i in range(i_size[0]):
    for j in range(i_size[1]):
        Z[i+int((k_size[0]-1)/2), j+int((k_size[1]-1)/2)] = img[i, j]

# Applying Mask
for i in range(i_size[0]):
    for j in range(i_size[1]):
        k = Z[i:i+k_size[0], j:j+k_size[1]]
        img2[i, j] = np.sum(k * kernel)

# Sharpening
img2 = np.array(img2, dtype=np.uint8)
mask = cv2.subtract(img, img2)
img2 = cv2.add(img, mask)

img2 = cv2.hconcat([img, img2])

cv2.imshow('Unsharp Mask', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
