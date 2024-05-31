


class Task:
    """
    Klasa Task reprezentuje zadanie ze wszystkimi jego cechami.

    """



    def __init__(self, title, description, priority, due_date, category, status = False):
        """
        Inicjalizuje egzemplarz klasy Task.

        Parametry:
        title (str): Nazwa zadania.
        description (str): Opis zadania.
        priority (int): Priorytet zadania.
        due_date (str): Termin wykonania zadania.
        category (str): Kategoria zadania.
        status (bool): Status zadania (domyślnie False).
    """
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.status = status



    def __str__(self):
        """
        Zwraca czytelną dla użytkownika reprezentację tekstową zadania.
        """
        status_str = 'Completed' if self.status else 'Pending'
        return (f"\nTitle: {self.title}\n Description: {self.description}\n Priority: {self.priority}\n "
                       f"Due Date: {self.due_date}\n Category: {self.category}\n Status: {status_str}")







