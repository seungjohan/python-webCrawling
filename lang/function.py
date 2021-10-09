avar = 1

def vartest(avar):
    avar += 1

# print(vartest(avar))
print(avar)

a = int(input())

def calculate(a):
    b = a * 2
    b = b*3 + 1

    return(b) 


print(calculate(a))


import random

num = random.randint(1, 20)
fnum = random.random()

vallist = [1,2,3,4,5]
val = random.choice(vallist)
fval = random.shuffle(vallist)

print("%d, %d, %s, %s" %(num, fnum, val, fval))
