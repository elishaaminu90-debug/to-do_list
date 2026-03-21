import streamlit as st
from manager import TaskManager
from todo import Task, PRIORITIES
from utils import validate_deadline

st.title("📝 To-Do List App")

manager = TaskManager()

st.header("Add Task")
title = st.text_input("Task Title")
deadline = st.text_input("Deadline (YYYY-MM-DD HH:MM)")
priority = st.selectbox("Priority", PRIORITIES)

if st.button("Add Task"):
    if not validate_deadline(deadline):
        st.error("Invalid deadline format.")
    else:
        manager.add_task(Task(title, deadline, priority))
        st.success("Task added!")

st.header("Tasks")
tasks = manager.list_tasks()

for i, t in enumerate(tasks):
    st.subheader(f"{i}. {t.title}")
    st.write(f"Deadline: {t.deadline}")
    st.write(f"Priority: {t.priority}")
    st.write(f"Completed: {t.completed}")

    col1, col2, col3 = st.columns(3)

    if col1.button("Mark Done", key=f"done{i}"):
        manager.mark_completed(i)
        st.experimental_rerun()

    if col2.button("Delete", key=f"del{i}"):
        manager.delete_task(i)
        st.experimental_rerun()