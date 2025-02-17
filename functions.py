import sys, os
import subprocess
FILEPATH = "todos.txt"


def push_to_github():
    """Commits and pushes changes to GitHub."""
    try:
        subprocess.run(["git", "add", "todos.txt"], check=True)
        subprocess.run(["git", "commit", "-m", "Updated todos from Streamlit app"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)  # Cambiá 'main' por la rama correcta
    except subprocess.CalledProcessError as e:
        print("Error to push changes to GitHub:", e)

def write_todos(todos):
    """Writes the updated to-do list to the text file and pushes changes to GitHub."""
    with open(FILE_PATH, "w") as file:
        file.writelines(todos)
    
    push_to_github()  # Subir cambios después de escribir el archivo


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
    """Writes the updated to-do list to the text file and pushes changes to GitHub."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)    
    
    push_to_github()  # Push changes after write the file
    

def get_img_path(image_name):
    """ Get the path of the images """
    if getattr(sys, 'frozen', False):
        # if it's an executable file, get the path from sys._MEIPASS
        return os.path.join(sys._MEIPASS, 'assets', image_name)
    else:
        # if it's not an executable file, use the local path
        return os.path.join(os.path.dirname(__file__), 'assets', image_name)


