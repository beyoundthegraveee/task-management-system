from FileHandler import FileHandler
from Task import Task
from TaskManager import TaskManager, TaskNotFoundError, InvalidInputError, InvalidDateError


def main():
    """
    Główna funkcja zarządzania zadaniami.
    Obsługuje interfejs użytkownika do zarządzania zadaniami, umożliwiając tworzenie,
    usuwanie, edytowanie, oznaczanie, wyświetlanie, filtrowanie, zapisywanie,
    ładowanie i generowanie statystyk zadań.
    """
    task_manager = TaskManager()

    while True:
        print("\n_____Task Management System_____\n"
              "[1] Create a new task\n" +
              "[2] Remove a task\n" +
              "[3] Edit a task\n" +
              "[4] Mark task\n" +
              "[5] View a list of tasks\n" +
              "[6] Filter tasks\n" +
              "[7] Save tasks\n" +
              "[8] Load tasks\n" +
              "[9] Generate statistics\n" +
              "[Q] Quit\n"
              )
        choice = input("Enter your choice: ")
        file_name = "data.txt"

        if choice == "1":
            task_data = input("Enter task details (title, description, due_date (YYYY-MM-DD), category): ")
            priority_choice = input("Choose the priority of the task:\n"+
                                    "[1] Low\n" +
                                    "[2] Medium\n" +
                                    "[3] High\n").strip()
            priority_dict = {"1": "Low", "2": "Medium", "3": "High"}
            priority = priority_dict.get(priority_choice)
            if priority is None:
                print("Invalid priority value.")
                continue
            try:
                title, description, due_date, category = task_data.split(',')
                task_manager.validate_date(due_date.strip())
                if any(task.title == title for task in task_manager.tasks):
                    print(f"Task with title '{title}' already exists.")
                    continue
                task = Task(title.strip(), description.strip(), priority.strip(), due_date.strip(), category.strip())
                task_manager.add_task(task)
            except ValueError:
                print("Invalid input. Please enter all details separated by [,] ")
            except InvalidDateError as e:
                print(e.__str__())
        elif choice == "2":
            try:
                title = input("Enter task title to remove: ")
                task_manager.remove_task(title)
            except TaskNotFoundError as e:
                print(e)
        elif choice == "3":
            try:
                title = input("Enter task title to change: ")
                task_manager.edit_task(title)
            except TaskNotFoundError as e:
                print(e)
        elif choice == "4":
            try:
                title = input("\nEnter task title to mark: ")
                task_manager.mark_task(title)
            except TaskNotFoundError as e:
                print(e)
        elif choice == "5":
            task_manager.show_tasks()
        elif choice == "6":
            priority_choice = input("Enter priority to filter by (or leave blank to skip): \n"+
                             "[1] Low\n" +
                             "[2] Medium\n" +
                             "[3] High\n")
            priority_dict = {"1": "Low", "2": "Medium", "3": "High"}
            priority = priority_dict.get(priority_choice) if priority_choice in priority_dict else None
            due_date = input("Enter due date (YYYY-MM-DD) to filter by (or leave blank to skip): ")
            status_choice = input("Enter status (completed/pending) to filter by (or leave blank to skip): ").strip()
            status = True if status_choice.lower() == 'completed' else False if status_choice.lower() == 'pending' else None
            try:
                filtered_tasks = task_manager.filter_tasks(priority, due_date, status)
                if filtered_tasks:
                    for task in filtered_tasks:
                        print(task)
                else:
                    print("No tasks found matching the criteria.")
            except InvalidInputError as e:
                print(e)
        elif choice == "7":
            FileHandler.save_tasks_to_file(task_manager.tasks, file_name)
        elif choice == "8":
            task_manager.load_tasks(file_name)
        elif choice == "9":
            task_manager.generate_statistics()
        elif choice == "Q":
            break
        else:
            print("Invalid input.\nPlease enter valid choice. ")





if __name__ == "__main__":
    main()



