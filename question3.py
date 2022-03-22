class List:

    def __init__(self, new_lst):
        self.lst = new_lst

    def __getitem__(self, item):
        temp = self.lst
        i = 0
        if isinstance(item, int):
            return temp[item]
        while isinstance(temp[item[i]], list):
            if i == len(item) - 1:
                return temp[item[i]]
            temp = temp[item[i]]
            i = i + 1
        return temp[item[i]]

    def __sizeof__(self):
        """
        :return: the number of elements in the list
        """
        return len(self.lst)

    def append(self, item):
        """
        appends the item to the end of the list
        :param item: the element to append
        """
        self.lst.append(item)

    def remove(self, element):
        """
        removes an element from the list.
        :param element: the element to remove
        """
        self.lst.remove(element)


if __name__ == '__main__':
    mylist = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ]
    )

    print(mylist[0, 1, 3])
    print(mylist[0, 1])
    print(mylist[0])

    mylist.append([2, 4, 3])
    print(mylist[3])
    print(mylist.__sizeof__())

    mylist.remove([2, 4, 3])
    print(mylist.__sizeof__())