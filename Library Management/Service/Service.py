import random
import string

from Domain.Book import Book


class Service:
    def __init__(self, bookRepository, clientRepository, rentRepository, validator):
        self.__bookRepository = bookRepository
        self.__clientRepository = clientRepository
        self.__rentRepository = rentRepository
        self.__validator = validator

    def theMostRented(self):
        """
        The most rented books
        :return: the list that has the most rented books
        """
        rents = self.__rentRepository.get_allRents()
        ap = {}
        for i in range(len(rents)):
            rent = rents[i]
            idBook = rent.get_book_id()
            if idBook in ap:
                ap[idBook] += 1
            else:
                ap[idBook] = 1

        report = []
        for i in ap:
            title = self.__bookRepository.get_titleBook(i)
            rentedBooks = ap[i]
            report.append([title, rentedBooks])

        report = sorted(report, key=lambda x: x[1], reverse=True)
        return report

    def sortClients_byName(self):
        """
        The clients, who have rented books, sorted ascending by name
        :return: the list with the clients, who have rented books, sorted ascending by name
        """
        rents = self.__rentRepository.get_allRents()
        report = []
        for i in range(len(rents)):
            rent = rents[i]
            idClient = rent.get_client_id()
            idBook = rent.get_book_id()
            if not bool(rent.get_isReturned()):
                name = self.__clientRepository.getClientName(idClient)
                title = self.__bookRepository.get_titleBook(idBook)
                report.append([name, title])

        report = sorted(report, key=lambda x: x[0], reverse=False)
        return report

    def sortClients_byNrRented(self):
        """
        The clients, who have rented books, sorted ascending by the number of books rented.
        :return: the list with the clients, who have rented books, sorted ascending by the number of books rented
        """
        rents = self.__rentRepository.get_allRents()
        ap = {}
        for i in range(len(rents)):
            rent = rents[i]
            idBook = rent.get_book_id()
            if not bool(rent.get_isReturned()):
                if idBook in ap:
                    ap[idBook] += 1
                else:
                    ap[idBook] = 1

        report = []
        for i in ap:
            name = self.__clientRepository.getClientName(i)
            rentedBooks = ap[i]
            report.append([name, rentedBooks])

        report = sorted(report, key=lambda x: x[1], reverse=False)
        return report

    def first20_mostActiveClients(self):
        """
        Print the first 20% of the clients that are the most active
        :return: the list with the first 20% clients that are the most active
        """
        rents = self.__rentRepository.get_allRents()
        ap = {}
        for i in range(len(rents)):
            rent = rents[i]
            idClient = rent.get_client_id()
            if idClient in ap:
                ap[idClient] += 1
            else:
                ap[idClient] = 1

        report = []
        for i in ap:
            name = self.__clientRepository.getClientName(i)
            rentedBooks = ap[i]
            report.append([name, rentedBooks])

        nrRented = int(len(report) * 0.2) + 1
        report = report[:nrRented]
        return report

    def createNewBook(self):
        """
        Creates a new book(random)
        """
        idBook = random.choice(range(1, 10000))
        while not self.__validator.validateBookID(idBook):
            idBook = random.choice(range(1, 10000))

        string1 = string.ascii_lowercase
        titleNoCh = random.choice(range(5, 20))
        title = ''.join(random.choices(string1, k=titleNoCh))
        title = str(title)

        authorNoCh = random.choice(range(10, 26))
        author = ''.join(random.choices(string1, k=authorNoCh))
        author = str(author)

        descriptionNoCh = random.choice(range(5, 35))
        description = ''.join(random.choices(string1, k=descriptionNoCh))
        description = str(description)

        book = Book(idBook, title, author, description)
        self.__bookRepository.add(book)

