equationA = list(map(int, input("Type the coefficients of the first equation= ").split(" ")))
equationB = list(map(int, input("Type the coefficients of the second equation= ").split(" ")))

answer = []
equ_a = []
equ_b = []

class polynomial(object):
    def __init__(self, list):
        self.exp = len(list) - 1
        self.coef = list

    def __reverse__(self, list):
        self.list = list[::-1]


def polynomial_add(Apos, Bpos):
    degree_a = len(Apos)
    degree_b = len(Bpos)

    for i in range(degree_a):
        equ_a.append([i, equationA[i]])
    for i in range(degree_b):
        equ_b.append([i, equationB[i]])

    while degree_a>=0 & degree_b>=0:
        if equ_a.exp > degree_b.exp:
            answer.append([i, equ_a[i]])
        if degree_a.exp == degree_b.exp:
            answer.append([i, equ_a[i] + equ_b[i]])
        if degree_a.exp < degree_b.exp:
            answer.append([i, equ_b[i]])

    while degree_a>=0:
        answer.append([i, equ_a[i]])

    while degree_b>=0:
        answer.append([i, equ_b[i]])


    return print(answer)


# def polynomial_mul(Apos, Bpos):
#     degree_a = len(Apos)
#     degree_b = len(Bpos)




equA = polynomial()
equB = polynomial()

