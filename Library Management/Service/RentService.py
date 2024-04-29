class RentService:
    def __init__(self, rentRepository):
        self.__rentRepo = rentRepository

    def add_rent(self, rent):
        """
        Add a rent
        :param rent: the rent
        """
        self.__rentRepo.addRent(rent)

    def delete_rent(self, idRent):
        """
        Delete a rent
        :param idRent: the id of the rent that we want to delete
        """
        self.__rentRepo.deleteRent(idRent)

    def update_rent(self, idRent, newRent):
        """
        Update a rent
        :param idRent: the id of the rent that we want to update
        :param newRent: the new rent
        """
        self.__rentRepo.updateRent(idRent, newRent)

    def search_rent(self, idRent):
        """
        Search for a rent
        :param idRent: the id of rent that we search for
        :return: the rent that we search for or message if the rent does not exist in the list
        """
        return self.__rentRepo.searchRent(idRent)

    def get_rents(self):
        """
        Get the list with rents
        :return: the list of rents
        """
        return self.__rentRepo.get_allRents()
