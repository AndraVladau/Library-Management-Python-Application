class ClientRepository:
    def __init__(self):
        self.__clientsList = []

    def add(self, client):
        """
        Add a client
        :param client: the client
        """
        self.__clientsList.append(client)

    def deleteClient(self, client_id):
        """
        Delete a client
        :param client_id: the id of the client that needs to be deleted
        """
        result = []
        for i in range(len(self.__clientsList)):
            if self.__clientsList[i].get_client_id() != client_id:
                result.append(self.__clientsList[i])
        self.__clientsList = result

    def updateClient(self, b, new_client):
        """
        Update a client
        :param b: the id of the client that needs to be updated
        :param new_client: the updated client
        """
        result = []
        for i in range(len(self.__clientsList)):
            if self.__clientsList[i].get_client_id() != b:
                result.append(self.__clientsList[i])
            else:
                result.append(new_client)
        self.__clientsList = result

    def searchClient(self, idClient):
        """
        Search for a client in the clients list
        :param idClient: the id of the client that you are searching for
        :return: the client or message if the client does not exist in the list
        """
        ok = False
        for i in range(len(self.__clientsList)):
            if int(self.__clientsList[i].get_client_id()) == int(idClient):
                result = self.__clientsList[i]
                return result
        if not ok:
            print("The client that you are searching for does not exist!")

    def get_allClients(self):
        """
        Get the list of the clients
        :return: the list of clients
        """
        return self.__clientsList

    def getClientName(self, idClient):
        for i in range(len(self.__clientsList)):
            if int(self.__clientsList[i].get_client_id()) == int(idClient):
                name = self.__clientsList[i].get_name()
                return name
