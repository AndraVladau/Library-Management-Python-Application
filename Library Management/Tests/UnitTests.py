import unittest

from Domain.Book import Book
from Domain.Client import Client
from Domain.Rent import Rent
from Domain.Validators import Validators

from Repository.BookFileRepository import BookFileRepository
from Repository.ClientFileRepository import ClientFileRepository
from Repository.RentFileRepository import RentFileRepository

from Service.BookService import BookService
from Service.ClientService import ClientService
from Service.RentService import RentService
from Service.FileService import FileService
from Utils.Sorts import Sorts


class TestBookDomainCases(unittest.TestCase):
    def setUp(self):
        self.book1 = Book(1, "The Cruel Prince", "Holly Black", "abcd")
        self.book2 = Book(2, "The Hobbit", "J.R.R.Tolkien", "abcd")
        self.book3 = Book(3, "The Fellowship of the Ring", "J.R.R.Tolkien", "abcd")
        self.book1Copy = Book(1, "The Cruel Prince", "Holly Black", "abcd")

    def testEqualOverload(self):
        self.assertEqual(self.book1, self.book1Copy)

    def testNotEqualOverLoad(self):
        self.assertNotEqual(self.book1, self.book2)
        self.assertNotEqual(self.book2, self.book3)
        self.assertNotEqual(self.book1, self.book3)

    def testGetID(self):
        self.assertEqual(self.book1.get_book_id(), 1)
        self.assertEqual(self.book2.get_book_id(), 2)
        self.assertEqual(self.book3.get_book_id(), 3)

    def testGetTitle(self):
        self.assertEqual(self.book1.get_title(), "The Cruel Prince")
        self.assertEqual(self.book2.get_title(), "The Hobbit")
        self.assertEqual(self.book3.get_title(), "The Fellowship of the Ring")

    def testGetAuthor(self):
        self.assertEqual(self.book1.get_author(), "Holly Black")
        self.assertEqual(self.book2.get_author(), "J.R.R.Tolkien")
        self.assertEqual(self.book3.get_author(), "J.R.R.Tolkien")

    def testGetDescription(self):
        self.assertEqual(self.book1.get_description(), "abcd")
        self.assertEqual(self.book2.get_description(), "abcd")
        self.assertEqual(self.book3.get_description(), "abcd")

    def testSetID(self):
        self.book2.set_book_id(4)
        self.assertEqual(self.book2.get_book_id(), 4)

    def testSetTitle(self):
        self.book2.set_title("If We Were Villains")
        self.assertEqual(self.book2.get_title(), "If We Were Villains")

    def testSetAuthor(self):
        self.book2.set_author("M.L.Rio")
        self.assertEqual(self.book2.get_author(), "M.L.Rio")

    def testSetDescription(self):
        self.book2.set_description("abc")
        self.assertEqual(self.book2.get_description(), "abc")


class TestClientDomainCases(unittest.TestCase):
    def setUp(self):
        self.client1 = Client(1, "Anya", "2505")
        self.client2 = Client(2, "Reg", "1612")
        self.client3 = Client(3, "Andreea", "1912")
        self.client1Copy = Client(1, "Anya", "2505")

    def testEqualOverload(self):
        self.assertEqual(self.client1, self.client1Copy)

    def testNotEqualOverLoad(self):
        self.assertNotEqual(self.client1, self.client2)
        self.assertNotEqual(self.client2, self.client3)
        self.assertNotEqual(self.client1, self.client3)

    def testGetID(self):
        self.assertEqual(self.client1.get_client_id(), 1)
        self.assertEqual(self.client2.get_client_id(), 2)
        self.assertEqual(self.client3.get_client_id(), 3)

    def testGetName(self):
        self.assertEqual(self.client1.get_name(), "Anya")
        self.assertEqual(self.client2.get_name(), "Reg")
        self.assertEqual(self.client3.get_name(), "Andreea")

    def testGetCnp(self):
        self.assertEqual(self.client1.get_cnp(), "2505")
        self.assertEqual(self.client2.get_cnp(), "1612")
        self.assertEqual(self.client3.get_cnp(), "1912")

    def testSetID(self):
        self.client2.set_client_id(4)
        self.assertEqual(self.client2.get_client_id(), 4)

    def testSetTitle(self):
        self.client2.set_name("Barty")
        self.assertEqual(self.client2.get_name(), "Barty")

    def testSetAuthor(self):
        self.client2.set_cnp("1411")
        self.assertEqual(self.client2.get_cnp(), "1411")


