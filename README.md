# OpenCV-OOB-Test

Celem projektu jest przetestowanie najnowszej stabilnej wersji modułu `opencv-python` z repozytorium PyPI (i w przyszłości z repozytorium GitHub), w tym pipeline CI/CD, testy funkcjonalne oraz wydajnościowe.

## Zespół, role i komunikacja
- **[Gabriel Lisiecki](https://github.com/gabriellisiecki) (Tech Lead / DevOps):** Architektura testów, wdrożenie GitHub Actions (CI/CD), testy wydajnościowe, Zarządzanie zadaniami dla zepsołu  (Issues), weryfikacja Pull Requestów jako `reviewer`. 
- **[Adrian Markowski](https://github.com/markowskiadrian) (Functional QA):** Projektowanie i implementacja wszystkich testów funkcjonalnych w kodzie Python, formatowanie raportów, weryfikacja Pull Requestów jako `reviewer`.
- **[Paweł Nawrocki](https://github.com/pawnaww) (QA / Docs):** Projektowanie scenariuszy testów akceptacyjnych na podstawie dokumentacji OpenCV, tworzenie i utrzymanie struktury plików w repozytorium, utrzymanie dokumentacji.

## Struktura katalogów projektu

```text
OpenCV-OOB-Test/
├── .github/
│   └── workflows/
│       └── pipeline.yml              # Konfiguracja GitHub Actions Pipeline
├── tests/
│   ├── functional/                   # Testy funkcjonalne
│   │   ├── test_format_io.py         # Wczytywanie i zapis obrazow (I/O)
│   │   ├── test_blurring.py          # Filtrowanie: GaussianBlur, medianBlur
│   │   ├── test_color_conversion.py  # Konwersja przestrzeni barw (BGR->GRAY)
│   │   └── test_canny_edge.py        # Detekcja krawedzi (Canny)
│   ├── performance/                  # Testy wydajnosciowe
│   │   ├── test_bench_io.py          # Benchmark I/O (zapis/odczyt 100 obrazow)
│   │   └── test_bench_processing.py  # Benchmark procesowania macierzy 4K/8K
│   └── data/                         # Dane testowe
├── docs/                             # Dokumentacja projektu
│   ├── test_scenarios.md             # Scenariusze testow akceptacyjnych
│   └── commit_rules.md               # Zasady commitowania
├── requirements.txt                  # Zaleznosci projektu
└── README.md                         # Glowny plik informacyjny
```

## Kanaly komunikacji

- **Serwer Discord zespolu:** [https://discord.gg/qwk5zNNku4](https://discord.gg/qwk5zNNku4)
- **Zarzadzanie zadaniami i kodem:** GitHub (Issues, Pull Requesty, Code Review)

### Kontakt do czlonkow zespolu

| Czlonek | Rola | GitHub | Discord |
|---------|------|--------|---------|
| Gabriel Lisiecki | Tech Lead / DevOps | [@gabriellisiecki](https://github.com/gabriellisiecki) | `butter4222` |
| Adrian Markowski | Functional QA | [@markowskiadrian](https://github.com/markowskiadrian) | `22adi` |
| Pawel Nawrocki | QA / Docs | [@pawnaww](https://github.com/pawnaww) | `pawnaww` |

## Harmonogram projektowy

Projekt trwa 2,5 miesiąca. Cele do zrealizowania w kolejnych etapach:
- **Punkt kontrolny 1 (Organizacja projektu):** 13.03.2026
- **Punkt kontrolny 2 (Zarządzanie kodem):** 10.04.2026
- **Punkt kontrolny 3 (Testowanie):** 15.05.2026
- **Ocena końcowa:** 29.05.2026

Dokładny harmonogram jest dostępny w widoku kalendarzowym w [GitHub Projects](https://github.com/users/gabriellisiecki/projects/3).

## Zasady i Zarzadzanie Kodem (Code Review & Branches)
Dokladny opis zasad i zarzadzania kodem jest dostepny w pliku [commit_rules.md](docs/commit_rules.md).

## Strategia testowa

Projekt testuje modul `opencv-python` w podejsciu OOB (Out Of the Box) - weryfikujemy zachowanie biblioteki w typowych scenariuszach uzycia, bez modyfikacji jej kodu zrodlowego.

### Testy funkcjonalne (4 testy)
Sprawdzaja poprawnosc dzialania kluczowych funkcji OpenCV:
- **I/O** - zapis i odczyt obrazow w roznych formatach (JPG, PNG)
- **Filtrowanie** - rozmycie Gaussa i medianowe, weryfikacja modyfikacji obrazu
- **Konwersja kolorow** - zmiana przestrzeni barw BGR na skale szarosci
- **Detekcja krawedzi** - algorytm Canny, weryfikacja binarnosci wyniku

### Testy wydajnosciowe (2 testy)
Mierza czas wykonania operacji na duzych danych:
- **Benchmark I/O** - zapis i odczyt 100 obrazow Full HD w formatach PNG i TIFF
- **Benchmark procesowania** - filtrowanie i detekcja krawedzi na macierzach 4K/8K

### Pipeline CI/CD
Pipeline uruchamiana jest automatycznie przy Pull Requestach do `main` oraz mozna ja odpalic recznie (`workflow_dispatch`). Pipeline:
- Instaluje `opencv-python-headless` z PyPI
- Uruchamia testy funkcjonalne i wydajnosciowe przez `pytest`
- Generuje raporty JUnit XML
- Uploaduje artefakty (raporty XML + wyniki JSON z benchmarkow)
- Wyswietla czytelne podsumowanie wynikow na stronie workflow run

### Scenariusze testow akceptacyjnych
Dokumentacja scenariuszy dostepna w pliku [test_scenarios.md](docs/test_scenarios.md).
