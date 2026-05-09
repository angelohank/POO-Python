from collections.abc import MutableSequence
class ClubeDoLivro(MutableSequence):
    def __delitem__(self, index):
        print('Deleting item at index', index)

    def __getitem__(self, item):
        print('Getting item at index', item)

    def __len__(self):
        return len(self)

    def __setitem__(self, index, value):
        print('Setting item at index', index)

    def insert(self, index, value):
        print('Inserting item at index', index)


clube = ClubeDoLivro()