class TestRentDomainCases(unittest.TestCase):
    def setUp(self):
        self.rent1 = Rent(1, 2, 1, True)
        self.rent2 = Rent(2, 1, 3, False)
        self.rent3 = Rent(3, 9, 7, False)
        self.rent1Copy = Rent(1, 2, 1, True)

    def testEqualOverload(self):
        self.assertEqual(self.rent1, self.rent1Copy)

    def testNotEqualOverLoad(self):
        self.assertNotEqual(self.rent1, self.rent2)
        self.assertNotEqual(self.rent2, self.rent3)
        self.assertNotEqual(self.rent1, self.rent3)

    def testGetID(self):
        self.assertEqual(self.rent1.get_rent_id(), 1)
        self.assertEqual(self.rent2.get_rent_id(), 2)
        self.assertEqual(self.rent3.get_rent_id(), 3)

    def testGetTitle(self):
        self.assertEqual(self.rent1.get_book_id(), 2)
        self.assertEqual(self.rent2.get_book_id(), 1)
        self.assertEqual(self.rent3.get_book_id(), 9)

    def testGetAuthor(self):
        self.assertEqual(self.rent1.get_client_id(), 1)
        self.assertEqual(self.rent2.get_client_id(), 3)
        self.assertEqual(self.rent3.get_client_id(), 7)

    def testGetDescription(self):
        self.assertEqual(self.rent1.get_isReturned(), True)
        self.assertEqual(self.rent2.get_isReturned(), False)
        self.assertEqual(self.rent3.get_isReturned(), False)

    def testSetID(self):
        self.rent2.set_rent_id(4)
        self.assertEqual(self.rent2.get_rent_id(), 4)

    def testSetTitle(self):
        self.rent2.set_book_id(9)
        self.assertEqual(self.rent2.get_book_id(), 9)

    def testSetAuthor(self):
        self.rent2.set_client_id(2)
        self.assertEqual(self.rent2.get_client_id(), 2)

    def testSetDescription(self):
        self.rent2.set_isReturned(True)
        self.assertEqual(self.rent2.get_isReturned(), True)


class TestBookFileRepositoryCases(unittest.TestCase):
    def setUp(self):
        self.bookFileRepo = BookFileRepository('BooksTest')

    def testGetBooks(self):
        books = self.bookFileRepo.get_allBooks()
        self.assertEqual(len(books), 12)

    def testAddBook(self):
        book1 = Book(13, "The Atlas Six", "Olivie Blake", "abcd")
        book2 = Book(14, "The Atlas Paradox", "Olivie Blake", "abcd")
        self.bookFileRepo.add(book1)
        self.bookFileRepo.add(book2)
        books = self.bookFileRepo.get_allBooks()
        self.assertEqual(len(books), 14)
        self.assertEqual(books[12].get_title(), "The Atlas Six")
        self.assertEqual(books[13].get_author(), "Olivie Blake")

    def testUpdateBook(self):
        newBook = Book(15, "The Atlas Complex", "Olivie Blake", "abcd")
        self.bookFileRepo.updateBook(14, newBook)
        books = self.bookFileRepo.get_allBooks()
        self.assertEqual(len(books), 14)
        self.assertEqual(int(books[13].get_book_id()), 15)
        self.assertEqual(books[13].get_title(), "The Atlas Complex")

    def testDeleteBook(self):
        self.bookFileRepo.deleteBook(13)
        books = self.bookFileRepo.get_allBooks()
        self.assertEqual(len(books), 13)

        self.bookFileRepo.deleteBook(15)
        books = self.bookFileRepo.get_allBooks()
        self.assertEqual(len(books), 12)

    def testSearchBook(self):
        book = self.bookFileRepo.searchBook(7)
        self.assertEqual(book.get_title(), "The Return of the King")


