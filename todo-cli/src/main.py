from todo import TodoManager
from storage import Storage

def display_manu():
    print("\n==== To-Do CLI ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("0. Exit")

def main():
    manager = TodoManager()
    running = True

    while running:
        display_manu()
        choice = input("Please enter your choice:")
        if choice == "1":
            manager.show_tasks()
        elif choice == "2":
            task = input("Please Enter task content:")
            manager.add_task(task)
        elif choice == "3":
            index = input("Please enter the index you wanna delete:")
            manager.delete_task(index)
        elif choice == "0":
            print("Exiting program...")
            running = False
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
