import cv2
import numpy as np
import time
import json
import os

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
    resolutions = {
        "4K": (3840, 2160),
        "8K": (7680, 4320)
    }

    print("\n--- Rozpoczynam Benchmark Procesowania Dużych Macierzy ---")

    results_data = {}

    for name, (width, height) in resolutions.items():
        image = generate_random_image(width, height)

        start_time = time.perf_counter()

        # 1. Konwersja do skali szarości (
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # 2. Silne rozmycie Gaussa 
        blurred = cv2.GaussianBlur(gray, (21, 21), 0)
        
        # 3. Ekstrakcja krawędzi
        edges = cv2.Canny(blurred, 50, 150)
        
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        print(f"Rozdzielczość {name:<2} ({width}x{height}): {duration:.3f}s")
        results_data[name] = round(duration, 3)
        
    print("----------------------------------------------------------")
    
    # Zapis wyników do pliku JSON, aby Paweł mógł je wykorzystać 
    # w swoim raporcie CI/CD (Issue #24)
    results_file = os.path.join(os.path.dirname(__file__), "results_processing.json")
    with open(results_file, "w") as f:
        json.dump(results_data, f, indent=4)
