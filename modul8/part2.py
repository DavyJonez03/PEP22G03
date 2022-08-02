# Iterator

class MyIterator():
    def __init__(self, number:int):
        self.number = number

    def __iter__(self):

    def __next__(self):
        pass

for i in MyIterator(3):
    print(i)