class Validators:
    def __init__(self, bookRepository, clientRepository, rentRepository):
        self.__bookRepository = bookRepository
        self.__clientRepository = clientRepository
        self.__rentRepository = rentRepository

    def validateBookID(self, ID):
        books = self.__bookRepository.get_allBooks()

        for i in range(len(books)):
            if ID == books[i].get_book_id():
                print("The ID already exists")
                return False
        return True

    def validateClientID(self, ID):
        clients = self.__clientRepository.get_allClients()

        for i in range(len(clients)):
            if ID == clients[i].get_client_id():
                print("The ID already exists")
                return False
        return True

    def validateRentID(self, ID):
        rents = self.__rentRepository.get_allRents()

        for i in range(len(rents)):
            if ID == rents[i].get_rent_id():
                print("The ID already exists")
                return False
        return True

    def idBookExists(self, idBook):
        books = self.__bookRepository.get_allBooks()

        for i in range(len(books)):
            if idBook == books[i].get_book_id():
                return True
        print("The book does not exist in the list!")
        return False

    def idClientExists(self, idClient):
        clients = self.__clientRepository.get_allClients()

        for i in range(len(clients)):
            if idClient == clients[i].get_client_id():
                return True
        print("The client does not exist in the list!")
        return False

    def validateStrings(self, string):
        if string == '':
            print("Invalid! The string can not be null.")
            return False
        return True
