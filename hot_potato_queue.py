# right is the front and left is the rear
# this also means that enqueue will be O(n) and dequeue will be O(1)
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)




def hotPotato(namelist, num):
    name_queue = Queue()

    for name in namelist:
        name_queue.enqueue(name)
    
    while name_queue.size() > 1:
        for i in range(num):
            name_queue.enqueue(name_queue.dequeue())
        
        name_queue.dequeue()
    
    return name_queue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))