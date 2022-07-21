# create a class that keeps track of how many objects of the same type were created

class Count:
    counter =[0]
    def __init__(self):
        self.counter.append(self.counter.pop(0)+1)

object1=Count()
object2=Count()
object3=Count()
object4=Count()
object5=Count()

print(Count.counter)

