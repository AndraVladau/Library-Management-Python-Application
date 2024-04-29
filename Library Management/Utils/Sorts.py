class Sorts:
    def compare_for_quickSort(self, x, y):
        if x < y:
            return True
        return False

    def quickSort(self, array, key=None, reverse=None):
        """
        Quick Sort
        :param reverse:
        :param array: the list that we want to sort
        :param key: after what we sort
        :return: the sorted list
        """

        if key is None:
            key = lambda x: x

        if len(array) == 0:
            return []
        pivot = array[0]
        if key is True:
            pivot = key(pivot)
        less = [x for x in array[1:] if self.compare_for_quickSort(x, pivot) is True]
        greater = [x for x in array[1:] if self.compare_for_quickSort(x, pivot) is False]
        result = self.quickSort(less, key=key, reverse=None) + [array[0]] + self.quickSort(greater, key=key, reverse=None)
        return result

    def compare_for_gnomeSort(self, x, y, reverse):
        if reverse:
            if x <= y:
                return True
        else:
            if x >= y:
                return True
        return False

    def gnomeSort(self, array, key=None, reverse=None):
        """
        Gnome sort
        :param array: the list that we want to sort
        :param key: after what we sort
        :param reverse: to sort ascending or descending
        :return: the sorted list
        """
        i = 1
        while i < len(array):
            if self.compare_for_gnomeSort(array[i][1], array[i - 1][1], reverse):
                i += 1
            else:
                array[i], array[i - 1] = array[i - 1], array[i]
                i -= 1
                if i == 0:
                    i = 1
        return array
