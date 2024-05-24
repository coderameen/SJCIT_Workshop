class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        
    #add book
    def add_book(self,title,author,copies):
        book = {"title":title,"author":author,"available_copies":copies,"copies":copies}
        
        self.books.append(book)
        print(f"{title} book has added successfully!!")
        
    def display_books(self):
        if self.books:
            print("Books Details: ")
            for book in self.books:
                print(f"The Book title is: {book['title']} | author is: {book['author']} | Available Copis: {book['available_copies']}")
        else:
            print("There is no book avialable!!")
    #helper function
    def find_book(self,title):
        if self.books:
            for book in self.books:
                if book['title'] == title:
                    return book
        return None  
    def barrow_book(self,title):
        book  = self.find_book(title)
        if book is not None:
            if book['available_copies'] <= book['copies']:
                book['available_copies'] -= 1
            print(f"{title} book has barrowed successful")
        else:
            print(f"{title} books is not available")
            
    def return_book(self,title):
        book = self.find_book(title)
        if book != None:
            if book['available_copies'] < book['copies']:
                book['available_copies'] += 1
                print(f"{title} book has been returned succesfully!!")
            else:
                print(f"This book not belongs to library!!")     
        else:
            print(f"This book not belongs to library!!")
            
             
l1 = LibraryManagementSystem()
l1.add_book('Algorithm','celvin',5)
l1.add_book('Ml_Learning', 'alen',3)
l1.display_books()
l1.barrow_book('Algorithm')
l1.barrow_book('Algorithm')
l1.display_books()
l1.return_book('Algorithm')
l1.display_books()
l1.return_book('Algorithm')
l1.display_books()
l1.return_book('Algorithm')
l1.display_books()