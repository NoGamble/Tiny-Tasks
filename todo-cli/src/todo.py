from storage import Storage

class TodoManager:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load()
    
    def show_tasks(self):
        if not self.tasks:
            print("To-do List is empty now!")
            return
        for idx, task in enumerate(self.tasks):
            print(f"{idx +1}. {task}")
    
    def add_task(self, task):
        self.tasks.append(task)
        self.storage.save(self.tasks)
        print("The task added successfully!")
    
    def delete_task(self, index):
        try:
            index = int(index) - 1
            self.tasks.pop(index)
            self.storage.save(self.tasks)
            print("The task deleted successfully!")
        except:
            print("Eror! Please check the index!")
        
        