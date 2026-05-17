# todo_store = {
#     1: {"title": "Повторить списки и словари", "completed": False},
#     30: {"title": "Сдать финальный проект", "completed": True}
# }



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







