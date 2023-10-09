class Good:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        return "your first value" + self

    def __next__(self):
