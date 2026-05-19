import cv2
import numpy as np
import time
import tempfile
import os
import json

def test_benchmark_io():
    """
    [PERF] Benchmark I/O (Issue #13)
    Test mierzący czas operacji dyskowych zapisu i odczytu sekwencji 100 obrazów Full HD
    dla formatów bezstratnych (.png, .tiff). Obrazy są przechowywane w katalogu tymczasowym,
    aby nie obciążać repozytorium fizycznymi plikami po zakończeniu działania.
    """
    frame = np.random.randint(0, 256, (1080, 1920, 3), dtype=np.uint8)
    
    num_images = 100
    formats = [".png", ".tiff"]
    
    print("\n--- Rozpoczynam Benchmark I/O (100 obrazów 1920x1080) ---")
    
    results_data = {}
    
    # Użycie TemporaryDirectory zapewnia automatyczne "sprzątanie" plików po wyjściu z bloku with
    with tempfile.TemporaryDirectory() as temp_dir:
        for fmt in formats:
            # 1. Test zapisu (Write)
            write_start_time = time.perf_counter()
            for i in range(num_images):
                filepath = os.path.join(temp_dir, f"frame_{i}{fmt}")
                cv2.imwrite(filepath, frame)
            write_end_time = time.perf_counter()
            write_duration = write_end_time - write_start_time
            
            # 2. Test odczytu (Read)
            read_start_time = time.perf_counter()
            for i in range(num_images):
                filepath = os.path.join(temp_dir, f"frame_{i}{fmt}")
                _ = cv2.imread(filepath)
            read_end_time = time.perf_counter()
            read_duration = read_end_time - read_start_time
            
            # Wypisanie sformatowanych wyników pomiaru
            print(f"{fmt.upper():<5} - Zapis: {write_duration:.2f}s | Odczyt: {read_duration:.2f}s")
            
            results_data[fmt] = {
                "write_s": round(write_duration, 3),
                "read_s": round(read_duration, 3)
            }
            
    print("---------------------------------------------------------")

    # Zapis wyników do pliku JSON, aby Paweł mógł je wykorzystać 
    # w swoim raporcie CI/CD (Issue #24)
    results_file = os.path.join(os.path.dirname(__file__), "results_io.json")
    with open(results_file, "w") as f:
        json.dump(results_data, f, indent=4)
