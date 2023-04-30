class Application:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __getitem__(self, items):
        return type(items), items
