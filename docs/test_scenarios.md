# Wstępne scenariusze testowe

## Testy funkcjonalne (4 sztuki)
1. **Wczytywanie i zapisywanie różnych formatów (I/O):** Sprawdzenie, czy biblioteka poprawnie wczytuje klatki w formatach `.jpg` oraz `.png` i potrafi zapisać je na dysk bez utraty kluczowych właściwości macierzy (np. poprawne wymiary i typ danych po odczytaniu).
2. **Konwersja przestrzeni barw (Color Space):** Weryfikacja funkcji `cv2.cvtColor`. Test założy konwersję obrazu BGR do skali szarości (GRAY) i sprawdzi, czy wynikowa macierz ma tylko jeden kanał oraz poprawne wartości pikseli.
3. **Nakładanie prostych filtrów (Blurring):** Sprawdzenie działania funkcji takich jak `cv2.GaussianBlur` czy `cv2.medianBlur` na testowym obrazie poprzez weryfikację, czy obraz wynikowy został zmodyfikowany (różni się od wejściowego) i zachował swoje początkowe wymiary.
4. **Wykrywanie Krawędzi (Canny Edge Detection):** Sprawdzenie działania funkcji algorytmicznej `cv2.Canny`. Test wykaże, czy z oryginalnego obrazu program poprawnie wyodrębnia jasne i ciemne kontury, otrzymując binarną (czarno-białą) macierz krawędzi różną od pierwotnego tła.

## Testy wydajnościowe (2 sztuki)
1. **Pomiar czasu procesowania dużych macierzy (4K/8K):** Zmierzenie czasu wykonania kosztownej operacji (np. detekcja krawędzi Canny lub wielokrotne nakładanie rozmycia) na sztucznie wygenerowanej lub wczytanej macierzy o bardzo dużej rozdzielczości. Wynik zostanie zapisany do logów w celu późniejszego porównania.
2. **Benchmark operacji wejścia/wyjścia (I/O Throughput):** Wczytanie i natychmiastowe zapisanie dużego zbioru plików (np. sekwencji 100 obrazów Full HD) do formatów bezstratnych, takich jak `.png` lub `.tiff`. Zmierzony zostanie łączny narzut czasowy operacji dyskowych w OpenCV w porównaniu do pojedynczego pliku.