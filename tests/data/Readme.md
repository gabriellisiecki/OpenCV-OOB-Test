# Dane testowe dla OpenCV

Ten katalog zawiera zminimalizowane próbki obrazów wykorzystywane jako dane wejściowe w zautomatyzowanych testach funkcjonalnych (framework `pytest`). 

## Zawartość
* `test_image.jpg` - Mikroskopijny obraz testowy w formacie stratnym (JPEG), używany do testowania operacji I/O.
* `test_image.png` - Mikroskopijny obraz testowy w formacie bezstratnym (PNG), używany m.in. do testów nakładania filtrów i konwersji przestrzeni barw.

**Uwaga:** Waga tych plików została celowo zredukowana do absolutnego minimum (pojedyncze kilobajty/bajty). Prosimy nie podmieniać ich na obrazy o dużej rozdzielczości, aby nie obciążać historii repozytorium Git oraz przyspieszyć działanie pipeline'u CI/CD.