import os


def save_tasks(tasks):
    directory = os.path.dirname(__file__)
    file_path = os.path.join(directory, "../list/tasksList.txt")
    with open(file_path, "w") as file:
        for index, item in enumerate(tasks, start=1):
            file.write(f"{index} :    {item}\n")

