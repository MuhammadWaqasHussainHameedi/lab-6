import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
def mse(image1, image2):
    return np.mean((image1 - image2) ** 2)

original_image = cv2.imread("C:\\Users\\ma\\project\\data\\Labdata\\ShahzadpurHH.tif", 0)
denoised_image = cv2.GaussianBlur(original_image, (5, 5), 0)

mse_value = mse(original_image, denoised_image)
print(f"Mean Squared Error: {mse_value}")


ssim_value = ssim(original_image, denoised_image)
print(f"Structural Similarity Index (SSIM): {ssim_value}")