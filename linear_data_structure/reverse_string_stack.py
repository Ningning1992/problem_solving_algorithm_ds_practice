class stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()
    def isempty(self):
        return self.list == []
    def peek(self):
        return self.list[len(self.list)-1]
    def size(self):
        return len(self.list)

def revstring(mystr):
    target_list = stack()
    for i in mystr:
        target_list.push(i)
    
    target_str = ''
    for i in range(target_list.size()):
        target_str += target_list.pop()
    
    return target_str

print(revstring('happy'))

