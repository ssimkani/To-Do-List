def show(tasks):
    # if no elements are in the list, there are no tasks to show
    if not tasks:
        print("You have no tasks to show.")

        # iterates over all tasks in the list and prints them out with an f-string.
        # the 'start=1' means that the tasks are numbered starting at 1 instead of 0.
    print()
    for index, item in enumerate(tasks, start=1):
        print(f"{index} :\t{item}")
    print()
