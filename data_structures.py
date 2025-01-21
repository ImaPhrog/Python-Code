import random
class stack:
    def __init__(self, contents = []):
        self.__items = contents
    def pop(self):
        if self.__isEmpty:
            return "empty"
        else:
            item = self.__items[-1]
            del self.__items[-1]
            return item

    def push(self, item):
        self.__items.append(item)

    def peek(self):
        if self.__isEmpty():
            return "empty"
        else:
            return self.__items[-1]

    def __isEmpty(self):
        if self.__items == []:
            return True
        else:
            return False

class queue:
    def __init__(self, content = []):
        self.items = content
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, item):
       self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        else:
            item = self.items[0]
            del self.items[0]
            return item

    def size(self):
        size = len(self.items)
        return size

class cqueue:
    def __init__(self, max_size):
        self.items = [""] * max_size
        self.front = 0
        self.rear = 0
        self.max_size = max_size
        self.size = 0

    def __str__(self):
        returnlist = ""
        for i in range(self.size):
            x = i % self.max_size
            item = self.items[self.rear+x]
            returnlist += str(item)
        return returnlist

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False


    def isFull(self):
        if self.size == self.max_size:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.isFull():
            return "full"
        else:
            self.items[self.front] = item
            self.size += 1
            self.front += 1
            self.front = self.front % self.max_size

    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        else:
            self.size -= 1
            self.rear += 1
            self.rear = self.rear % self.max_size

class bucket:
    def __init__(self, contents = []):
        self.__items = contents
    
    def drop(self, item):
        self.__items.append(item)

    def look(self):
        return random.choice(self.__items)

    def grab(self):
        if self.__isEmpty():
            return "Empty"
        else:
            i = random.randint(0,self.__length()-1)
            item = self.__items[i]
            del self.__items[i]
            return item

    def __isEmpty(self):
        if self.__items == []:
            return True
        else:
            return False
    def __length(self):
        return len(self.__items)
    
bucket1 = bucket([0,1,2,3,4,5])
print(bucket1.grab())
bucket1.drop(389)
print(bucket1.grab())