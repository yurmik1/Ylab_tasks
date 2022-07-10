

if __name__ == '__main__':
    class CyclicIterator:

        def __init__(self, lst):
            self.lst = list(lst)

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index >= len(self.lst):
                self.index = 0
            result = self.lst[self.index]
            self.index += 1
            return result


    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
