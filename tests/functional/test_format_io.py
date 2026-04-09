import cv2
import numpy as np
import pytest
import os

def test_opencv_version():
    """Check if OpenCV is installed."""
    assert cv2.__version__ is not None

def test_image_creation_and_save():
    """Test creating an image and saving it to disk."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[25:75, 25:75] = [255, 0, 0] # Blue square
    
    test_file = "test_image.png"
    cv2.imwrite(test_file, img)
    
    assert os.path.exists(test_file)
    
    # Read back and verify
    read_img = cv2.imread(test_file)
    assert read_img.shape == (100, 100, 3)
    assert np.array_equal(read_img[50, 50], [255, 0, 0])
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)
