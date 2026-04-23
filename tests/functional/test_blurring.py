import cv2
import numpy as np
import pytest

def test_gaussian_blur():
    """
    Test for cv2.GaussianBlur.
    Verify that the output image is blurred (modified) and has the same dimensions as the input.
    """
    # Create a simple test image (a white square in a black background)
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(img, (25, 25), (75, 75), (255, 255, 255), -1)
    
    # Apply Gaussian Blur
    ksize = (5, 5)
    sigmaX = 0
    blurred = cv2.GaussianBlur(img, ksize, sigmaX)
    
    # Assertions
    assert blurred is not None, "Output image is None"
    assert blurred.shape == img.shape, f"Shape mismatch: {blurred.shape} != {img.shape}"
    assert blurred.dtype == img.dtype, f"Dtype mismatch: {blurred.dtype} != {img.dtype}"
    assert not np.array_equal(img, blurred), "Image was not modified by GaussianBlur"
    
    # Check if the blurring effect occurred
    diff = cv2.absdiff(img, blurred)
    assert np.sum(diff) > 0, "No difference detected between original and blurred image"

def test_median_blur():
    """
    Test for cv2.medianBlur.
    Verify that the output image is blurred (modified) and has the same dimensions as the input.
    """
    # Create a test image with some "noise" pixels
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(img, (25, 25), (75, 75), (255, 255, 255), -1)
    
    # Add unique pixels that represent noise
    img[30, 30] = [255, 0, 0] # Red pixel
    img[70, 70] = [0, 255, 0] # Green pixel
    
    # Apply Median Blur
    ksize = 5
    blurred = cv2.medianBlur(img, ksize)
    
    # Assertions
    assert blurred is not None, "Output image is None"
    assert blurred.shape == img.shape, f"Shape mismatch: {blurred.shape} != {img.shape}"
    assert blurred.dtype == img.dtype, f"Dtype mismatch: {blurred.dtype} != {img.dtype}"
    assert not np.array_equal(img, blurred), "Image was not modified by medianBlur"
    
    # Check if the noise pixels were removed/modified by the median filter
    assert not np.array_equal(blurred[30, 30], [255, 0, 0]), "Red noise pixel was not removed"
    assert not np.array_equal(blurred[70, 70], [0, 255, 0]), "Green noise pixel was not removed"
