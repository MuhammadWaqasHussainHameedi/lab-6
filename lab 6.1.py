'noise reduction'
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("C:\\Users\\ma\\project\\data\\Labdata\\ShahzadpurHH.tif", 0)  # Load the TIFF image in grayscale
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # Adjust the kernel size as needed
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blurred_image, cmap='gray')
plt.title('Denoised Image'), plt.xticks([]), plt.yticks([])
cv2.imwrite('denoised_image.tif', blurred_image)
plt.show()