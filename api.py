from notes import NoteBook
from fastapi import FastAPI
from pydantic import BaseModel


class NoteItem(BaseModel):
    name: str
    content: str


app = FastAPI()
new_notebook = NoteBook("My Notebook")


@app.get("/")
async def home_message():
    """
    Describe functionality of NoteBook API
    :return:
    """
    return {"message": "See all notes with /list, find a note by search term with /find?term, get note contents with /note/name and add a new note to the notebook with /add, "}


@app.get("/list")
def list_notes():
    """
    Get request returns list of all notes
    :return:
    """
    return new_notebook.notes()


@app.get("/find")
def find_note(term: str):
    """
    Get request returns all notes that match search term
    :param term:
    :return:
    """
    return {"term": term, "matching notes": [new_notebook.find(term)]}


@app.get("/note/{name}")
def return_note(name: str):
    """
    Get request returns note contents for note specified by name
    :param name:
    :return:
    """
    return new_notebook.get_note(name)


@app.post("/add")
def add_note(new_note: NoteItem):
    """
    Post request to add new note
    :param new_note:
    :return:
    """
    new_notebook.add(new_note.name, new_note.content)
    return "success"
