def show_tasks(store):
    """Выводит все задачи на экран"""

    if not store:
        print("\n[!] Ваш список задач пока пуст")
        return
    
    for task_id, task_data in store.items():
        if task_data["completed"] == True:
            status = "[V] Выполнена"
        else:
            status = "[X] В процессе"
        
        print(f"ID: {task_id} | {task_data['title']} - {status}")

def add_task(store, title):
    """Добавляет новую задачу в общую бд"""
    if not title.strip():
        print("[!] Название задачи не может быть пустым")
        return

    if store:
        new_id = max(store.keys()) + 1
    else:
        new_id = 1
    
    store[new_id] = {
        "title": title.strip(),
        "completed": False
    }

    print(f"[+] Задача '{title}' успешно добавлена с ID: {new_id}")


def complete_task(store, task_id):
    """Отмечает задачу как выполненную по ее ID"""

    if task_id in store:
        store[task_id]['completed'] = True
        print(f"[V] Задача №{task_id} ('{store[task_id]['title']}') выполнена!")
    else:
        print("[!] Ошибка: Задачи с таким ID не существует")



def main():
    todo_store = {}

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Выйти")

        choice = input("\nВыберите действие (1-4): ").strip()

        if choice == "4":
            print("Программа завершена, хорошего дня!")
            break

        elif choice == "1":
            show_tasks(todo_store)
        elif choice == "2":
            task_title = input("Введите название задачи: ").strip()
            add_task(todo_store, task_title)
        elif choice == "3":
            show_tasks(todo_store)

            if todo_store:
                task_id = int(input("\n Введите ID выполненной задачи: "))
                complete_task(todo_store, task_id)

if __name__ == "__main__":
    main()
