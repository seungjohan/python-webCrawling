class HelloBot:
    print('HelloBot')


hello_bot1 = HelloBot()
# hello_bot2 = HelloBot()


class B:
    def __init__(self):
        print("hello, python world")

b = B()

class A:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

object= A(1,2,3)

num = object.a
print("%s" %num)


