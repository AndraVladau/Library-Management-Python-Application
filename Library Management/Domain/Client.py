class Client:
    def __init__(self, client_id, name, cnp):
        self.__client_id = client_id
        self.__name = name
        self.__cnp = cnp

    def get_client_id(self):
        """
        Get the client's id
        :return: the client's id
        """
        return self.__client_id

    def get_name(self):
        """
        Get the client's name
        :return: the client's name
        """
        return self.__name

    def get_cnp(self):
        """
        Get the client's cnp
        :return: the client's cnp
        """
        return self.__cnp

    def set_client_id(self, new_client_id):
        """
        Set the new id of the client
        :param new_client_id: the new id of the client
        """
        self.__client_id = new_client_id

    def set_name(self, new_name):
        """
        Set the new name of the client
        :param new_name: the new name of the client
        """
        self.__name = new_name

    def set_cnp(self, new_cnp):
        """
        Set the new cnp of the client
        :param new_cnp: the new cnp of the client
        """
        self.__cnp = new_cnp

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, Client):
            return False
        return self.__client_id == other.__client_id and self.__name == other.__name and self.__cnp == other.__cnp

    def __str__(self):
        return str(self.__client_id) + ". " + self.__name + ", " + self.__cnp
