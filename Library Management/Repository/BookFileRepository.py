from Domain.Book import Book


class BookFileRepository:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        books = []
        with open(self.__filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line != ' ':
                    line = line.strip()
                    bookLine = line.split(',')
                    idBook = bookLine[0]
                    title = bookLine[1]
                    author = bookLine[2]
                    description = bookLine[3]
                    book = Book(idBook, title, author, description)
                    books.append(book)
        file.close()
        return books

    def save_in_file(self, books):
        with open(self.__filename, 'w') as file:
            for book in books:
                file.write(
                    str(book.get_book_id()) + "," + book.get_title() + "," + book.get_author() + "," + book.get_description())
                file.write('\n')
            file.close()

    def add(self, book):
        """
        Add a book
        :param book: the book
        """
        books = self.load_from_file()
        books.append(book)
        self.save_in_file(books)

    def deleteBook(self, book_id):
        """
        Delete a book
        :param book_id: the id of the book that needs to be deleted
        """
        books = self.load_from_file()
        result = []
        for i in range(len(books)):
            idBook = books[i].get_book_id()
            if int(idBook) != book_id:
                result.append(books[i])
        books = result
        self.save_in_file(books)

    def updateBook(self, b, new_book):
        """
        Update a book
        :param b: the id of the book that needs to be updated
        :param new_book: the updated book
        """
        books = self.load_from_file()
        result = []
        for i in range(len(books)):
            if int(books[i].get_book_id()) != b:
                result.append(books[i])
            else:
                result.append(new_book)
        books = result
        self.save_in_file(books)

    def updateBookRecursive(self, i, books, b, new_book):
        """
        Update recursively a book
        :param i: the counter
        :param books: the list with books
        :param b: the id of the book that needs to be updated
        :param new_book: the updated book
        """
        if i >= len(books):
            return
        if i == b:
            books[i].set_book_id(new_book.get_book_id())
            books[i].set_title(new_book.get_title())
            books[i].set_author(new_book.get_author())
            books[i].set_description(new_book.get_description())
            self.save_in_file(books)
            return
        self.updateBookRecursive(i + 1, books, b, new_book)

    def searchBook(self, idBook):
        """
        Search for a book
        Complexity: caz favorabil: θ(1)
                    cas nefavorabil : θ(n)
                    caz genral: O(n)
        :param idBook: the book's id that we are searching for
        :return: the book that we search for
        """
        books = self.load_from_file()
        ok = False
        for i in range(len(books)):
            if int(books[i].get_book_id()) == idBook:
                result = books[i]
                return result
        if not ok:
            print("The book that you are searching for does not exist!")


    def get_allBooks(self):
        """
        Get the list of the books
        :return: list of books
        """
        return self.load_from_file()

    def get_titleBook(self, idBook):
        books = self.load_from_file()
        for i in range(len(books)):
            if int(books[i].get_book_id()) == idBook:
                title = books[i].get_title()
                return title
