# importing modules
from items import add as a

from items import edit as e

from items import show as s

from items import delete as d

from items import clear as c

from items import clear_screen as cs

from items import save_tasks as st

def main():
    # initializing variables
    tasks = []
    select = 0

    #  printing all possible options fo creating to-do-list
    print(
        """Input values: (type -1 to cancel execution of add, edit, and delete)

1. Add Task
2. Edit Task
3. Delete Task
4. Show Tasks
5. Clear Tasks
6. Clear Screen
7. Exit\n\n"""
    )
    # main loop
    while True:

        if select == 6:
            print(
                """Input values: (type -1 to cancel execution of add, edit, and delete)

1. Add Task
2. Edit Task
3. Delete Task
4. Show Tasks
5. Clear Tasks
6. Clear Screen
7. Exit\n\n"""
            )
        # try and except to except a ValueError
        try:
            select = int(
                input("Select an option:\t")
            )  # input from user for selecting option

        except ValueError:
            print("Please enter a valid selection.\n")
            continue

        if select == 1:
            a.add(tasks)
            st.save_tasks(tasks)
            continue

        elif select == 2:
            e.edit(tasks)
            st.save_tasks(tasks)
            continue

        elif select == 3:
            d.delete(tasks)
            st.save_tasks(tasks)
            continue

        elif select == 4:
            s.show(tasks)
            continue

        elif select == 5:
            c.clear(tasks)
            st.save_tasks(tasks)
            continue

        elif select == 6:
            cs.clear_screen()
            continue

        elif select == 7:
            print("\nBye!")
            raise SystemExit

        # if an integer selection is greater than 6, print an error statement

        else:
            print("Please enter a valid selection.\n")
            continue


main()
