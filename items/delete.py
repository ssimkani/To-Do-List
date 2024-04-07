def delete(tasks):
    if not tasks:
        print('Your tasks list is empty.\n')
        return

    while True:
        try:
            delete_task = int(input('\nEnter task number to delete:\t'))
            if delete_task == -1:
                print()
                return

            elif delete_task < 1 or delete_task > len(tasks):
                print('Index is out of range.\n')
                continue

        except ValueError:
            print('Please enter a valid selection.\n')
            continue

        delete_task -= 1
        deleted_task = tasks.pop(delete_task)
        print(deleted_task)

        choice = input('\nIs this the task you want to delete? (y/n):\t').lower().strip()

        if choice == 'y':
            break
        else:
            tasks.insert(delete_task, deleted_task)  # if user enters no, the popped task gets inserted back into the
            # the list
            continue

    print('\nTask deleted successfully.\n')
