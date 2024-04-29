class ClientService:
    def __init__(self, clientRepository):
        self.__clientRepo = clientRepository

    def add_client(self, client):
        """
        Add a client
        :param client: the client
        """
        self.__clientRepo.add(client)

    def delete_client(self, client_id):
        """
        Delete a client
        :param client_id: the id of the client that needs to be deleted
        """
        self.__clientRepo.deleteClient(client_id)

    def update_client(self, c, new_client):
        """
        Update a client
        :param c: the id of the client that needs to be updated
        :param new_client: the updated client
        """
        self.__clientRepo.updateClient(c, new_client)

    def search_client(self, idClient):
        return self.__clientRepo.searchClient(idClient)

    def get_clients(self):
        """
        Get the list of the clients
        :return: the list of clients
        """
        return self.__clientRepo.get_allClients()
