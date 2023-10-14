from models.database import Database
from factories.media_factory import MediaFactory
from models.interface import Interface

db = Database()
db.set('peopleList')

Media = MediaFactory()
media1 = Media.createMedia('book', 'Tartarugas Até Lá em Baixo', 'John Green')

db.create(2, media1.toDict())


'Interface -- (dados) -> MediaFactory -- (dict) --> Database'