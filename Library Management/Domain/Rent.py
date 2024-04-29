class Rent:
    def __init__(self, rent_id, book_id, client_id, isReturned):
        self.__rent_id = rent_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__isReturned = isReturned

    def get_rent_id(self):
        return self.__rent_id

    def get_book_id(self):
        return self.__book_id

    def get_client_id(self):
        return self.__client_id

    def get_isReturned(self):
        return self.__isReturned

    def set_rent_id(self, new_rent_id):
        self.__rent_id = new_rent_id

    def set_book_id(self, new_book_id):
        self.__book_id = new_book_id

    def set_client_id(self, new_client_id):
        self.__client_id = new_client_id

    def set_isReturned(self, new_isReturned):
        self.__isReturned = new_isReturned

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, Rent):
            return False
        return (self.__rent_id == other.__rent_id and self.__book_id == other.__book_id and
                self.__client_id == other.__client_id and self.__isReturned == other.__isReturned)

    def __str__(self):
        return str(self.__rent_id) + ". " + str(self.__book_id) + ", " + str(self.__client_id) + ", " + str(self.__isReturned)
