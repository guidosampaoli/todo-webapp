import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = (st.session_state["new_todo"][0].upper() + st.session_state["new_todo"][1:]).strip() + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My ToDo App")
st.subheader("This is my ToDo Web App.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add new Todo...", label_visibility="hidden",
              placeholder="Add new ToDo...", key="new_todo",
              on_change=add_todo)

st.session_state

