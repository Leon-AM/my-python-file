#This is module library.

class Library:
    save_book= {}

    def __init__(self , name_book , pages ):
        self.name_book = name_book.strip()
        self.pages = pages
        
    
    # add books
    def add_book(self):
        Library.save_book[self.name_book] = self.pages
        return f"book name : {self.name_book} and number of pages : {self.pages}"

    # remove book
    def remove_book(self):
        Library.save_book.pop(self.name_book)
        return f"remove {self.name_book}"
    
    #search book
    def search_book(self):
        search = input("book search : ").strip()
        found = False
        for key in self.save_book:
            if search in key:
                print("This book is available")
                found = True
        if not found:
            print("This book not available")
        return self.save_book
    
    #show books
    def show_books(self):
        return self.save_book

lib1 = Library("python" , "100")
Library.add_book(lib1)
print(Library.show_books(Library))
#__name__
def my_module():
    print(f"in module , name is {__name__}")

if __name__ == "__main__":
    Library.show_books(Library)


        






