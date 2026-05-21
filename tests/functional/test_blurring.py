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

def test_blur_empty_image():
    """
    Test blurring on a 0x0 empty image.
    Verifies that calling cv2.GaussianBlur or cv2.medianBlur on an empty image raises cv2.error.
    """
    # Create an empty 0x0 image
    empty_img = np.zeros((0, 0, 3), dtype=np.uint8)

    # 1. Gaussian Blur should raise cv2.error
    with pytest.raises(cv2.error) as exc_info_g:
        cv2.GaussianBlur(empty_img, (5, 5), 0)
    assert "!_src.empty()" in str(exc_info_g.value)

    # 2. Median Blur should raise cv2.error
    with pytest.raises(cv2.error) as exc_info_m:
        cv2.medianBlur(empty_img, 5)
    assert "!_src0.empty()" in str(exc_info_m.value)

def test_blur_large_kernel():
    """
    Test blurring with very large kernel sizes, and invalid even kernel sizes.
    Verifies that very large odd kernels succeed and blur, whereas even kernels raise cv2.error.
    """
    # Create a test image
    img = np.zeros((150, 150, 3), dtype=np.uint8)
    cv2.rectangle(img, (40, 40), (110, 110), (255, 255, 255), -1)

    # 1. Very large odd kernel (e.g., 101) - should succeed
    large_ksize_g = (101, 101)
    blurred_g = cv2.GaussianBlur(img, large_ksize_g, 0)
    assert blurred_g is not None
    assert blurred_g.shape == img.shape
    assert not np.array_equal(img, blurred_g), "Image should be modified by large Gaussian Blur"

    large_ksize_m = 101
    blurred_m = cv2.medianBlur(img, large_ksize_m)
    assert blurred_m is not None
    assert blurred_m.shape == img.shape
    assert not np.array_equal(img, blurred_m), "Image should be modified by large Median Blur"

    # 2. Invalid even kernel size (e.g., 6) - should raise cv2.error
    with pytest.raises(cv2.error) as exc_info_even_g:
        cv2.GaussianBlur(img, (6, 6), 0)
    assert "ksize.width % 2 == 1" in str(exc_info_even_g.value)

    with pytest.raises(cv2.error) as exc_info_even_m:
        cv2.medianBlur(img, 6)
    assert "ksize % 2 == 1" in str(exc_info_even_m.value)

