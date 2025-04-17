tasks=[]

def add_task(task):
    tasks.append({'task':task,'done':False})

def show_task():
    for task in tasks:
        if task['done']==True:
            status="✅"
        else:
         status="❌"

        print(task['task']+"."+status)

def complete_task(index):
   tasks[index-1]['done']=True

add_task("learn python")
add_task("Do pushups")
complete_task(1)
complete_task(2)
show_task()
