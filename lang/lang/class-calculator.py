# result = 0
# result2 = 0

# def adder(num):
#     global result
#     result += num

#     return result

# def adder2(num):
#     global result2
#     result2 += num

#     return result2

# print(adder(3))
# print(adder(4))

# print(adder2(3))
# print(adder2(4))


class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result = self.result + num
        
        return self.result

class SuperCalculator(Calculator):
    def substractor(self, num):
        self.result = self.result - num

        return self.result

class UltraSuperCalculator(Calculator):
    def multiplier(self, num):
        self.result = self.result * num

        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))

print(cal2.adder(3))
print(cal2.adder(4))

        
class BookReader:
    def __init__(self):
        self.name = str()
        self.title = str()

    def read_book(self):
        print(self.name + ' is reading book')

    def title_book(self):
        print(self.title + ' is the title')


reader = BookReader()
reader.name = 'Chris'
reader.title = 'self confience'
reader.read_book()
reader.title_book()