from Task import Task


class FileHandler:
    """
    Klasa FileHandler obsługuje operacje związane z zapisywaniem, ładowaniem i usuwaniem zadań z pliku.
    Metody:
    task_exists(filename)
    save_tasks_to_file(tasks, filename)
    load_tasks_from_file(filename)
    remove_task_from_file(title, filename)
    """

    @staticmethod
    def task_exists(filename):
        """
        Sprawdza, czy zadania istnieją w pliku.

        Parametry:
        filename (str): Nazwa pliku do sprawdzenia.

        Zwraca:
        list: Lista tytułów istniejących zadań.
        """
        existing_tasks = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        key, value = line.split(': ', 1)
                        if key.strip() == 'Title':
                            existing_tasks.append(value.strip())
        except FileNotFoundError:
            pass
        return existing_tasks



    @staticmethod
    def save_tasks_to_file(tasks, filename):
        """
       Zapisuje zadania do pliku.

       Parametry:
       tasks (list): Lista zadań do zapisania.
       filename (str): Nazwa pliku do zapisu zadań.
       """
        existing_tasks = FileHandler.task_exists(filename)
        tasks_to_save = []
        for task in tasks:
            if task.title in existing_tasks:
                choice = input("Do you want to overwrite existing task {}? (y/n): ".format(task.title))
                if choice.lower() == "y":
                    print("Task {} overwritten successfully".format(task.title))
                    existing_tasks.remove(task.title)
                    tasks_to_save.append(task)
                elif choice.lower() == "n":
                    print("Task {} not overwritten".format(task.title))
                    tasks_to_save.append(task)
                    continue
                else:
                    print("Please enter y or n.")
                    return
            else:
                tasks_to_save.append(task)

        print()
        with open(filename, 'w') as file:
            for task in tasks_to_save:
                file.write(task.__str__() + '\n')
                print(f"Task {task.title} saved successfully")



    @staticmethod
    def load_tasks_from_file(filename):
        """
        Ładuje zadania z pliku.

        Parametry:
        filename (str): Nazwa pliku do załadowania zadań.

        Zwraca:
        list: Lista załadowanych zadań.
        """
        tasks = []
        try:
            with open(filename, 'r') as file:
                task_data = {}
                for line in file:
                    line = line.strip()
                    if line:
                        key, value = line.split(': ', 1)
                        task_data[key.strip()] = value.strip()
                    else:
                        if task_data:
                            title = task_data.get('Title', 'None')
                            task = Task(
                                title,
                                task_data.get('Description', 'None'),
                                task_data.get('Priority', 'None'),
                                task_data.get('Due Date', 'None'),
                                task_data.get('Category', 'None'),
                                True if task_data.get('Status', 'Pending') == 'Completed' else False
                            )
                            tasks.append(task)
                            task_data = {}

                if task_data:
                    task = Task(
                        task_data.get('Title', 'None'),
                        task_data.get('Description', 'None'),
                        task_data.get('Priority', 'None'),
                        task_data.get('Due Date', 'None'),
                        task_data.get('Category', 'None'),
                        True if task_data.get('Status', 'Pending') == 'Completed' else False
                    )
                    tasks.append(task)
        except FileNotFoundError:
            pass
        return tasks


    @staticmethod
    def remove_task_from_file(title, filename):
        """
        Usuwa zadanie z pliku na podstawie tytułu.

        Parametry:
        title (str): Tytuł zadania do usunięcia.
        filename (str): Nazwa pliku, z którego ma być usunięte zadanie.
        """
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
            with open(filename, 'w') as file:
                task_found = False
                for line in lines:
                    if f"Title: {title}" in line:
                        task_found = True
                    elif task_found and line.strip() == "":
                        task_found = False
                    elif not task_found:
                        file.write(line)
        except FileNotFoundError:
            print(f"File '{filename}' not found")