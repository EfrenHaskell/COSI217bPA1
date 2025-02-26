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

    :return:
    """
    return new_notebook.notes()


@app.get("/find")
def find_note(term: str):
    return {"term": term, "matching notes": [new_notebook.find(term)]}


@app.get("/note/{name}")
def return_note(name: str):
    return new_notebook.get_note(name)


@app.post("/add")
def add_note(new_note: NoteItem):
    new_notebook.add(new_note.name, new_note.content)
    return "success"
