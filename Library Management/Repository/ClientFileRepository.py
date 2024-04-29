from Domain.Client import Client


class ClientFileRepository:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        clients = []
        with open(self.__filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                clientLine = line.split(',')
                idClient = clientLine[0]
                name = clientLine[1]
                cnp = clientLine[2]
                client = Client(idClient, name, cnp)
                clients.append(client)
        file.close()
        return clients

    def save_in_file(self, clients):
        with open(self.__filename, 'w') as file:
            for client in clients:
                file.write(str(client.get_client_id()) + ',' + client.get_name() + ',' + client.get_cnp() + '\n')
            file.close()

    def add(self, client):
        """
        Add a client
        :param client: the client
        """
        clients = self.load_from_file()
        clients.append(client)
        self.save_in_file(clients)

    def deleteClient(self, client_id):
        """
        Delete a client
        :param client_id: the id of the client that needs to be deleted
        """
        clients = self.load_from_file()
        result = []
        for i in range(len(clients)):
            if int(clients[i].get_client_id()) != client_id:
                result.append(clients[i])
        clients = result
        self.save_in_file(clients)

    def updateClient(self, b, new_client):
        """
        Update a client
        :param b: the id of the client that needs to be updated
        :param new_client: the updated client
        """
        clients = self.load_from_file()
        result = []
        for i in range(len(clients)):
            if int(clients[i].get_client_id()) != b:
                result.append(clients[i])
            else:
                result.append(new_client)
        clients = result
        self.save_in_file(clients)

    def searchClient(self, idClient):
        """
        Search for a client in the clients list
        :param idClient: the id of the client that you are searching for
        :return: the client or message if the client does not exist in the list
        """
        clients = self.load_from_file()
        ok = False
        for i in range(len(clients)):
            if int(clients[i].get_client_id()) == int(idClient):
                result = clients[i]
                return result
        if not ok:
            print("The client that you are searching for does not exist!")

    def get_allClients(self):
        """
        Get the list of the clients
        :return: the list of clients
        """
        return self.load_from_file()

    def getClientName(self, idClient):
        clients = self.load_from_file()
        for i in range(len(clients)):
            if int(clients[i].get_client_id()) == int(idClient):
                name = clients[i].get_name()
                return name
