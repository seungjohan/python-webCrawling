class CreateStack:
    def __init__(self):
        self.stackarr = []

    def push(self, ele):
        return self.stackarr.append(ele)

    def pop(self, ele):
        try:
            return self.stackarr.pop()
        except IndexError:
            return print("Stack is Empty")

    def top(self):
        try:
            return self.stackarr[-1]
        except IndexError:
            return print("Stack is Empty")

    def __len__(self):
        return len(self.stackarr)

    def isEmpty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty == 1:
            print("Error")
            return exit
        else:
            return self.stackarr[-1]

    

def Calculator(tokens):
    stack = []

    op1 = stack.pop()
    op2 = stack.pop()

    for token in tokens:
        if token == '+':
            stack.pop(op1 + op2)
        if token == '-':
            stack.pop(op1 - op2)
        if token == '*':
            stack.pop(op1 * op2)
        if token == '/':
            stack.pop(op1 / op1)
        else:
            stack.push(token)

    return stack

def infixToProfix(tokenList):
    for token in tokenList:
        if type(token) is int:
            





# def solution:
#     operator = CreateStack()
#     operand = CreateStack()

#     calculate = str(input("Type the calculation which you want to know the result= ").split(" "))

#     Calculator(calculate)


# def test():
#     result = []
#     eval_r = []
#     test_case = ['5 + 3', '(1 + 2) * (3 + 4)', '7 * (9-(3+2))', '3 + (2 - 3 * (1 + 2 + ( 4 * 2 - 1)))']
#     for tc in test_case:
#         result += [solution(tc)]
#         eval_r += [eval(tc)]

#     return "result : {} \neval: {}".format(result, eval_r)