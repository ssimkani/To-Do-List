def add(tasks):

    add_task = input('Enter task:\t')

    if add_task == '-1':
        print()
        return
    tasks.append(add_task)
    print('\nTask added successfully.\n')
