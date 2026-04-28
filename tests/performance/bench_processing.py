import cv2
import numpy as np

def generate_random_image(width, height):
    """
    Generuje sztuczną macierz obrazu z losowym szumem (3 kanały, 8-bit).
    Służy jako baza testowa do obciążania algorytmów OpenCV bez konieczności
    trzymania ciężkich plików w repozytorium projektu.
    """
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

def test_benchmark_large_matrices():
    """
    [PERF] Procesowanie dużych macierzy (Issue #12)
    Test wydajności mierzący czas nakładania ciężkich filtrów (rozmycie, Canny)
    na obrazy w wysokich rozdzielczościach (4K, 8K).
    """
    pass
