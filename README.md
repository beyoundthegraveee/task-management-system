Opis projektu:
Napisz aplikację do zarządzania zadaniami, która umożliwia dodawanie, usuwanie, edytowanie, filtrowanie,
wyświetlanie i zapisywanie zadań do pliku tekstowego.
Funkcje aplikacji:
 Dodawanie nowych zadań wraz z priorytetem, terminem wykonania, priorytet, kategoria
(praca/osobiste/etc) i opisem.
 Usuwanie i edycja istniejących zadań, w tym zmiana priorytetu, terminu wykonania i opisu.
 Oznaczanie zadań jako zakończone.
 Wyświetlanie listy zadań wraz z ich szczegółami.
 Filtrowanie zadań na podstawie priorytetu, terminu wykonania lub statusu.
 Zapisywanie i wczytywanie zadań do/z pliku tekstowego.
 Dodaj funkcje generowania statystyk i analizy danych dotyczących zadań, takich jak średni czas
wykonania zadania, procentowe zakończenie zadań na czas, najczęstsze priorytety.
 Dodaj obsługę błędów takie jak edycja zakończonych zadań, wywołanie nieistniejącego zadania,
niepoprawnie wpisana data.
 Utwórz prosty interface.
Struktura projektu:
Klasa Task, która będzie reprezentować pojedyncze zadanie. Klasa powinna zawierać odpowiednie
atrybuty (np. nazwa zadania, opis, priorytet, termin wykonania, czy zadanie jest zakończone) oraz metody
do zarządzania danymi zadania.
Klasa TaskManager, która będzie zarządzała zadaniami. Będzie zawierała metody do dodawania,
usuwania, edytowania, oznaczania jako zakończone oraz wczytywania i zapisywania zadań do pliku.
Klasa FileHandler, która będzie odpowiedzialna za operacje związane z plikiem, takie jak zapisywanie i
wczytywanie danych.
Klasy wyjątków do obsługi sytuacji błędnych, np. TaskNotFoundError, InvalidDateError, itp.
