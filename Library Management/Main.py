from Repository.BookRepository import BookRepository
from Repository.ClientRepository import ClientRepository
from Repository.RentRepository import RentRepository
from Repository.BookFileRepository import BookFileRepository
from Repository.ClientFileRepository import ClientFileRepository
from Repository.RentFileRepository import RentFileRepository
from Service.BookService import BookService
from Service.ClientService import ClientService
from Service.RentService import RentService
from Service.FileService import FileService
from Service.Service import Service
from Tests.Tests import Tests
from UI.Console import Console
from Domain.Validators import Validators
from Utils.Sorts import Sorts


def main():
    # bookRepository = BookRepository()
    # clientRepository = ClientRepository()
    # rentRepository = RentRepository()
    # bookSrv = BookService(bookRepository)
    # bookSrv = BookService(bookFileRepository)
    # clientSrv = ClientService(clientRepository)
    # service = Service(bookRepository, clientRepository, rentRepository, validator)

    bookFileRepository = BookFileRepository("Files/Books")
    clientFileRepository = ClientFileRepository("Files/Clients")
    rentFileRepository = RentFileRepository("Files/Rents")
    rentSrv = RentService(rentFileRepository)
    bookFileSrv = BookService(bookFileRepository)
    clientFileSrv = ClientService(clientFileRepository)
    validator = Validators(bookFileRepository, clientFileRepository, rentFileRepository)
    sorts = Sorts()
    fileService = FileService(bookFileRepository, clientFileRepository, rentFileRepository, sorts, validator)
    test = Tests(bookFileRepository, clientFileRepository, rentFileRepository, bookFileSrv, clientFileSrv, rentSrv, fileService)
    console = Console(bookFileSrv, clientFileSrv, rentSrv, fileService, validator, test)
    console.start()


main()
