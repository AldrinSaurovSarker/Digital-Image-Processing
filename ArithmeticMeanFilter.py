# Arithmetic Mean Filter to blur images using cv2 Python
import cv2
import numpy as np

# Specifying the image file and resizing it to a standard size.
img = cv2.imread("images/Einstein.jpg", 0)
img = cv2.resize(img, (500, 500))

# We have taken a 5x5 size filter. We can also use 3x3, 7x7 etc.
kernel = np.ones([5, 5]) / 25
i_size = img.shape
k_size = kernel.shape

img2 = np.zeros([i_size[0], i_size[1]])

R = i_size[0] + k_size[0] - 1
C = i_size[1] + k_size[1] - 1
Z = np.zeros([R, C])

# Padding: Expanding image size by the borders so that index doesn't exceed out of range while applying filter
for i in range(i_size[0]):
    for j in range(i_size[1]):
        Z[i + int((k_size[0] - 1) / 2), j + int((k_size[1] - 1) / 2)] = img[i, j]

# Applying Filter: For every pixel on the image, put the center of the filter on the pixel. Let the pixel be 'P'
# Calculate the sum of the image area the filter is currently occupying and replace 'P' by the sum.
# Move to the next image pixel.
for i in range(i_size[0]):
    for j in range(i_size[1]):
        k = Z[i:i + k_size[0], j:j + k_size[1]]
        img2[i, j] = np.sum(k * kernel)

# Concatenating blurred image with original image and preview
img2 = np.array(img2, dtype=np.uint8)
img2 = cv2.hconcat([img, img2])

print('Displaying Image....')
cv2.imshow('Arithmetic Mean Filter', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
