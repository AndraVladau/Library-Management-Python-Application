class Book:
    def __init__(self, book_id, title, author, description):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__description = description

    def get_book_id(self):
        """
        Get the book's id
        :return: the book's id
        """
        return self.__book_id

    def get_title(self):
        """
        Get the book's title
        :return: the book's title
        """
        return self.__title

    def get_description(self):
        """
        Get the book's description
        :return: the book's description
        """
        return self.__description

    def get_author(self):
        """
        Get the book's author
        :return: the book's author
        """
        return self.__author

    def set_book_id(self, new_book_id):
        """
        Set the new id of the book
        :param new_book_id: the new id of the book
        """
        self.__book_id = new_book_id

    def set_title(self, new_title):
        """
        Set the new title of the book
        :param new_title: the new title of the book
        """
        self.__title = new_title

    def set_author(self, new_author):
        """
        Set the new author of the book
        :param new_author: the new author of the book
        """
        self.__author = new_author

    def set_description(self, new_description):
        """
        Set the new description of the book
        :param new_description: the new description of the book
        """
        self.__description = new_description

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, Book):
            return False
        return (self.__book_id == other.__book_id and self.__title == other.__title and self.__author == other.__author
                and self.__description == other.__description)

    def __str__(self):
        return str(self.__book_id) + ". " + self.__title + ", " + self.__author + ", " + self.__description
