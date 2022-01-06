# equationA = list(map(int, input("Type the coefficients of the first equation= ").split(" ")))
# equationB = list(map(int, input("Type the coefficients of the second equation= ").split(" ")))

equationA = [3,0,0,0,6,3]
equationB = [7,0,5,0,1]

answer = [0]

    
def polynomial_add(Apos, Bpos):
    degree_a = len(Apos) - 1
    degree_b = len(Bpos) - 1

    while degree_a>=0 & degree_b>=0:
        i = 0
        if degree_a > degree_b:
            answer[i] = equationA[i]
            i+=1
            degree_a-=1
        elif degree_a == degree_b:
            answer[i] = equationA[i] + equationB[i]
            i+=1
            degree_a-=1
            degree_b-=1
        else:
            answer[i] = equationB[i]
            i+=1
            degree_b-=1

    while degree_a >=0:
        answer[i] = equationA[i]
        i+=1
        degree_a-=1

    while degree_b >=0:
        answer[i] = equationA[i]
        i+=1
        degree_b-=1
            
    return print(answer)


def polynomial_add2(Apos, Bpos):
    reversed_apos = Apos[::-1]
    reversed_bpos = Bpos[::-1]
    reversed_answer = []

    degree_a = len(Apos) - 1
    degree_b = len(Bpos) - 1

    while(degree_a >=0 & degree_b >=0):
        if degree_a > degree_b :
            for i in range(degree_b):
                reversed_answer[i] = reversed_apos[i] + reversed_bpos[i]
            for i in range(degree_b + 1, degree_a):
                reversed_answer[i] = reversed_apos[i]
        elif degree_a == degree_b :
            for i in range(degree_a):
                reversed_answer[i] = reversed_apos[i] + reversed_bpos[i]
        else :
            for i in range(degree_a):
                reversed_answer[i] = reversed_apos[i] + reversed_bpos[i]
            for i in range(degree_a + 1, degree_b):
                reversed_answer[i] = reversed_bpos[i]


    while degree_a >= 0:
        for i in range(degree_a):
            reversed_answer[i] = reversed_apos[i]


    while degree_b >= 0:
        for i in range(degree_b):
            reversed_answer[i] = reversed_bpos[i]






def polynomial_mul(Apos, Bpos):
    degree_a = len(Apos) - 1
    degree_b = len(Bpos) - 1
    degree_c = degree_a * degree_b







polynomial_add2(equationA, equationB)

# polynomial_add(equationA, equationB)
# polynomial_mul(equationA, equationB)



