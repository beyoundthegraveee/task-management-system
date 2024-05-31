from collections import Counter
from datetime import datetime

from FileHandler import FileHandler


class TaskManager:
    """
    Klasa TaskManager zarządza listą zadań i operacjami na nich.
    Metody:
    add_task(task)
    remove_task(title)
    edit_task(title)
    mark_task(title)
    show_tasks()
    filter_tasks(priority, due_date, status)
    save_tasks_to_file(tasks, file_name)
    load_tasks(file_name)
    generate_statistics()
    validate_date(date_str)
    """

    def __init__(self):
        """
        Inicjalizuje instancję klasy TaskManager.
        """
        self.tasks = []


    def add_task(self, task):
        """
        Dodaje nowe zadanie do listy zadań.

        Parametry:
        task (Task): Zadanie do dodania.
        """
        self.tasks.append(task)
        print("\nTask added successfully")


    def remove_task(self, title):
        """
        Usuwa zadanie z listy zadań na podstawie tytułu.

        Parametry:
        title (str): Tytuł zadania do usunięcia.
        """
        task = self.find_task_by_title(title)
        self.tasks.remove(task)
        FileHandler.remove_task_from_file(title, "data.txt")
        print("\nTask removed successfully")

    def find_task_by_title(self, title):
        """
        Znajduje zadanie na podstawie tytułu.

        Parametry:
        title (str): Tytuł zadania do znalezienia.

        Zwraca:
        Task: Znalezione zadanie.

        Wyjątki:
        TaskNotFoundError: Jeśli zadanie o podanym tytule nie zostanie znalezione.
        """
        for task in self.tasks:
            if task.title == title:
                return task
        raise TaskNotFoundError(f"Task with title '{title}' not found.")



    def edit_task(self, title):
        """
        Edytuje zadanie na podstawie tytułu.

        Parametry:
        title (str): Tytuł zadania do edycji.

        Wyjątki:
        TaskCompletedError: Jeśli zadanie jest ukończone i nie może być edytowane.
        InvalidDateError: Jeśli nowa data jest w niepoprawnym formacie.
        """
        try:
            task = self.find_task_by_title(title)
            if task.status == True:
                raise TaskCompletedError("\nCompleted tasks cannot be changed")
            print("\nSelect the field to change: \n" +
                  "[1] Title: " + task.title + "\n" +
                  "[2] Description: " + task.description + "\n" +
                  "[3] Priority: " + task.priority + "\n" +
                  "[4] Date: " + task.due_date + "\n" +
                  "[5] Category: " + task.category + "\n"
                  )
            choice = int(input("Enter your choice: "))
            if choice == 1:
                task.title = input("New title: ")
            elif choice == 2:
                task.description = input("New description: ")
            elif choice == 3:
                priority_choice = input("Choose new priority:\n"+
                                      "[1] Low\n"+
                                      "[2] Medium\n"+
                                      "[3] High\n")
                priority_dict = {"1": "Low", "2": "Medium", "3": "High"}
                task.priority = priority_dict.get(priority_choice)
            elif choice == 4:
                new_date = input("New date: ")
                self.validate_date(new_date.strip())
                task.due_date = new_date
            elif choice == 5:
                task.category = input("New category: ")
            else:
                print("Invalid input.\nPlease enter valid choice. ")
                return

            print("\nTask edited successfully\n")
        except TaskCompletedError as e:
            print(e)
        except InvalidDateError as e:
            print(e)


    def mark_task(self, title):
        """
        Oznacza zadanie jako ukończone lub nieukończone.

        Parametry:
        title (str): Tytuł zadania do oznaczenia.

        Wyjątki:
        TaskNotFoundError: Jeśli zadanie o podanym tytule nie zostanie znalezione.
        """
        task = self.find_task_by_title(title)
        print("\nEnter task status:\n" +
              "[T] Completed\n" +
              "[F] Not Completed\n")
        choice = input("Enter your choice: ")
        if choice == "T":
            if task.status == True:
                print("\nTask status already set as completed.\n")
                return
            else:
                task.status = True
        elif choice == "F":
            if task.status == False:
                print("\nTask status already set as not completed.\n")
                return
            else:
                task.status = False
        else:
            print("Invalid input.\nPlease enter valid choice. ")
            return

        print("Task marked successfully")

    def show_tasks(self):
        """
        Wyświetla wszystkie zadania.
        """
        print("___________")
        for task in self.tasks:
            print(task)

    def filter_tasks(self, priority=None, due_date=None, status=None):
        """
        Filtruje zadania na podstawie priorytetu, daty i statusu.

        Parametry:
        priority (str, opcjonalnie): Priorytet do filtrowania (Low, Medium, High).
        due_date (str, opcjonalnie): Data do filtrowania (YYYY-MM-DD).
        status (bool, opcjonalnie): Status do filtrowania (True dla ukończonych, False dla nieukończonych).

        Zwraca:
        list: Lista przefiltrowanych zadań.

        Wyjątki:
        InvalidInputError: Jeśli żadne kryterium filtrowania nie zostanie wybrane.
        InvalidDateError: Jeśli data jest w niepoprawnym formacie.
        """
        if not priority and not due_date and status is None:
            raise InvalidInputError("No filter criteria selected.")
        try:
            filtered_tasks = self.tasks
            if priority:
                filtered_tasks = [task for task in filtered_tasks if task.priority == priority]
            if due_date:
                self.validate_date(due_date)
                filtered_tasks = [task for task in filtered_tasks if task.due_date == due_date]
            if status is not None:
                filtered_tasks = [task for task in filtered_tasks if task.status == status]
            return filtered_tasks
        except InvalidDateError as e:
            print(e)

    def generate_statistics(self):
        """
        Generuje statystyki dotyczące zadań.

        Wyświetla:
        - Łączną liczbę zadań.
        - Liczbę ukończonych zadań.
        - Liczbę nieukończonych zadań.
        - Procent ukończonych zadań.
        - Najczęściej występujący priorytet zadań.
        """
        total_tasks = len(self.tasks)
        completed_tasks = sum(task.status for task in self.tasks if task.status == True)
        pending_tasks = total_tasks - completed_tasks
        percent_completed = (completed_tasks / total_tasks) * 100 if total_tasks != 0 else 0
        priorities = [task.priority for task in self.tasks]
        most_common_priority = Counter(priorities).most_common(1)
        print(f"Total tasks: {total_tasks}" +
              f"\nCompleted tasks: {completed_tasks}" +
              f"\nPending tasks: {pending_tasks}" +
              f"\nPercentage of completed tasks: {percent_completed}%" +
              f"\nMost common priority: {most_common_priority}")

    def load_tasks(self, filename):
        """
        Ładuje zadania z pliku.

        Parametry:
        filename (str): Nazwa pliku do załadowania zadań.
        """
        new_tasks = FileHandler.load_tasks_from_file(filename)
        if new_tasks is not None:
            for task in new_tasks:
                if not any(t.title == task.title for t in self.tasks):
                    self.tasks.append(task)
                    print(f"Task with title '{task.title}' added to list.")
                else:
                    print(f"Task with title '{task.title}' already exists in list.")
                    return
            print("\nTasks loaded successfully")
        else:
            print("\nFile is empty")


    def validate_date(self, date):
        """
        Sprawdza poprawność formatu daty.

        Parametry:
        date (str): Data do sprawdzenia.

        Wyjątki:
        InvalidDateError: Jeśli data jest w niepoprawnym formacie.
        """
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise InvalidDateError(f"Incorrect date format: {date}. Expected format: YYYY-MM-DD")




class TaskNotFoundError(Exception):
    """
    Wyjątek TaskNotFoundError jest podnoszony, gdy zadanie o podanym tytule nie zostanie znalezione.
    """
    pass

class InvalidInputError(Exception):
    """
    Wyjątek InvalidInputError jest podnoszony, gdy użytkownik wprowadzi nieprawidłowe dane wejściowe.

    Atrybuty:
    message (str): Komunikat opisujący błąd.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class TaskCompletedError(Exception):
    """
    Wyjątek TaskCompletedError jest podnoszony, gdy użytkownik próbuje edytować zadanie, które jest ukończone.
    """
    pass


class InvalidDateError(Exception):
    """
    Wyjątek InvalidDateError jest podnoszony, gdy użytkownik wprowadzi datę w niepoprawnym formacie.
    """
    pass


