class Media:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Book(Media):

    def showInfo(self):
        return print(f"Book: {self.title} Author: {self.author}")
    
    def toDict(self):
        return {
            'type': 'book',
            'title': self.title,
            'author': self.author
        }

    def __repr__(self):
        return f"< Book: {self.title} Author: {self.author} >"


class Film(Media):
    def showInfo(self):
        return print(f"Film: {self.title} Author: {self.author}")

    def toDict(self):
        return {
            'type': 'film',
            'title': self.title,
            'author': self.author
        }

    def __repr__(self):
        return f"< Film: {self.title} Author: {self.author} >"


class Music(Media):
    def showInfo(self):
        return print(f"Music: {self.title} Author: {self.author}")

    def toDict(self):
        return {
            'type': 'music',
            'title': self.title,
            'author': self.author
        }

    def __repr__(self):
        return f"< Music: {self.title} Author: {self.author} >"
