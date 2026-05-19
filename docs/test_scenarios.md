# Scenariusze testów akceptacyjnych

Poniższy dokument definiuje ustrukturyzowane scenariusze testów akceptacyjnych dla projektu testowania biblioteki `opencv-python`.

## Scenariusz 1: Wczytywanie i zapisywanie plików (I/O)
**1. Cel testu:** Weryfikacja poprawności wczytywania i zapisywania obrazów w formatach `.jpg` i `.png` przez bibliotekę, bez utraty kluczowych właściwości macierzy.

**2. Oczekiwany rezultat:** Zapisane pliki pomyślnie tworzą się na dysku w wyznaczonym formacie, a ich ponowne wczytanie do programu zwraca macierz obrazu o identycznych wymiarach bazowych (szerokość, wysokość) co plik oryginalny.

**3. Kryterium zaliczenia:** Funkcje testowe `pytest` nie zwracają wyjątków podczas operacji I/O, a asercje porównujące wymiary macierzy wejściowej i wyjściowej przechodzą pomyślnie (zwracają wartość `True`).

---

## Scenariusz 2: Konwersja przestrzeni barw (Color Space)
**1. Cel testu:** Sprawdzenie działania wbudowanej funkcji `cv2.cvtColor` podczas konwersji standardowego obrazu wielokanałowego (BGR) do jednokanałowej skali szarości (GRAY).

**2. Oczekiwany rezultat:** Po wykonaniu operacji konwersji, otrzymana macierz obrazu traci trzeci wymiar (głębię kolorów BGR) i posiada tylko jeden kanał reprezentujący luminancję pikseli, zachowując przy tym pierwotną rozdzielczość obrazu.

**3. Kryterium zaliczenia:** Asercja sprawdzająca parametr `.shape` macierzy w bibliotece NumPy potwierdza brak trzeciego wymiaru, a wykonanie testu kończy się statusem PASS.

---

## Scenariusz 3: Nakładanie prostych filtrów wygładzających (Blurring)
**1. Cel testu:** Weryfikacja poprawnego działania algorytmów splotowych na przykładzie nałożenia filtru rozmycia Gaussowskiego (`cv2.GaussianBlur`) na obraz testowy.

**2. Oczekiwany rezultat:** Wygenerowany obraz zostaje poprawnie zmodyfikowany matematycznie (wartości poszczególnych pikseli ulegają uśrednieniu zgodnie z rozmiarem jądra filtru), przy jednoczesnym zachowaniu oryginalnych wymiarów siatki obrazu.

**3. Kryterium zaliczenia:** Bezpośrednie porównanie (np. poprzez operację różnicy macierzy) obrazu wejściowego i wyjściowego wykazuje rozbieżności w wartościach pikseli, a asercja sprawdzająca rozdzielczość nie zgłasza błędu.