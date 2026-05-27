
import typer
import json
import datetime
import time

app = typer.Typer()
tasks_data_file = "tasks_data.json"

@app.command()
def add(name: str):
    task = {
        "name": name,
        "created_at": datetime.datetime.now().replace(microsecond=0).isoformat(),
        "status": "todo",
        "id": int(time.time())
    }
    try:
        with open(tasks_data_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
        tasks.append(task)
        with open(tasks_data_file, "w") as f:
            json.dump(tasks, f, indent=2)
    else:
        tasks.append(task)
        with open(tasks_data_file, "w") as f:
            json.dump(tasks, f, indent=2)
    print(f"Task '{name}' added successfully.")

@app.command()
def list():
    try:
        with open(tasks_data_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("No tasks found.")
        return
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['name']} - {task['status']} (Created at: {task['created_at']}, ID: {task['id']})")

@app.command()
def strt(name: str):
    try:
        with open(tasks_data_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("No tasks found.")
        return
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks):
        if task["name"] == name:
            task["status"] = "in_progress"
            with open(tasks_data_file, "w") as f:
                json.dump(tasks, f, indent=2)
            print(f"Task '{name}' started.")
            return
        
@app.command()
def cmplt(name: str):
    try:
        with open(tasks_data_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("No tasks found.")
        return
    if not tasks:
        print("No tasks found")
        return
    for idx, task in enumerate(tasks):
        if task["name"] == name:
            task["status"] = "done"
            with open(tasks_data_file, "w") as f:
                json.dump(tasks, f, indent=2)
                print(f"{name} task completed.")
                return

@app.command()
def dlt(name: str):
    try:
        with open(tasks_data_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("Tasks not found.")
        return
    if not tasks:
        print ("No tasks found.")
        return
    for idx, task in enumerate(tasks):
        if task["name"] == name:
            del tasks[idx]
            with open(tasks_data_file, "w") as f:
                json.dump(tasks, f, indent=2)
                print(f"{name} task cleared.")
                return

@app.command()
def clr():
    try:
        with open(tasks_data_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("No tasks found.")
        return
    if not tasks:
        print("No tasks found.")
        return
    tasks = []
    with open(tasks_data_file, "w") as f:
        json.dump(tasks, f, indent=2)
        print("All tasks cleared.")
        
    
if __name__ == "__main__":
    app()

    