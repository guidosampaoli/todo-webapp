import streamlit as st
import functions

st.set_page_config(
    page_title="To-Do Webb App",
    page_icon="https://github.com/guidosampaoli/todo-webapp/blob/master/favicon.png"
)

todos = functions.get_todos()

if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""

def add_todo():
    if st.session_state["new_todo"]:  # Check if the input is not empty
        todo = (st.session_state["new_todo"].strip()[0].upper() + st.session_state["new_todo"].strip()[1:]) + "\n"
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

st.title("My ToDo App")
st.subheader("This is my ToDo Web App.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add new Todo...", label_visibility="hidden",
              placeholder="Add new ToDo...", key="new_todo",
              on_change=add_todo)

