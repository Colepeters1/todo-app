import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


unique_value = 0
for todo in todos:
    unique_value += 1
    st.checkbox(todo, key=f"todo{unique_value}")


st.text_input(label="", placeholder="Add a new todo...")