class TestClientFileRepositoryCases(unittest.TestCase):
    def setUp(self):
        self.clientFileRepo = ClientFileRepository('ClientsTest')

    def testGetClients(self):
        clients = self.clientFileRepo.get_allClients()
        self.assertEqual(len(clients), 10)

    def testAddClient(self):
        client1 = Client(11, "Lily", "3001")
        self.clientFileRepo.add(client1)
        clients = self.clientFileRepo.get_allClients()
        self.assertEqual(len(clients), 11)
        self.assertEqual(clients[10].get_name(), "Lily")

    def testUpdateClient(self):
        newClient = Client(12, "Marlene", "3004")
        self.clientFileRepo.updateClient(11, newClient)
        clients = self.clientFileRepo.get_allClients()
        self.assertEqual(len(clients), 11)
        self.assertEqual(int(clients[10].get_client_id()), 12)
        self.assertEqual(clients[10].get_name(), "Marlene")

    def testDeleteClient(self):
        self.clientFileRepo.deleteClient(12)
        clients = self.clientFileRepo.get_allClients()
        self.assertEqual(len(clients), 10)

    def testSearchClient(self):
        client = self.clientFileRepo.searchClient(7)
        self.assertEqual(client.get_name(), "Andreea")


class TestRentFileRepositoryCases(unittest.TestCase):
    def setUp(self):
        self.rentFileRepo = RentFileRepository('RentsTest')

    def testGetRents(self):
        rents = self.rentFileRepo.get_allRents()
        self.assertEqual(len(rents), 21)

    def testAddRent(self):
        rent1 = Rent(22, 12, 3, False)
        self.rentFileRepo.addRent(rent1)
        rents = self.rentFileRepo.get_allRents()
        self.assertEqual(len(rents), 22)
        self.assertEqual(int(rents[21].get_book_id()), 12)
        self.assertEqual(int(rents[21].get_client_id()), 3)

    def testUpdateRent(self):
        newRent = Rent(23, 10, 3, True)
        self.rentFileRepo.updateRent(22, newRent)
        rents = self.rentFileRepo.get_allRents()
        self.assertEqual(len(rents), 22)
        self.assertEqual(int(rents[21].get_book_id()), 10)
        self.assertEqual(rents[21].get_isReturned(), "True")

    def testDeleteRent(self):
        self.rentFileRepo.deleteRent(23)
        rents = self.rentFileRepo.get_allRents()
        self.assertEqual(len(rents), 21)

    def testSearchRent(self):
        rent = self.rentFileRepo.searchRent(10)
        self.assertEqual(str(rent.get_isReturned()), "True")


class TestBookServiceCases(unittest.TestCase):
    def setUp(self):
        bookFileRepo = BookFileRepository("BooksTest")
        self.bookSrv = BookService(bookFileRepo)

    def testGetBooks(self):
        books = self.bookSrv.get_books()
        self.assertEqual(len(books), 12)

    def testAddBook(self):
        book1 = Book(13, "The Atlas Six", "Olivie Blake", "abcd")
        book2 = Book(14, "The Atlas Paradox", "Olivie Blake", "abcd")
        self.bookSrv.add_book(book1)
        self.bookSrv.add_book(book2)

        books = self.bookSrv.get_books()
        self.assertEqual(len(books), 14)

    def testUpdateBook(self):
        newBook = Book(15, "The Atlas Complex", "Olivie Blake", "abcd")
        self.bookSrv.update_book(14, newBook)
        books = self.bookSrv.get_books()
        self.assertEqual(len(books), 14)
        self.assertEqual(int(books[13].get_book_id()), 15)
        self.assertEqual(books[13].get_title(), "The Atlas Complex")

    def testDeleteBook(self):
        self.bookSrv.delete_book(13)
        books = self.bookSrv.get_books()
        self.assertEqual(len(books), 13)

        self.bookSrv.delete_book(15)
        books = self.bookSrv.get_books()
        self.assertEqual(len(books), 12)

    def testSearchBook(self):
        book = self.bookSrv.search_book(7)
        self.assertEqual(book.get_title(), "The Return of the King")


