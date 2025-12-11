# Python Assignment – OOP + Function Arguments
# File name: assignment.py


# ------------------------------------------------------------
# PART 1 – OOP IMPLEMENTATION
# ------------------------------------------------------------

# Implement the following classes exactly as specified.

# 1. Class Task
#    - Attributes:
#         title (string)
#         description (string, default "")
#         is_done (boolean, default False)
#    - Methods:
#         __init__(self, title, description="")
#         mark_done(self)
#         mark_undone(self)
#         __str__(self)
#           - returns "☐ <title>" when is_done is False
#           - returns "☑ <title>" when is_done is True

class Task:
    def __init__(self, title: str, description: str = "", is_done: bool = False):
        self.title = title
        self.description = description
        self.is_done = is_done

    def mark_done(self):
        if self.is_done == True:
            return self.title
        
    def mark_undone(self):
        if self.is_done == False:
            return self.title
    
    def __str__(self):
        if self.is_done:
            return f" {self.title}: finished"
        else:
            return f" {self.title} :not finished"
# 2. Class TodoList
#    - Attributes:
#         name (string)
#         tasks (list of Task objects, initially empty)
#    - Methods:
#         __init__(self, name)
#         add_task(self, title, description="")
#         remove_task(self, index)
#         complete_task(self, index)
#         list_tasks(self)
#             prints "index: <task_str>" for each task
class TodoList():
    def __init__(self, name: str, tasks: list = []):
        self.name = name
        self.tasks = tasks

    def add_task(self, title: str, description: str = ""):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        # super().__init__(title, description)
       

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].is_done = True

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")

    def __str__(self):
        return f" {self.name} "


# ------------------------------------------------------------
# Required test code for PART 1
# ------------------------------------------------------------

if __name__ == "__main__":
    todo = TodoList("My Day")

    todo.add_task("Buy milk")
    todo.add_task("Learn Python", "Finish OOP and argument passing assignment")

    print(f"All tasks:{todo}")
    todo.list_tasks()

    print("\nCompleting task 0...")
    todo.complete_task(0)
    todo.list_tasks()

    print("\nRemoving task 0...")
    todo.remove_task(0)
    todo.list_tasks()



# ------------------------------------------------------------
# PART 2 – FUNCTION ARGUMENT BEHAVIOR
# ------------------------------------------------------------

def increment_number(x):
    print("Inside function, before:", x)
    x = x + 1
    print("Inside function, after:", x)

num = 10
print("Before calling:", num)
increment_number(num)
print("After calling:", num)



def append_exclamation(text):
    print("Inside function, before:", text)
    text = text + "!"
    print("Inside function, after:", text)

msg = "Hello"
print("Before calling:", msg)
append_exclamation(msg)
print("After calling:", msg)



def add_item(my_list, item):
    print("Inside function, before:", my_list)
    my_list.append(item)
    print("Inside function, after:", my_list)

numbers = [1, 2, 3]
print("Before calling:", numbers)
add_item(numbers, 4)
print("After calling:", numbers)



def replace_list(my_list):
    print("Inside function, before:", my_list)
    my_list = [0, 0, 0]
    print("Inside function, after:", my_list)

nums = [1, 2, 3]
print("Before calling:", nums)
replace_list(nums)
print("After calling:", nums)



# ------------------------------------------------------------
# PART 3 – OOP + ARGUMENT PASSING
# ------------------------------------------------------------

# Classes Task and TodoList must already be implemented above for this to run.

def complete_all_tasks(todo_list):
    for task in todo_list.tasks:
        task.mark_done()

def replace_todo_list(todo_list):
    todo_list = TodoList("New List")
    todo_list.add_task("Some new task")

my_todo = TodoList("Original List")
my_todo.add_task("Task 1")
my_todo.add_task("Task 2")

print("Before complete_all_tasks:")
my_todo.list_tasks()

complete_all_tasks(my_todo)
print("\nAfter complete_all_tasks:")
my_todo.list_tasks()

print("\nBefore replace_todo_list:")
my_todo.list_tasks()

replace_todo_list(my_todo)
print("\nAfter replace_todo_list:")
my_todo.list_tasks()
