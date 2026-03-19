# Zasady i Zarządzanie Kodem (Code Review & Branches)

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