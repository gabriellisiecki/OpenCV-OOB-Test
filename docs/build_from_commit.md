# Budowanie OpenCV z wybranego commita (GitHub)

## Cel

Zamiast instalowac gotowa paczke `opencv-python` z PyPI, ten workflow pozwala na:
- Pobranie wybranego commita z oficjalnego repozytorium [opencv/opencv-python](https://github.com/opencv/opencv-python)
- Zbudowanie go ze zrodel na runnerze GitHub Actions
- Przetestowanie go przy uzyciu naszej istniejacey suity testow

## Jak uruchomic

1. Wejdz w zakladke **Actions** w repozytorium
2. Wybierz workflow **OpenCV Build from Commit**
3. Kliknij **Run workflow**
4. Wpisz SHA commita z repozytorium `opencv/opencv-python` (np. `71d3237`)
5. Kliknij **Run workflow**

## Zaleznosci budowania

Budowanie OpenCV ze zrodel wymaga dodatkowych narzedzi w porownaniu do instalacji z PyPI:

| Zaleznosc | Cel |
|-----------|-----|
| `cmake` | System budowania C++ uzywany przez OpenCV |
| `build-essential` | Kompilator GCC/G++ |
| `pkg-config` | Wykrywanie bibliotek systemowych |
| `numpy` | Wymagany przez opencv-python do budowania |
| `scikit-build` | Nakladka na cmake dla Pythona |

## Ograniczenia

- Budowanie trwa okolo 20-40 minut (w porownaniu do kilku sekund instalacji z PyPI)
- Ustawiony jest `timeout-minutes: 60` aby uniknac niekontrolowanego zuzycia minut CI
- Budowane sa tylko niezbedne moduly (`core`, `imgproc`, `imgcodecs`) aby skrocic czas kompilacji
- Uzywana jest wersja headless (`ENABLE_HEADLESS=1`) - bez GUI

## Rozwiazane problemy

Glowne wyzwania napotkane podczas implementacji:
1. **Dlugi czas budowania** - ograniczony przez wybor minimalnej listy modulow (`CMAKE_ARGS="-DBUILD_LIST=core,imgproc,imgcodecs"`)
2. **Zaleznosci systemowe** - zainstalowane przez `apt-get` w kroku pipeline
3. **Submoduly Git** - OpenCV korzysta z submodulow, wymagany jest `--recursive` przy klonowaniu
