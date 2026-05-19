import cv2
import numpy as np
import os
import pytest

def test_read_image():
    # Create a dummy image
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('dummy.jpg', img)

    # Read the image
    read_img = cv2.imread('dummy.jpg')

    # Check if the image was read successfully
    assert read_img is not None
    assert read_img.shape == (100, 100, 3)
    assert read_img.dtype == np.uint8

    # Clean up
    os.remove('dummy.jpg')

def test_write_image():
    # Create a dummy image
    img = np.zeros((100, 100, 3), dtype=np.uint8)

    # Write the image
    cv2.imwrite('dummy_write.jpg', img)
    cv2.imwrite('dummy_write.png', img)

    # Check if the files exist
    assert os.path.exists('dummy_write.jpg')
    assert os.path.exists('dummy_write.png')

    # Read the images back
    read_img_jpg = cv2.imread('dummy_write.jpg')
    read_img_png = cv2.imread('dummy_write.png')

    # Check properties
    assert read_img_jpg is not None
    assert read_img_jpg.shape == (100, 100, 3)
    assert read_img_jpg.dtype == np.uint8

    assert read_img_png is not None
    assert read_img_png.shape == (100, 100, 3)
    assert read_img_png.dtype == np.uint8

    # Clean up
    os.remove('dummy_write.jpg')
    os.remove('dummy_write.png')

def test_read_non_existent_file():
    # Attempt to read a file that does not exist
    read_img = cv2.imread('this_file_does_not_exist_at_all.jpg')
    assert read_img is None, "Reading a non-existent file should return None"

def test_write_invalid_path():
    # Create a dummy image
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Attempt to write to an invalid path/directory
    success = cv2.imwrite('invalid_directory_path_123/dummy.jpg', img)
    assert success is False, "Writing to an invalid path should return False"

def test_read_non_image_file():
    # Create a temporary non-image text file
    temp_txt_path = 'temp_text_file.txt'
    with open(temp_txt_path, 'w') as f:
        f.write("This is a simple text file, not an image.")
        
    try:
        # Attempt to read the text file as an image
        read_img = cv2.imread(temp_txt_path)
        assert read_img is None, "Reading a non-image file should return None"
    finally:
        # Clean up
        if os.path.exists(temp_txt_path):
            os.remove(temp_txt_path)

