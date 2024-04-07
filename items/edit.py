def edit(tasks):
    if not tasks:
        print('You have no tasks to edit.\n')
        return

    while True:
        # initializing variable edit_task
        edit_task = 0

        try:
            # asking for input and using try and except to except ValueError and IndexError
            edit_task = int(input('\nEnter task number to edit:\t'))
            if edit_task == -1:
                print()
                return

            elif edit_task < 1 or edit_task > len(tasks):
                print('index is out of range.\n')
                continue

        except ValueError:
            print('Please enter a valid selection.\n')
            continue

        edit_task -= 1  # subtracting 1 from the index that the user entered because the list starts at index 0
        # so if user enters 1, they mean they want to edit the first element in the list.

        the_task = tasks.pop(edit_task)  # popping the task that user wants to edit
        print(the_task)  # and printing it

        choice = input('\nIs this the task you want to edit? (y/n):\t').lower().strip()

        if choice == 'y':
            break
        else:
            tasks.insert(edit_task, the_task)  # if user enters no, the popped task gets inserted back into the
            # the list
            continue

    new_task = input("Enter new task:\t")
    tasks.insert(edit_task, new_task)
    print('\nTask edited successfully.\n')
