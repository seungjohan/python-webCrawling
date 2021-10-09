# equationA = list(map(int, input("Type the coefficients of the first equation= ").split(" ")))
# equationB = list(map(int, input("Type the coefficients of the second equation= ").split(" ")))

equationA = [3,0,0,0,6,3]
equationB = [7,0,5,0,1]

answer = [0]

class polynomial(object):
    def __init__(self, list):
        self.exp = len(list) - 1
        self.coef = list

    def __reverse__(self, list):
        self.list = list[::-1]

    
