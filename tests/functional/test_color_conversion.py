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

def test_grayscale_to_grayscale():
    """
    Test converting a 1-channel (grayscale) image to grayscale.
    Verifies that direct conversion using BGR2GRAY on 1-channel input raises an error,
    and converting to BGR and back to GRAY preserves original values (no changes).
    """
    # Create a 1-channel grayscale image
    img_gray = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

    # 1. Direct conversion should fail because it expects 3 channels
    with pytest.raises(cv2.error) as exc_info:
        cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
    assert "Invalid number of channels" in str(exc_info.value) or exc_info.value.code == -15

    # 2. Conversion from Gray -> BGR -> Gray should result in no changes
    img_bgr = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    img_gray_back = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    assert np.array_equal(img_gray, img_gray_back), "Grayscale conversion via BGR introduced changes in pixel values"

def test_conversion_with_unusual_depths():
    """
    Test conversion on images with unusual bit-depths (16-bit and float32).
    Verifies that cv2.cvtColor successfully converts them and preserves the data depth.
    """
    # 1. 16-bit unsigned integer (uint16)
    img_bgr_16 = np.random.randint(0, 65536, (100, 100, 3), dtype=np.uint16)
    img_gray_16 = cv2.cvtColor(img_bgr_16, cv2.COLOR_BGR2GRAY)
    
    assert img_gray_16 is not None
    assert img_gray_16.shape == (100, 100)
    assert img_gray_16.dtype == np.uint16, f"Expected uint16, got {img_gray_16.dtype}"

    # 2. 32-bit single-precision floating point (float32)
    img_bgr_f32 = np.random.rand(100, 100, 3).astype(np.float32)
    img_gray_f32 = cv2.cvtColor(img_bgr_f32, cv2.COLOR_BGR2GRAY)
    
    assert img_gray_f32 is not None
    assert img_gray_f32.shape == (100, 100)
    assert img_gray_f32.dtype == np.float32, f"Expected float32, got {img_gray_f32.dtype}"

