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

## Zasady i Zarządzanie Kodem (Code Review & Branches)
Dokładny opis zasad i zarządzania kodem jest dostępny w pliku [commit_rules.md](docs/commit_rules.md).


