import cv2
import numpy as np
import pytest

def test_bgr_to_gray_conversion():
    """
    Test conversion from BGR color space to Grayscale.
    Verify that the output has a single channel and correct dimensions.
    """
    # Create a dummy BGR image (100x100, 3 channels)
    # BGR values: Blue, Green, Red
    img_bgr = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Fill with some colors to ensure conversion logic is exercised
    img_bgr[0:50, 0:50] = [255, 0, 0]    # Blue
    img_bgr[0:50, 50:100] = [0, 255, 0]  # Green
    img_bgr[50:100, 0:50] = [0, 0, 255]  # Red
    img_bgr[50:100, 50:100] = [127, 127, 127] # Gray

    # Convert BGR to GRAY
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Assertions
    assert img_gray is not None, "Conversion result should not be None"
    
    # In OpenCV, GRAY images have shape (height, width)
    assert len(img_gray.shape) == 2, f"Expected 2 dimensions for grayscale image, got {len(img_gray.shape)}"
    assert img_gray.shape == (100, 100), f"Expected shape (100, 100), got {img_gray.shape}"
    
    # Verify data type
    assert img_gray.dtype == np.uint8, f"Expected dtype uint8, got {img_gray.dtype}"

    # Verify that it's effectively 1 channel (by checking shape length again or explicitly)
    # If it was 3 channels, shape would be (100, 100, 3)
