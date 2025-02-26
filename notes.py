class NoteBook:

    def __init__(self, name: str):
        self.name: str = name
        self.__notes: dict[str, str] = {}

    def __dict__(self) -> dict[str, str]:
        return self.__notes

    def add(self, name: str, content: str):
        self.__notes[name] = content

    def find(self, query_term: str) -> list[str]:
        return [note for note, contents in self.__notes.items() if query_term in contents]

    def get_note(self, name: str) -> str:
        return self.__notes[name]

    def notes(self) -> list[str]:
        return [note_name for note_name in self.__notes]
