class BookService:
    def __init__(self, bookRepository):
        self.__bookRepo = bookRepository

    def add_book(self, book):
        """
        Add a book
        :param book: the book
        """
        self.__bookRepo.add(book)

    def delete_book(self, book_id):
        """
        Delete a book
        :param book_id: the id of the book that needs to be deleted
        """
        self.__bookRepo.deleteBook(book_id)

    def update_book(self, b, new_book):
        """
        Update a book
        :param b: the id of the book that needs to be updated
        :param new_book: the updated book
        """
        self.__bookRepo.updateBook(b, new_book)

    def update_book_recursive(self, b, new_book):
        """
        Update recursively a book
        :param b: the id of the book that needs to be updated
        :param new_book: the updated book
        """
        self.__bookRepo.updateBookRecursive(0, self.get_books(), b, new_book)

    def search_book(self, idBook):
        return self.__bookRepo.searchBook(idBook)

    def search_book_recursive(self, idBook):
        return self.__bookRepo.searchBookRecursive(0, idBook, self.get_books())

    def get_books(self):
        """
        Get the list of the books
        :return: list of books
        """
        return self.__bookRepo.get_allBooks()
