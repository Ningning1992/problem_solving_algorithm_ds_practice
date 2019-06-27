# using left of the list as rear and right as front
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def palchecker(aString):
    mydeque = Deque()
    for character in aString:
        mydeque.addRear(character)
    
    still_same = True
    while mydeque.size() > 1 and still_same:
        front_c = mydeque.removeFront()
        end_c = mydeque.removeRear()
        if front_c != end_c:
            still_same = False
    
    return still_same

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
