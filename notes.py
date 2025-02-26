class PrintObject:
    def __init__(self, item):
        self.__item = item

    def text(self):
        """
        Prints text value of item
        :return:
        """
        if type(self.__item) == str:
            print(self.__item)


class NoteBook:

    def __init__(self, name: str):
        self.name: str = name
        self.__notes: dict[str, str] = {}

    def __getitem__(self, item):
        """
        Return PrintObject of note contents
        :param item:
        :return:
        """
        return PrintObject(self.__notes[item])

    def add(self, name: str, content: str):
        """
        Add new note
         - A note is composed of a name and content
        :param name:
        :param content:
        :return:
        """
        self.__notes[name] = content

    def find(self, query_term: str) -> list[str]:
        """
        find note that has query_term in its contents
        :param query_term:
        :return:
        """
        return [note for note, contents in self.__notes.items() if query_term in contents]

    def get_note(self, name: str) -> str:
        """
        Return note contents by name
        :param name:
        :return:
        """
        return self.__notes[name]

    def notes(self) -> list[str]:
        """"
        Return a list of all note names
        """
        return [note_name for note_name in self.__notes]
