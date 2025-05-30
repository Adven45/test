tasks = []

def add_task(task):
    tasks.append({'task': task, 'done': False})

def show_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def complete_task(index):
    tasks[index - 1]['done'] = True

# Example:
add_task("Learn Python")
add_task("Do pushups")
complete_task(1)
show_tasks()
