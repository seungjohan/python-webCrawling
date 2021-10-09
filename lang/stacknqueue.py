class stack:
    def __init__(self):
        self.arr = []

    def push(self, ele):
        return self.arr.append(ele)

    def pop(self, ele):
        try:
            return self.arr.pop()
        except IndexError:
            return print("Stack is Empty")

    def top(self):
        try:
            return self.arr[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.arr)

    # def isEmpty(self):
    #     return self.arr == [0]

    def isEmpty(self):
        return self.__len__() == 0

    def peek(self):
        if self.isEmpty():
            print("Error")
            exit
        
        return self.arr[-1]


MAX_QSIZE = 10

class queue:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        is_empty = False

        if self.size == 0:
            is_empty = True
        return is_empty

    def isFull(self):
        is_full = False

        if self.size == 10:
            is_full = True
        return is_full

    def enqueue(self, ele):
        self.arr.append(ele)

    def dequeue(self):
        if self.isEmpty():
            return print("Queue is Empty")

        return self.arr.pop()

    def size(self):
        return len(self.arr)

    def peek(self):
        if self.isEmpty():
            return print("Queue is Empty")
        return self.arr[0]

MAX_QSIZE = 10

class circleQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr = [None] * MAX_QSIZE

    # def size(self):
    #     return len(self.arr)

    def isEmpty(self):
        is_empty = False

        if self.front == self.rear:
            is_empty = True
        return is_empty

    def isFull(self):
        is_full = False

        if self.front == self.rear % MAX_QSIZE:
            is_full = True
        return is_full

    def clear(self):
        self.front = self.rear

    def enqueue(self, ele):
        if not self.isFull():
            self.arr[self.rear] = ele
            self.rear -= 1

    def dqueue(self):
        if not self.isEmpty():
            self.arr.pop(self.front)
            self.front += 1

    def peek(self):
        if not self.isEmpty():
            return self.arr[(self.front + 1)%MAX_QSIZE]




# isEmpty, isFull, claer, enqueue, dqueue, peek

    
