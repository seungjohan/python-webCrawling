class A:
    def __init__(self):
        self.name = "sjh"
        print(self.name)


object = A()



class B:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)

object1 = B('smh')
object1.printName()

object2 = B('syo')
object2.printName()


class C:
    def sayHello(self):
        print("Hello My Fucking World!")
    def callSayHello(self):
        self.sayHello()

c = C()
C().sayHello()
c.callSayHello()



class D:
    def __del__(self):
        print("Good Bye My friend")

object5 = D()
del object5
