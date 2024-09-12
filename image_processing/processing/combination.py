import numpy as np
import skimage as ski

from skimage.color import rgb_colors
from skimage.exposure import histogram_matching
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."
    gray_image1 = rgb_colors.gray(image1)
    gray_image2 = rgb_colors.gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similarity of the images: ", score)
    normalized_difference_image = (difference_image-np.minimum(difference_image))/(np.maximum(difference_image)-np.minimum(difference_image))
    return normalized_difference_image

def transfer_histogram(image1, image2):
    matched_image = histogram_matching(image1, image2, multichannel=True)
    return matched_image