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
│       └── pipeline.yml       # Konfiguracja GitHub Actions Pipeline
├── tests/
│   ├── functional/            # Skrypty testów funkcjonalnych
│   │   ├── test_format_io.py  # (Przykład) Test wczytywania/zapisu obrazów
│   │   └── ...
│   ├── performance/           # Skrypty testów wydajnościowych 
│   │   ├── bench_filters.py   # (Przykład) Benchmark nakładania filtrów
│   │   └── ...
│   └── data/                  # Próbki danych testowych (np. małe obrazki JPG/PNG do testów)
├── docs/                      # Dokumentacja projektu
├── requirements.txt           # Zależności projektu 
└── README.md                  # Główny plik informacyjny / spis treści
```

## Kanały komunikacji

- **Bieżąca komunikacja:** - Kanał komunikacyjny (Discord): `https://discord.gg/qwk5zNNku4`
- **Zarządzanie zadaniami i kodem:** GitHub (Issues, Pull Requesty, Code Review).

## Harmonogram projektowy

Projekt trwa 2,5 miesiąca. Cele do zrealizowania w kolejnych etapach:
- **Punkt kontrolny 1 (Organizacja projektu):** 13.03.2026
- **Punkt kontrolny 2 (Zarządzanie kodem):** 10.04.2026
- **Punkt kontrolny 3 (Testowanie):** 15.05.2026
- **Ocena końcowa:** 29.05.2026

Dokładny harmonogram jest dostępny w widoku kalendarzowym w [GitHub Projects](https://github.com/users/gabriellisiecki/projects/3).

## Zasady i Zarządzanie Kodem (Code Review & Branches)
Dokładny opis zasad i zarządzania kodem jest dostępny w pliku [commit_rules.md](docs/commit_rules.md).


