def clear(tasks):
    if not tasks:
        print('you have no tasks to clear.\n')
        return
    choice = input('\nAre you sure you want to clear your to-do list? (y/n)\t').lower().strip()
    if choice == 'y':
        tasks.clear()
        print('\ntasks list cleared successfully.\n')
    else:
        return
