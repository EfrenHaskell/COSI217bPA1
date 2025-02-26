import streamlit as st
from notes import NoteBook

new_notebook = NoteBook("")

st.markdown("# NoteBook")
search_term = st.sidebar.text_input("Search...")

if search_term is None or search_term == "":
    note_name = st.sidebar.selectbox("Notes", new_notebook.notes())
else:
    note_name = st.sidebar.selectbox("Notes (Filtered for search term)", new_notebook.find(search_term.title()))

if st.button("show note"):
    if note_name:
        st.markdown(f"## {note_name}")
        st.write(new_notebook.get_note(note_name))
    else:
        st.write("No note to display, select a note in the sidebar or create a new one by clicking add note")
if st.button("add note"):
    new_note_name = st.text_input("Note Name: ")
    new_note_contents = st.text_input("Note Contents: ")
    if st.button("submit"):
        new_notebook.add(new_note_name.title(), new_note_contents.title())
