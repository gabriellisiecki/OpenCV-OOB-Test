import cv2
import numpy as np
import pytest

def test_canny_edge_detection():
    """
    Test the Canny edge detection algorithm's correctness.
    Verifies that the function produces a binary matrix and successfully 
    distinguishes edges from the background.
    """
    # Create a synthetic image: a white circle on a black background
    # This provides clear edges for the Canny algorithm to detect.
    image = np.zeros((200, 200), dtype=np.uint8)
    cv2.circle(image, (100, 100), 50, 255, -1)

    # Apply Canny edge detection
    # Thresholds are chosen to be robust for this high-contrast image
    edges = cv2.Canny(image, 100, 200)

    # Check if the output matrix is not None
    assert edges is not None, "Canny edge detection failed to produce an output"

    # Check if the output has the same dimensions as the input
    assert edges.shape == image.shape, f"Output shape {edges.shape} does not match input shape {image.shape}"

    # Assertion: Check if the output matrix is binary (contains only 0 and 255)
    unique_values = np.unique(edges)
    for value in unique_values:
        assert value in [0, 255], f"Output matrix is not binary; found unexpected value: {value}"

    # Assertion: Check if the extracted edges differ from the initial background
    # The background was all zeros. We expect at least some pixels to be 255 (edges).
    assert np.any(edges == 255), "Canny edge detection failed to detect any edges"
    
    # Additional check: ensure it's not just a copy of the input
    # (though binary check already covers this if input was grayscale with other values, 
    # but here input is also 0/255. However, Canny should only mark the perimeter).
    assert not np.array_equal(edges, image), "Output should only contain edges, not the filled shape"

if __name__ == "__main__":
    pytest.main([__file__])
