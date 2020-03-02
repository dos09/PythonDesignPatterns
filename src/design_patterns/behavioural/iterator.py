"""
Iterator is a behavioral design pattern that lets you traverse elements of a 
collection without exposing its underlying representation 
(list, stack, tree, etc.).
"""

import abc


class Container(abc.ABC):

    @abc.abstractmethod
    def get_iterator(self):
        raise NotImplementedError()


class SimpleDataStructure(Container):

    def __init__(self, arr):
        self.arr = arr or []

    def get_iterator(self):
        return SimpleDataStructureIterator(self)


class SimpleDataStructureIterator:

    def __init__(self, simple_data_structure):
        self.arr = simple_data_structure.arr
        self.index = 0
        self.max_index = len(self.arr) - 1

    def has_next(self):
        return self.index <= self.max_index

    def next(self):
        index = self.index
        self.index += 1
        return self.arr[index]


def run():
    data = SimpleDataStructure([7, 8, 10, 12])
    it = data.get_iterator()
    while it.has_next():
        print(it.next(), end=' ')


if __name__ == '__main__':
    run()
