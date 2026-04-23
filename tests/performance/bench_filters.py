import cv2
import numpy as np
import time
import pytest

def test_performance_blur():
    """Simple performance test for Gaussian Blur."""
    img = np.random.randint(0, 256, (1000, 1000, 3), dtype=np.uint8)
    
    start_time = time.time()
    cv2.GaussianBlur(img, (15, 15), 0)
    end_time = time.time()
    
    duration = end_time - start_time
    print(f"Blurring 1000x1000 image took: {duration:.4f}s")
    assert duration < 0.5 # Should be very fast
