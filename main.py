from mylibrary.library import Library
Library.my_module()
python = Library("python" , "100")
java = Library("java" , "100")
Library.add_book(python)
Library.add_book(java)
Library.remove_book(python)
print(Library.show_books(Library))
