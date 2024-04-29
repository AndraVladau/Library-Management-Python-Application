import random
import string
from functools import reduce

from Domain.Book import Book


class FileService:
    def __init__(self, bookFileRepository, clientRepository, rentRepository, sorts, validator):
        self.__bookFileRepository = bookFileRepository
        self.__sorts = sorts
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
            if int(idBook) in ap:
                ap[int(idBook)] += 1
            else:
                ap[int(idBook)] = 1

        report = []
        for i in ap:
            title = self.__bookFileRepository.get_titleBook(i)
            rentedBooks = ap[i]
            report.append([title, rentedBooks])

        # report = sorted(report, key=lambda x: x[1], reverse=True)
        report = self.__sorts.gnomeSort(report, key=None, reverse=True)
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
            if rent.get_isReturned() == "False":
                name = self.__clientRepository.getClientName(int(idClient))
                title = self.__bookFileRepository.get_titleBook(int(idBook))
                report.append([name, title])

        # report = sorted(report, key=lambda x: x[0], reverse=False)
        report = self.__sorts.quickSort(report, key=lambda x: x[0], reverse=False)
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
            idClient = rent.get_client_id()
            if rent.get_isReturned() == "False":
                if int(idClient) in ap:
                    ap[int(idClient)] += 1
                else:
                    ap[int(idClient)] = 1

        report = []
        for i in ap:
            name = self.__clientRepository.getClientName(i)
            rentedBooks = ap[i]
            report.append([name, rentedBooks])

        # report = sorted(report, key=lambda x: x[1], reverse=False)
        report = self.__sorts.gnomeSort(report, key=None, reverse=False)
        return report

    def first20_mostActiveClients(self):
        """
        Print the first 20% the most active clients
        :return: the list with the first 20% the most active clients
        """
        rents = self.__rentRepository.get_allRents()
        ap = {}
        for i in range(len(rents)):
            rent = rents[i]
            idClient = rent.get_client_id()
            if int(idClient) in ap:
                ap[int(idClient)] += 1
            else:
                ap[int(idClient)] = 1

        report = []
        for i in ap:
            name = self.__clientRepository.getClientName(i)
            rentedBooks = ap[i]
            report.append([name, rentedBooks])

        # report = sorted(report, key=lambda x: x[1], reverse=True)
        report = self.__sorts.gnomeSort(report, key=lambda x: x[1], reverse=True)
        nrRented = int(len(report) * 0.2) + 1
        report = report[:nrRented]
        return report

    def first20_mostRentedBooks(self):
        """
        Print the first 20% thw most rented books
        :return: the list with the first 20% most rented books
        """
        rents = self.__rentRepository.get_allRents()
        ap = {}
        for i in range(len(rents)):
            rent = rents[i]
            idBook = rent.get_book_id()
            if int(idBook) in ap:
                ap[int(idBook)] += 1
            else:
                ap[int(idBook)] = 1

        report = []
        for i in ap:
            book = self.__bookFileRepository.get_titleBook(i)
            rentedBooks = ap[i]
            report.append([book, rentedBooks])

        # report = sorted(report, key=lambda x: x[1], reverse=True)
        report = self.__sorts.gnomeSort(report, key=lambda x: x[1], reverse=True)
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
        self.__bookFileRepository.add(book)

