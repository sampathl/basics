class Book(object):
    def __init__(self,isbn_,last_,first_,title_):
        self.isbn=isbn_
        self.last=last_
        self.first=first_
        self.title=title_
    

class Booknode(object):
    def __init__(self,isbn,last,first,title):
        self.book=Book(isbn,last,first,title)
        self.next=None
        