class TestClientServiceCases(unittest.TestCase):
    def setUp(self):
        clientFileRepo = ClientFileRepository('ClientsTest')
        self.clientSrv = ClientService(clientFileRepo)

    def testGetClients(self):
        clients = self.clientSrv.get_clients()
        self.assertEqual(len(clients), 10)

    def testAddClient(self):
        client1 = Client(11, "Lily", "3001")
        self.clientSrv.add_client(client1)
        clients = self.clientSrv.get_clients()
        self.assertEqual(len(clients), 11)
        self.assertEqual(clients[10].get_name(), "Lily")

    def testUpdateClient(self):
        newClient = Client(12, "Marlene", "3004")
        self.clientSrv.update_client(11, newClient)
        clients = self.clientSrv.get_clients()
        self.assertEqual(len(clients), 11)
        self.assertEqual(int(clients[10].get_client_id()), 12)
        self.assertEqual(clients[10].get_name(), "Marlene")

    def testDeleteClient(self):
        self.clientSrv.delete_client(12)
        clients = self.clientSrv.get_clients()
        self.assertEqual(len(clients), 10)

    def testSearchClient(self):
        client = self.clientSrv.search_client(7)
        self.assertEqual(client.get_name(), "Andreea")


class TestRentServiceCases(unittest.TestCase):
    def setUp(self):
        rentFileRepo = RentFileRepository('RentsTest')
        self.rentSrv = RentService(rentFileRepo)

    def testGetRents(self):
        rents = self.rentSrv.get_rents()
        self.assertEqual(len(rents), 21)

    def testAddRent(self):
        rent1 = Rent(22, 12, 3, False)
        self.rentSrv.add_rent(rent1)
        rents = self.rentSrv.get_rents()
        self.assertEqual(len(rents), 22)
        self.assertEqual(int(rents[21].get_book_id()), 12)
        self.assertEqual(int(rents[21].get_client_id()), 3)

    def testUpdateRent(self):
        newRent = Rent(23, 10, 3, True)
        self.rentSrv.update_rent(22, newRent)
        rents = self.rentSrv.get_rents()
        self.assertEqual(len(rents), 22)
        self.assertEqual(int(rents[21].get_book_id()), 10)
        self.assertEqual(rents[21].get_isReturned(), "True")

    def testDeleteRent(self):
        self.rentSrv.delete_rent(23)
        rents = self.rentSrv.get_rents()
        self.assertEqual(len(rents), 21)

    def testSearchRent(self):
        rent = self.rentSrv.search_rent(10)
        self.assertEqual(str(rent.get_isReturned()), "True")


class TestFileServiceCases(unittest.TestCase):
    def setUp(self):
        bookFileRepo = BookFileRepository("BooksTest")
        clientFileRepo = ClientFileRepository('ClientsTest')
        rentFileRepo = RentFileRepository('RentsTest')
        sorts = Sorts()
        validator = Validators(bookFileRepo, clientFileRepo, rentFileRepo)
        self.srv = FileService(bookFileRepo, clientFileRepo, rentFileRepo, sorts, validator)

    def testMostRented(self):
        report = self.srv.theMostRented()
        self.assertEqual(report[0][0], "The Wicked King")
        self.assertEqual(report[5][0], "The Fellowship of the Ring")
        self.assertEqual(report[11][0], "Fall of Ruin and Wrath")

    def testSortByName(self):
        report = self.srv.sortClients_byName()
        self.assertEqual(len(report), 13)
        self.assertEqual(report[0][0], "Andreea")
        self.assertEqual(report[7][0], "James")
        self.assertEqual(report[12][0], "Tom")

    def testSortByNoRented(self):
        report = self.srv.sortClients_byNrRented()
        self.assertEqual(len(report), 8)
        self.assertEqual(report[0][0], "Barty")
        self.assertEqual(report[4][0], "Anya")
        self.assertEqual(report[7][0], "Andreea")

    def testFirst20MostActive(self):
        report = self.srv.first20_mostActiveClients()
        self.assertEqual(report[0][0], "Anya")
        self.assertEqual(report[1][0], "Andreea")

    def testFirst20MostRentedBooks(self):
        report = self.srv.first20_mostRentedBooks()
        self.assertEqual(report[0][0], "The Wicked King")
        self.assertEqual(report[1][0], "If We Were Villains")
        self.assertEqual(report[2][0], "The Queen of Nothing")
