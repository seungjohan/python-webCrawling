class A:
    num = 0
    
    def __init__(self):
        self.num = self.num + 1

class B:
    num = 0

    def __init__(self):
        B.num = B.num + 1


a1 = A()
a2 = A()
print(a1.num)
print(a2.num)

b1 = B()
b2 = B()
print(b1.num)
print(b2.num)