import sys, os
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """" Read a text file and return the list of To-Do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def show_todos():
    """ Show To-Do list from text file """
    todos_local = get_todos()
    for index_local, item in enumerate(todos_local):
        print(f"{index_local + 1}) {item.strip()}")


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the To-Do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def get_img_path(image_name):
    """ Get the path of the images """
    if getattr(sys, 'frozen', False):
        # if it's an executable file, get the path from sys._MEIPASS
        return os.path.join(sys._MEIPASS, 'assets', image_name)
    else:
        # if it's not an executable file, use the local path
        return os.path.join(os.path.dirname(__file__), 'assets', image_name)

