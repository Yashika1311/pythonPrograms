#Design a library catalogue system using inheritance. take base class library item and derieved classes book, dvd and journal. each derived class should have unique attributes and methohds and system should support checking in nd checking out System.

class library:
    def __init__(self,title,book_no,copies):
        self.title=title
        self.book_no=book_no
        self.copies=copies
        self.checked_out_copies=0

def book(library):
     def __init__(self, title, book_no,copies, author):
           super().__init__(title, book_no, copies)
           self.author = author



       