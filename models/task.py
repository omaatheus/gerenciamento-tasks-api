class Task:
    def __init__(self, id, title, description, done=False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.done = done

    def toDict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
        }