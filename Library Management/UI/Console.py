from Domain.Book import Book
from Domain.Client import Client
from Domain.Rent import Rent


class Console:
    def __init__(self, bookSrv, clientSrv, rentSrv, srv, validator, tests):
        self.__srvBook = bookSrv
        self.__srvClient = clientSrv
        self.__srvRent = rentSrv
        self.__srv = srv
        self.__validator = validator
        self.__tests = tests

    def tests(self):
        self.__tests.test_create_book()
        self.__tests.test_create_client()
        self.__tests.test_create_rent()
        self.__tests.test_add_book()
        self.__tests.test_update_book()
        self.__tests.test_delete_book()
        self.__tests.test_add_client()
        self.__tests.test_update_client()
        self.__tests.test_delete_client()
        self.__tests.test_addBook()
        self.__tests.test_updateBook()
        self.__tests.test_deleteBook()
        self.__tests.test_addClient()
        self.__tests.test_updateClient()
        self.__tests.test_deleteClient()
        self.__tests.test_add_rent()
        self.__tests.test_update_rent()
        self.__tests.test_delete_rent()
        self.__tests.test_addRent()
        self.__tests.test_updateRent()
        self.__tests.test_deleteRent()
        self.__tests.test_reports()

    def printMenu(self):
        print("Options:")
        print("BOOK. Book options")
        print("CLIENT. Client options")
        print("RENT. Rent options")
        print("REPORT. Reports")
        print("EXIT. Exit")

    def bookMenu(self):
        print("1. Add a book.")
        print("2. Delete a book.")
        print("3. Update a book.")
        print("4. Search for a book.")
        print("5. Create a random book.")
        print("P. Print all books.")
        print("E. Exit the book options.")

    def clientMenu(self):
        print("1. Add a client.")
        print("2. Delete a client.")
        print("3. Update a client.")
        print("4. Search for a client.")
        print("P. Print all clients.")
        print("E. Exit the client options.")

    def rentMenu(self):
        print("1. Add a rent.")
        print("2. Delete a rent.")
        print("3. Update a rent.")
        print("4. Search for a rent.")
        print("P. Print all rents.")
        print("E. Exit the rent options.")

    def reportsMenu(self):
        print("1. The most rented books.")
        print("2. The clients, who have rented books, sorted ascending by name.")
        print("3. The clients, who have rented books, sorted ascending by the number of books rented.")
        print("4. Print the first 20% of the clients that are the most active.")
        print("E. Exit the reports.")

    def read_book(self):
        book_id = input("The book's ID: ")
        while not self.__validator.validateBookID(book_id):
            book_id = input("The book's ID: ")

        title = input("The book's title: ")
        while not self.__validator.validateStrings(title):
            title = input("The book's title: ")

        author = input("The book's author: ")
        while not self.__validator.validateStrings(author):
            author = input("The book's author: ")

        description = input("The book's description: ")
        while not self.__validator.validateStrings(description):
            description = input("The book's description: ")

        return Book(book_id, title, author, description)

    def read_client(self):
        client_id = input("The client's ID: ")
        while not self.__validator.validateClientID(client_id):
            client_id = input("The client's ID: ")

        name = input("The client's name: ")
        while not self.__validator.validateStrings(name):
            name = input("The client's name: ")

        cnp = input("The client's cnp: ")
        while not self.__validator.validateStrings(cnp):
            cnp = input("The client's cnp: ")

        return Client(client_id, name, cnp)

    def read_rent(self):
        rent_id = input("The rent's ID: ")
        while not self.__validator.validateRentID(rent_id):
            rent_id = input("The rent's ID: ")

        book_id = input("The book's ID: ")
        if not self.__validator.idBookExists(book_id):
            return 0

        client_id = input("The client's ID: ")
        if not self.__validator.idClientExists(client_id):
            return 0

        isReturned = bool(input("The book is returned: "))

        return Rent(rent_id, book_id, client_id, isReturned)

    def printBooks(self):
        books = self.__srvBook.get_books()
        for i in range(len(books)):
            print(books[i])
        print("")

    def printClients(self):
        clients = self.__srvClient.get_clients()
        for i in range(len(clients)):
            print(clients[i])
        print("")

    def printRents(self):
        rents = self.__srvRent.get_rents()
        for i in range(len(rents)):
            print(rents[i])
        print("")

    def add_book_UI(self):
        book = self.read_book()

        try:
            self.__srvBook.add_book(book)
            print("The book was successfully added!")
        except ValueError as ve:
            print("Error: " + ve)

    def delete_book_UI(self):
        book_id = input("The book's ID that you want to delete: ")
        try:
            self.__srvBook.delete_book(book_id)
            print("The book was successfully deleted!")
        except ValueError as ve:
            print("Error: " + ve)

    def update_book_UI(self, string):
        book_id = int(input("The book's ID that you want to update: "))
        book = self.read_book()
        if string == 'a':
            try:
                self.__srvBook.update_book(book_id, book)
                print("The book was successfully updated!")
            except ValueError as ve:
                print("Error: " + ve)
        elif string == 'b':
            try:
                self.__srvBook.update_book_recursive(book_id, book)
                print("The book was successfully updated!")
            except ValueError as ve:
                print("Error: " + ve)

    def search_book_UI(self):
        book_id = int(input("The book's ID that you search for: "))
        try:
            result = self.__srvBook.search_book(book_id)
            print(result)
        except ValueError as ve:
            print("Error: " + ve)

    def add_client_UI(self):
        client = self.read_client()

        try:
            self.__srvClient.add_client(client)
            print("The client was successfully added!")
        except ValueError as ve:
            print("Error: " + ve)

    def delete_client_UI(self):
        client_id = int(input("The client's ID that you want to delete: "))
        try:
            self.__srvClient.delete_client(client_id)
            print("The client was successfully deleted!")
        except ValueError as ve:
            print("Error: " + ve)

    def update_client_UI(self):
        client_id = int(input("The client's ID that you want to update: "))
        client = self.read_client()
        try:
            self.__srvClient.update_client(client_id, client)
            print("The client was successfully updated!")
        except ValueError as ve:
            print("Error: " + ve)

    def search_client_UI(self):
        client_id = int(input("The client's ID that you search for: "))
        try:
            result = self.__srvClient.search_client(client_id)
            print(result)
        except ValueError as ve:
            print("Error: " + ve)

    def add_rent_UI(self):
        rent = self.read_rent()
        if rent != 0:
            try:
                self.__srvRent.add_rent(rent)
                print("The rent was successfully added!")
            except ValueError as ve:
                print("Error: " + ve)

    def delete_rent_UI(self):
        rent_id = int(input("The rent's ID that you want to delete: "))
        try:
            self.__srvRent.delete_rent(rent_id)
            print("The rent was successfully deleted!")
        except ValueError as ve:
            print("Error: " + ve)

    def update_rent_UI(self):
        rent_id = int(input("The rent's ID that you want to update: "))
        rent = self.read_rent()
        try:
            self.__srvRent.update_rent(rent_id, rent)
            print("The rent was successfully updated!")
        except ValueError as ve:
            print("Error: " + ve)

    def search_rent_UI(self):
        rent_id = int(input("The rent's ID that you search for: "))
        try:
            result = self.__srvRent.search_rent(rent_id)
            print(result)
        except ValueError as ve:
            print("Error: " + ve)

    def mostRented(self):
        report = self.__srv.theMostRented()
        for i in range(len(report)):
            print(report[i][0])

    def sortClientsName(self):
        report = self.__srv.sortClients_byName()
        for i in range(len(report)):
            print(report[i][0] + ", " + report[i][1])

    def sortClientsNrRented(self):
        report = self.__srv.sortClients_byNrRented()
        for i in range(len(report)):
            print(report[i][0] + ", " + str(report[i][1]))

    def first20MostActive(self):
        report = self.__srv.first20_mostActiveClients()
        for i in range(len(report)):
            print(report[i][0])

    def first20MostRentedBooks(self):
        report = self.__srv.first20_mostRentedBooks()
        for i in range(len(report)):
            print(report[i][0] + ', number of clients= ' + str(report[i][1]))

    def createRandomBook(self):
        self.__srv.createNewBook()

    def self_populate(self):
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

        self.__srvBook.add_book(book1)
        self.__srvBook.add_book(book2)
        self.__srvBook.add_book(book3)
        self.__srvBook.add_book(book4)
        self.__srvBook.add_book(book5)

        self.__srvClient.add_client(client1)
        self.__srvClient.add_client(client2)
        self.__srvClient.add_client(client3)
        self.__srvClient.add_client(client4)
        self.__srvClient.add_client(client5)

        self.__srvRent.add_rent(rent1)
        self.__srvRent.add_rent(rent2)
        self.__srvRent.add_rent(rent3)
        self.__srvRent.add_rent(rent4)
        self.__srvRent.add_rent(rent5)
        self.__srvRent.add_rent(rent6)
        self.__srvRent.add_rent(rent7)
        self.__srvRent.add_rent(rent8)
        self.__srvRent.add_rent(rent9)
        self.__srvRent.add_rent(rent10)

    def start(self):
        #self.tests()
        print("All tests passed!")

        #self.self_populate()

        while True:
            self.printMenu()
            print("")
            print("Your option: ")
            cmd = input("--> ")
            option = cmd.split(' ')
            if option[0] == "BOOK":
                ok = True
                while ok:
                    self.bookMenu()
                    print("")
                    print("Your command: ")
                    command = input("--> ")
                    command.upper().strip()
                    if command == '1':
                        self.add_book_UI()
                    elif command == '2':
                        self.delete_book_UI()
                    elif command == '3':
                        print("Options: ")
                        print("a. Non-recursive.")
                        print("b. Recursive.")
                        string = input("--> ")
                        self.update_book_UI(string)
                    elif command == '4':
                        self.search_book_UI()
                    elif command == '5':
                        self.createRandomBook()
                    elif command == 'P':
                        self.printBooks()
                    elif command == 'E':
                        print("")
                        ok = False
            elif option[0] == "CLIENT":
                ok = True
                while ok:
                    self.clientMenu()
                    print("")
                    print("Your command: ")
                    command = input("--> ")
                    command.upper().strip()
                    if command == '1':
                        self.add_client_UI()
                    elif command == '2':
                        self.delete_client_UI()
                    elif command == '3':
                        self.update_client_UI()
                    elif command == '4':
                        self.search_client_UI()
                    elif command == 'P':
                        self.printClients()
                    elif command == 'E':
                        print("")
                        ok = False
            elif option[0] == "RENT":
                ok = True
                while ok:
                    self.rentMenu()
                    print("")
                    print("Your command: ")
                    command = input("--> ")
                    command.upper().strip()
                    if command == '1':
                        self.add_rent_UI()
                    elif command == '2':
                        self.delete_rent_UI()
                    elif command == '3':
                        self.update_rent_UI()
                    elif command == '4':
                        self.search_rent_UI()
                    elif command == 'P':
                        self.printRents()
                    elif command == 'E':
                        print("")
                        ok = False
            elif option[0] == "REPORT":
                ok = True
                while ok:
                    self.reportsMenu()
                    print("")
                    print("Your command: ")
                    command = input("--> ")
                    command.upper().strip()
                    if command == '1':
                        self.mostRented()
                    elif command == '2':
                        self.sortClientsName()
                    elif command == '3':
                        self.sortClientsNrRented()
                    elif command == '4':
                        self.first20MostActive()
                    elif command == '5':
                        self.first20MostRentedBooks()
                    elif command == 'E':
                        print("")
                        ok = False
            elif option[0] == "EXIT":
                print("Goodbye!")
                return False
            else:
                print("Invalid option!")
