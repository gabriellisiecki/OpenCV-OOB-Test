# OpenCV-OOB-Test

Celem projektu jest przetestowanie najnowszej stabilnej wersji modułu `opencv-python` z repozytorium PyPI (i w przyszłości z repozytorium GitHub), w tym pipeline CI/CD, testy funkcjonalne oraz wydajnościowe.

## Zespół, role i komunikacja
- **Gabriel Lisiecki (Tech Lead / DevOps):** Architektura testów, wdrożenie GitHub Actions (CI/CD), testy wydajnościowe, Zarządzanie zadaniami dla zepsołu  (Issues), weryfikacja Pull Requestów jako `reviewer`. 
- **Adrian Markowski (Functional QA):** Projektowanie i implementacja wszystkich testów funkcjonalnych w kodzie Python, formatowanie raportów, weryfikacja Pull Requestów jako `reviewer`.
- **Paweł Nawrocki (QA / Docs):** Projektowanie scenariuszy testów akceptacyjnych na podstawie dokumentacji OpenCV, tworzenie i utrzymanie struktury plików w repozytorium, utrzymanie dokumentacji.

- **Kanał komunikacyjny (Discord)**: `https://discord.gg/qwk5zNNku4`

## Zasady i Zarządzanie Kodem (Code Review & Branches)

Zgodnie z wymaganiami z Punktu Kontrolnego nr 2, projekt podlega restrykcyjnemu zarządzaniu kodem:

1. **Issues (Zadania):** Każda praca musi pochodzić ze zgłoszenia (Issue) na GitHubie. Do Issue musi być przypisany wykonawca. 

2. **Gałęzie (Branches):** Nowe funkcjonalności powinny być rozwijane na osobnych gałęziach. Nazewnictwo musi być czytelne, np.:
   - `feature/adds-functional-blur-test`
   - `docs/update-acceptance-scenarios`
   - `bugfix/pipeline-crash`
Każdy Branch jest podpięty pod odpowiadający mu Issue.

3. **Commity:** Krótkie, anglojęzyczne, jasno opisujące co robi dany kawałek kodu (np. `Add initial benchmark structure`).

4. **Pull Requesty i Code Review:**
   - Zabrania się bezpośredniego wypychania kodu na gałąź `main` (push do main).
   - Każdy kod wchodzący na `main` musi przejść przez system Pull Requestów (PR).
   - Każdy PR musi zostać zatwierdzony ("Approved") przez minimum **jednego** członka zespołu, który **nie jest** autorem kodu. To zadanie (Code Review) może wykonać ktokolwiek.
   - Każdy PR jest podpięty pod odpowiadający mu Issue.

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
├── docs/
│   └── test_scenarios.md      # Dokument z opisem scenariuszy testów akceptacyjnych
├── requirements.txt           # Zależności projektu 
└── README.md                  # Główny plik informacyjny
```

## Kanały komunikacji

- **Bieżąca komunikacja:** [DO UZUPEŁNIENIA: np. serwer Discord / grupa na Messengerze / Slack]
- **Zarządzanie zadaniami i kodem:** GitHub (Issues, Pull Requesty, Code Review).

## Harmonogram projektowy

Projekt trwa 2,5 miesiąca. Cele do zrealizowania w kolejnych etapach:
- **Punkt kontrolny 1 (Organizacja projektu):** [DO UZUPEŁNIENIA: Wpisz datę]
- **Punkt kontrolny 2 (Zarządzanie kodem):** [DO UZUPEŁNIENIA: Wpisz datę]
- **Punkt kontrolny 3 (Testowanie):** [DO UZUPEŁNIENIA: Wpisz datę]
- **Ocena końcowa:** [DO UZUPEŁNIENIA: Wpisz datę]

Dokładny harmonogram jest dostępny w widoku kalendarzowym w GitHub Projects.

## Wstępne scenariusze testowe

### Testy funkcjonalne (4 sztuki)
1. **Wczytywanie i zapisywanie różnych formatów (I/O):** Sprawdzenie, czy biblioteka poprawnie wczytuje klatki w formatach `.jpg` oraz `.png` i potrafi zapisać je na dysk bez utraty kluczowych właściwości macierzy (np. poprawne wymiary i typ danych po odczytaniu).
2. **Konwersja przestrzeni barw (Color Space):** Weryfikacja funkcji `cv2.cvtColor`. Test założy konwersję obrazu BGR do skali szarości (GRAY) i sprawdzi, czy wynikowa macierz ma tylko jeden kanał oraz poprawne wartości pikseli.
3. **Nakładanie prostych filtrów (Blurring):** Sprawdzenie działania funkcji takich jak `cv2.GaussianBlur` czy `cv2.medianBlur` na testowym obrazie poprzez weryfikację, czy obraz wynikowy został zmodyfikowany (różni się od wejściowego) i zachował swoje początkowe wymiary.
4. **Wykrywanie Krawędzi (Canny Edge Detection):** Sprawdzenie działania funkcji algorytmicznej `cv2.Canny`. Test wykaże, czy z oryginalnego obrazu program poprawnie wyodrębnia jasne i ciemne kontury, otrzymując binarną (czarno-białą) macierz krawędzi różną od pierwotnego tła.

### Testy wydajnościowe (2 sztuki)
1. **Pomiar czasu procesowania dużych macierzy (4K/8K):** Zmierzenie czasu wykonania kosztownej operacji (np. detekcja krawędzi Canny lub wielokrotne nakładanie rozmycia) na sztucznie wygenerowanej lub wczytanej macierzy o bardzo dużej rozdzielczości. Wynik zostanie zapisany do logów w celu późniejszego porównania.
2. **Benchmark operacji wejścia/wyjścia (I/O Throughput):** Wczytanie i natychmiastowe zapisanie dużego zbioru plików (np. sekwencji 100 obrazów Full HD) do formatów bezstratnych, takich jak `.png` lub `.tiff`. Zmierzony zostanie łączny narzut czasowy operacji dyskowych w OpenCV w porównaniu do pojedynczego pliku.

---

## 📌 TODO: Zadania startowe Gabriela


- [x] Opracowanie wstępnych pomysłów na obszary funkcjonalne do testów dla OpenCV.
- [x] Dopisanie podziału poszczególnych "Stanowisk" do README dla każdego członka.
- [x] Konfiguracja Środowiska Github Issues, utowrzenie projektu.
- [x] Dodanie reguł "Code Review" i ochrony gałęzi `main` w ustawieniach na serwerze GitHub po założeniu wspólnego repozytorium.

## 📌 TODO: Zadania startowe Adriana

- [ ] Dodanie poszczególnych tasków rozpisanych w README do projektu w GitHub Issues.
- [ ] Rozplanowanie założonych zgłoszeń (Issues) na przestrzeni czasu w widoku GitHub Projects, ustalając przewidywane terminy i daty końcowe.
- [ ] Przypisanie w `README.md` używanego kanału komunikacyjnej grupy (stworzenie kanału w Discord)

## 📌 TODO: Zadania startowe Pawła

- [ ] Wygenerowanie i wypchnięcie do repozytorium początkowej struktury katalogów (zgodnie z rozpiską z sekcji *"Struktura katalogów projektu"*).
- [ ] Uzupełnienie ram czasowych w `README.md` w sekcji *"Harmonogram"*.
- [ ] Zainicjowanie projektu, dodanie do requirements.txt wymaganych zależności.
