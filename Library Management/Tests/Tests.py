from Domain.Book import Book
from Domain.Client import Client
from Domain.Rent import Rent


class Tests:
    def __init__(self, bookRepository, clientRepository, rentRepository, bookService, clientService, rentService, srv):
        self.__test_list = []
        self.__bookRepo = bookRepository
        self.__clientRepo = clientRepository
        self.__rentRepo = rentRepository
        self.__bookSrv = bookService
        self.__clientSrv = clientService
        self.__rentSrv = rentService
        self.__srv = srv

    # Tests for domain
    def test_create_book(self):
        book = Book(1, 'a', 'b', 'c')

        assert (book.get_book_id() == 1)
        assert (book.get_title() == 'a')
        assert (book.get_author() == 'b')
        assert (book.get_description() == 'c')

        book.set_book_id(2)
        book.set_title('r')
        book.set_author('t')
        book.set_description('b')

        assert (book.get_book_id() == 2)
        assert (book.get_title() == 'r')
        assert (book.get_author() == 't')
        assert (book.get_description() == 'b')

    def test_create_client(self):
        client = Client(1, 'a', '1234567891011')

        assert (client.get_client_id() == 1)
        assert (client.get_name() == 'a')
        assert (client.get_cnp() == '1234567891011')

        client.set_client_id(2)
        client.set_name('r')
        client.set_cnp('1416724476543')

        assert (client.get_client_id() == 2)
        assert (client.get_name() == 'r')
        assert (client.get_cnp() == '1416724476543')

    def test_create_rent(self):
        rent = Rent(1, 2, 3, True)

        assert (rent.get_rent_id() == 1)
        assert (rent.get_book_id() == 2)
        assert (rent.get_client_id() == 3)
        assert (rent.get_isReturned() == True)

        rent.set_rent_id(2)
        rent.set_book_id(3)
        rent.set_client_id(4)
        rent.set_isReturned(False)

        assert (rent.get_rent_id() == 2)
        assert (rent.get_book_id() == 3)
        assert (rent.get_client_id() == 4)
        assert (rent.get_isReturned() == False)

    # Tests for repository

    def test_add_book(self):
        book1 = Book(1, 'a', 'b', 'c')
        book2 = Book(2, 'b', 'c', 'd')
        book3 = Book(3, 'c', 'd', 'e')

        self.__bookRepo.add(book1)
        self.__bookRepo.add(book2)
        self.__bookRepo.add(book3)
        books = self.__bookRepo.get_allBooks()
        assert (len(books) == 3)

    def test_delete_book(self):
        books = self.__bookRepo.get_allBooks()
        assert (len(books) == 3)

        self.__bookRepo.deleteBook(2)
        books = self.__bookRepo.get_allBooks()
        assert (len(books) == 2)

        self.__bookRepo.deleteBook(4)
        books = self.__bookRepo.get_allBooks()
        assert (len(books) == 1)

        self.__bookRepo.deleteBook(3)
        books = self.__bookRepo.get_allBooks()
        assert (len(books) == 0)

    def test_update_book(self):
        book = Book(4, 'c', 'd', 'e')
        self.__bookRepo.updateBook(1, book)
        books = self.__bookRepo.get_allBooks()
        assert (books[0].get_title() == 'c')
        assert (books[0].get_author() == 'd')
        assert (books[0].get_description() == 'e')

    def test_add_client(self):
        client1 = Client(1, 'a', '123')
        client2 = Client(2, 'b', '456')
        client3 = Client(3, 'c', '789')

        self.__clientRepo.add(client1)
        self.__clientRepo.add(client2)
        self.__clientRepo.add(client3)
        clients = self.__clientRepo.get_allClients()
        assert (len(clients) == 3)

    def test_update_client(self):
        client = Client(4, 'b', '456')
        self.__clientRepo.updateClient(1, client)
        clients = self.__clientRepo.get_allClients()
        assert (clients[0].get_client_id() == 4)
        assert (clients[0].get_name() == 'b')
        assert (clients[0].get_cnp() == '456')

    def test_delete_client(self):
        clients = self.__clientRepo.get_allClients()
        assert (len(clients) == 3)

        self.__clientRepo.deleteClient(2)
        clients = self.__clientRepo.get_allClients()
        assert (len(clients) == 2)

        self.__clientRepo.deleteClient(4)
        clients = self.__clientRepo.get_allClients()
        assert (len(clients) == 1)

        self.__clientRepo.deleteClient(3)
        clients = self.__clientRepo.get_allClients()
        assert (len(clients) == 0)

    def test_add_rent(self):
        rent1 = Rent(1, 2, 3, True)
        rent2 = Rent(2, 3, 4, False)
        rent3 = Rent(3, 4, 5, True)

        self.__rentRepo.addRent(rent1)
        self.__rentRepo.addRent(rent2)
        self.__rentRepo.addRent(rent3)

        rents = self.__rentRepo.get_allRents()
        assert (len(rents) == 3)

    def test_update_rent(self):
        rent = Rent(4, 3, 2, True)
        self.__rentRepo.updateRent(2, rent)
        rents = self.__rentRepo.get_allRents()
        assert (rents[1].get_rent_id() == 4)
        assert (rents[1].get_book_id() == 3)
        assert (rents[1].get_client_id() == 2)
        assert (rents[1].get_isReturned() == True)

    def test_delete_rent(self):
        rents = self.__rentRepo.get_allRents()
        assert (len(rents) == 3)

        self.__rentRepo.deleteRent(1)
        rents = self.__rentRepo.get_allRents()
        assert (len(rents) == 2)

        self.__rentRepo.deleteRent(4)
        rents = self.__rentRepo.get_allRents()
        assert (len(rents) == 1)

        self.__rentRepo.deleteRent(3)
        rents = self.__rentRepo.get_allRents()
        assert (len(rents) == 0)

    # Tests for service

    def test_addBook(self):
        book1 = Book(1, 'a', 'b', 'c')
        book2 = Book(2, 'b', 'c', 'd')
        book3 = Book(3, 'c', 'd', 'e')

        self.__bookSrv.add_book(book1)
        self.__bookSrv.add_book(book2)
        self.__bookSrv.add_book(book3)

        books = self.__bookSrv.get_books()
        assert (len(books) == 3)

    def test_deleteBook(self):
        books = self.__bookSrv.get_books()
        assert (len(books) == 3)

        self.__bookSrv.delete_book(2)
        books = self.__bookSrv.get_books()
        assert (len(books) == 2)

        self.__bookSrv.delete_book(4)
        self.__bookSrv.delete_book(3)

    def test_updateBook(self):
        book = Book(4, 'c', 'd', 'e')
        self.__bookSrv.update_book(1, book)
        books = self.__bookSrv.get_books()
        assert (books[0].get_title() == 'c')
        assert (books[0].get_author() == 'd')
        assert (books[0].get_description() == 'e')

    def test_addClient(self):
        client1 = Client(1, 'c', '123')
        client2 = Client(2, 'd', '456')
        client3 = Client(3, 'e', '789')

        self.__clientSrv.add_client(client1)
        self.__clientSrv.add_client(client2)
        self.__clientSrv.add_client(client3)
        clients = self.__clientSrv.get_clients()
        assert (len(clients) == 3)

    def test_deleteClient(self):
        clients = self.__clientSrv.get_clients()
        assert (len(clients) == 3)

        self.__clientSrv.delete_client(2)
        clients = self.__clientSrv.get_clients()
        assert (len(clients) == 2)

        self.__clientSrv.delete_client(1)
        self.__clientSrv.delete_client(3)

    def test_updateClient(self):
        client = Client(1, 'b', '456')
        self.__clientSrv.update_client(1, client)
        clients = self.__clientSrv.get_clients()
        assert (clients[0].get_client_id() == 1)
        assert (clients[0].get_name() == 'b')
        assert (clients[0].get_cnp() == '456')

    def test_addRent(self):
        rent1 = Rent(1, 2, 3, True)
        rent2 = Rent(2, 3, 4, False)
        rent3 = Rent(3, 4, 5, True)

        self.__rentSrv.add_rent(rent1)
        self.__rentSrv.add_rent(rent2)
        self.__rentSrv.add_rent(rent3)
        rents = self.__rentSrv.get_rents()
        assert (len(rents) == 3)

    def test_updateRent(self):
        rent = Rent(1, 3, 5, False)
        self.__rentSrv.update_rent(1, rent)
        rents = self.__rentSrv.get_rents()
        assert (rents[0].get_rent_id() == 1)
        assert (rents[0].get_book_id() == 3)
        assert (rents[0].get_client_id() == 5)
        assert (rents[0].get_isReturned() == False)

    def test_deleteRent(self):
        rents = self.__rentSrv.get_rents()
        assert (len(rents) == 3)

        self.__rentSrv.delete_rent(2)
        rents = self.__rentSrv.get_rents()
        assert (len(rents) == 2)

        self.__rentSrv.delete_rent(1)
        rents = self.__rentSrv.get_rents()
        assert (len(rents) == 1)

        self.__rentSrv.delete_rent(3)
        rents = self.__rentSrv.get_rents()
        assert (len(rents) == 0)

    def test_reports(self):
        book1 = Book(1, 'a', 'b', 'c')
        book2 = Book(2, 'b', 'c', 'd')
        book3 = Book(3, 'c', 'd', 'e')
        book4 = Book(4, 'd', 'e', 'f')
        book5 = Book(5, 'e', 'f', 'g')

        client1 = Client(1, 'a', '2505')
        client2 = Client(2, 'r', '1212')
        client3 = Client(3, 'e', '1903')
        client4 = Client(4, 'b', '1211')
        client5 = Client(5, 'p', '0319')

        rent1 = Rent(1, 2, 1, True)
        rent2 = Rent(2, 2, 2, False)
        rent3 = Rent(3, 3, 4, False)
        rent4 = Rent(4, 1, 5, True)
        rent5 = Rent(5, 4, 2, True)
        rent6 = Rent(6, 1, 3, False)
        rent7 = Rent(7, 2, 1, True)
        rent8 = Rent(8, 5, 2, False)
        rent9 = Rent(9, 5, 3, True)
        rent10 = Rent(10, 3, 1, True)

        self.__bookSrv.add_book(book1)
        self.__bookSrv.add_book(book2)
        self.__bookSrv.add_book(book3)
        self.__bookSrv.add_book(book4)
        self.__bookSrv.add_book(book5)

        self.__clientSrv.add_client(client1)
        self.__clientSrv.add_client(client2)
        self.__clientSrv.add_client(client3)
        self.__clientSrv.add_client(client4)
        self.__clientSrv.add_client(client5)

        self.__rentSrv.add_rent(rent1)
        self.__rentSrv.add_rent(rent2)
        self.__rentSrv.add_rent(rent3)
        self.__rentSrv.add_rent(rent4)
        self.__rentSrv.add_rent(rent5)
        self.__rentSrv.add_rent(rent6)
        self.__rentSrv.add_rent(rent7)
        self.__rentSrv.add_rent(rent8)
        self.__rentSrv.add_rent(rent9)
        self.__rentSrv.add_rent(rent10)

        report = self.__srv.theMostRented()
        assert (report[0][0] == 'b')
        assert (report[1][0] == 'c')
        assert (report[2][0] == 'a')
        assert (report[3][0] == 'e')
        assert (report[4][0] == 'd')

        report = self.__srv.sortClients_byName()
        assert (report[0][0] == 'b')
        assert (report[1][0] == 'e')
        assert (report[2][0] == 'r')
        assert (report[3][0] == 'r')

        report = self.__srv.sortClients_byNrRented()
        assert (report[0][0] == 'r')
        assert (report[1][0] == 'e')
        assert (report[2][0] == 'a')
        assert (report[3][0] == 'p')

        report = self.__srv.first20_mostActiveClients()
        assert (report[0][0] == 'a')
        assert (report[1][0] == 'r')

        self.__bookSrv.delete_book(1)
        self.__bookSrv.delete_book(2)
        self.__bookSrv.delete_book(3)
        self.__bookSrv.delete_book(4)
        self.__bookSrv.delete_book(5)

        self.__clientSrv.delete_client(1)
        self.__clientSrv.delete_client(2)
        self.__clientSrv.delete_client(3)
        self.__clientSrv.delete_client(4)
        self.__clientSrv.delete_client(5)

        self.__rentSrv.delete_rent(1)
        self.__rentSrv.delete_rent(2)
        self.__rentSrv.delete_rent(3)
        self.__rentSrv.delete_rent(4)
        self.__rentSrv.delete_rent(5)
        self.__rentSrv.delete_rent(6)
        self.__rentSrv.delete_rent(7)
        self.__rentSrv.delete_rent(8)
        self.__rentSrv.delete_rent(9)
        self.__rentSrv.delete_rent(10)

