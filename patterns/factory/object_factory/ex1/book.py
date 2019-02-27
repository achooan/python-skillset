

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def serialize(self, serializer):
        serializer.start_object('book', self.book_id)
        serializer.add_property('title', self.title)
        serializer.add_property('author', self.author)
