from models.media import Book, Film, Music

class MediaFactory():
    def createMedia(self, type, title, author):
        mediaType = {
            "book": Book(title, author),
            "film": Film(title, author),
            "music": Music(title, author),
        }

        return mediaType[type]