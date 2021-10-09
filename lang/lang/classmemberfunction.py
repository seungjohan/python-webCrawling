# class A:
#     def printPython(self):
#         print("Python World")
#     @classmethod
#     def callMemberFunction(cls):
#         self.printPython()

# A.callMemberFunction()

# class B:
#     def __init__(self):
#         self.name = "ym"
#     @classmethod

#     def accessMemberVariable(cls):
#         self.name = "km"

# B.accessMemberVariable()


class Profile:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name: ",self.name, "Age: ",self.age)

kname = input("Name?: ")
kage = input("Age?: ")
profile1 = Profile(kname, kage)
profile2 = Profile("kss", "25")
profile1.info()
profile2.info()
print(profile1.name + profile1.age)