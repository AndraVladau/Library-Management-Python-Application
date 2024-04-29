class RentRepository:
    def __init__(self):
        self.__rentList = []

    def addRent(self, rent):
        """
        Add a rent
        :param rent: the rent
        """
        self.__rentList.append(rent)

    def deleteRent(self, idRent):
        """
        Delete a rent
        :param idRent: the id of the rent that we want to delete
        """
        result = []
        for i in range(len(self.__rentList)):
            if self.__rentList[i].get_rent_id() != idRent:
                result.append(self.__rentList[i])
        self.__rentList = result

    def updateRent(self, idRent, newRent):
        """
        Update a rent
        :param idRent: the id of the rent that we want to update
        :param newRent: the new rent
        """
        result = []
        for i in range(len(self.__rentList)):
            if self.__rentList[i].get_rent_id() != idRent:
                result.append(self.__rentList[i])
            else:
                result.append(newRent)
        self.__rentList = result

    def searchRent(self, idRent):
        """
        Search for a rent
        :param idRent: the id of rent that we search for
        :return: the rent that we search for or message if the rent does not exist in the list
        """
        ok = False
        for i in range(len(self.__rentList)):
            if self.__rentList[i].get_rent_id() == idRent:
                result = self.__rentList[i]
                return result

        if not ok:
            print("The rent that you are searching for does not exist!")

    def get_allRents(self):
        """
        Get the list with rents
        :return: the list of rents
        """
        return self.__rentList


