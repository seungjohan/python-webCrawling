# # sentence = input("type the sentence: ")

# # print(sentence.split(" "))

# han = "My Name is %s".format(seungjohan)
# print(han)
# print(han%seungjohan)

number = []
# total = 0

while(True):

    num = int(input("type the number: "))

    number.append(num)

    for i in range(len(number)) :
        print("+ %s" %number[i])
        # total += number[i]

    print("= %s" %sum(number))
    # print("= %s" %total)

