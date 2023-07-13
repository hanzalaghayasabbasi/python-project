# Library Managment add delete and nobooks

class libray:
    def __init__(self):
        self.noBooks=0
        self.Books=[]

    def add_books(self,books):
      self.Books.append(books)
      self.noBooks=len(self.Books)

    def info(self):
      print("The number of books are : {0}  and the name of books are  ".format(self.noBooks) )
      for k in self.Books:
          print(k)

    
    def del_books(self):
      self.Books.pop()
      self.noBooks=len(self.Books)
      print("After delete last book Now number of books are : {0}  and the name of books are  ".format(self.noBooks) )
      


l=libray()
l.add_books("Harry Porter 1")
l.add_books("Harry Porter 2")
l.add_books("Harry Porter 3")
l.add_books("Harry Porter 4")
l.info()
l.del_books()

