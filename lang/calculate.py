calculate = input("Type the equation= ")

while(True):
    total = 0
    calculate.split("+")

    for i in range(len(calculate)):
        total += int(calculate[i])