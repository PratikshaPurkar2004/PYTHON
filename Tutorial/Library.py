class Library:
    
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)
    def ShowInfo(self):
         print(f"the library has {self.no_of_books} books and books are")
         for book in self.books:
             print(book)
    
l1=Library()
l1.addbook("java")
l1.addbook("python")
l1.addbook("software testing")
l1.addbook("math")
l1.addbook("electronic")
l1.ShowInfo()
        
for i in range(0,len(books)):
    print(books[i])
