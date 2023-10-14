from models.database import Database
from factories.media_factory import MediaFactory
from controller.interface import Interface
import os

"""
You can implement any commands you want in the interface, those below are just some examples.
"""


def addBookToDatabase():
    media = Media.createMedia(
        input('Tipo: '), input('Titulo: '), input('Autor: '))
    db.create(2, media.toDict())


def readIndexFromDatabase():
    indexList = db.read('keys')
    indexList = sorted(list(map(int, indexList)))
    return indexList


def sumAllIndex():
    indexList = readIndexFromDatabase()
    return print(sum(indexList))


db = Database()
db.set(os.getenv('DATABASE_FILE'))

Media = MediaFactory()

i = Interface()
i.commands = {
    "create": {"func": addBookToDatabase, "parameters": 0},
    "read index": {"func": readIndexFromDatabase, "parameters": 0},
    "sum indexes": {"func": sumAllIndex, "parameters": 0}
}

r = i.listen()
i.execute(r)
