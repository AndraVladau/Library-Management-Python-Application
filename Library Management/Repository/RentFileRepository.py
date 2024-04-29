from Domain.Rent import Rent


class RentFileRepository:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        rents = []
        with open(self.__filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                rentLine = line.split(',')
                idRent = rentLine[0]
                idBook = rentLine[1]
                idClient = rentLine[2]
                isReturned = rentLine[3]
                rent = Rent(idRent, idBook, idClient, isReturned)
                rents.append(rent)
        file.close()
        return rents

    def save_in_file(self, rents):
        with open(self.__filename, 'w') as file:
            for rent in rents:
                file.write(
                    str(rent.get_rent_id()) + ',' + str(rent.get_book_id()) + ',' + str(rent.get_client_id()) + ',' + str(rent.get_isReturned()) + '\n')
            file.close()

    def addRent(self, rent):
        """
        Add a rent
        :param rent: the rent
        """
        rents = self.load_from_file()
        rents.append(rent)
        self.save_in_file(rents)

    def deleteRent(self, idRent):
        """
        Delete a rent
        :param idRent: the id of the rent that we want to delete
        """
        rents = self.load_from_file()
        result = []
        for i in range(len(rents)):
            if int(rents[i].get_rent_id()) != idRent:
                result.append(rents[i])
        rents = result
        self.save_in_file(rents)

    def updateRent(self, idRent, newRent):
        """
        Update a rent
        :param idRent: the id of the rent that we want to update
        :param newRent: the new rent
        """
        rents = self.load_from_file()
        result = []
        for i in range(len(rents)):
            if int(rents[i].get_rent_id()) != idRent:
                result.append(rents[i])
            else:
                result.append(newRent)
        rents = result
        self.save_in_file(rents)

    def searchRent(self, idRent):
        """
        Search for a rent
        :param idRent: the id of rent that we search for
        :return: the rent that we search for or message if the rent does not exist in the list
        """
        rents = self.load_from_file()
        ok = False
        for i in range(len(rents)):
            if int(rents[i].get_rent_id()) == idRent:
                result = rents[i]
                return result

        if not ok:
            print("The rent that you are searching for does not exist!")

    def get_allRents(self):
        """
        Get the list with rents
        :return: the list of rents
        """
        return self.load_from_file()
