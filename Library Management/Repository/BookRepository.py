class BookRepository:
    def __init__(self):
        self.__booksList = []

    def add(self, book):
        """
        Add a book
        :param book: the book
        """
        self.__booksList.append(book)

    def deleteBook(self, book_id):
        """
        Delete a book
        :param book_id: the id of the book that needs to be deleted
        """
        result = []
        for i in range(len(self.__booksList)):
            if self.__booksList[i].get_book_id() != book_id:
                result.append(self.__booksList[i])
        self.__booksList = result

    def updateBook(self, b, new_book):
        """
        Update a book
        :param b: the id of the book that needs to be updated
        :param new_book: the updated book
        """
        result = []
        for i in range(len(self.__booksList)):
            if self.__booksList[i].get_book_id() != b:
                result.append(self.__booksList[i])
            else:
                result.append(new_book)
        self.__booksList = result

    def searchBook(self, idBook):
        ok = False
        for i in range(len(self.__booksList)):
            if self.__booksList[i].get_book_id() != idBook:
                result = self.__booksList[i]
                return result
        if not ok:
            print("The book that you are searching for does not exist!")

    def get_allBooks(self):
        """
        Get the list of the books
        :return: list of books
        """
        return self.__booksList

    def get_titleBook(self, idBook):
        for i in range(len(self.__booksList)):
            if self.__booksList[i].get_book_id() == idBook:
                title = self.__booksList[i].get_title()
                return title
