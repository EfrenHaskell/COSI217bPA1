import streamlit as st
from notes import NoteBook

if "notes" not in st.session_state:
    """
    Maintain persistent notebook object
    """
    st.session_state.notes = NoteBook("")

st.markdown("# NoteBook")


with st.form("Add Note"):
    st.markdown("## Add Note")
    col1, col2 = st.columns([1, 1])
    with col1:
        note_name = st.text_input("Note Name:")
    with col2:
        note_contents = st.text_input("Note Contents:")
    submit = st.form_submit_button(label="Submit")

if submit:
    st.session_state.notes.add(note_name, note_contents)
    st.write("Note added Successfully!")

search_term = st.sidebar.text_input("Search...")

if search_term == "":
    note_name = st.sidebar.selectbox("Notes", st.session_state.notes.notes())
else:
    note_name = st.sidebar.selectbox("Notes (Filtered for search term)", st.session_state.notes.find(search_term))

if st.button("show note"):
    if note_name:
        st.markdown(f"## {note_name}")
        st.write(st.session_state.notes.get_note(note_name))
    else:
        st.write("No note to display, select a note in the sidebar or create a new one by clicking add note")
