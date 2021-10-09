# vertical triangle
print("---vertical triangle---")
for i in range(7):
    print("*"*i)

print("\n\n")
# regular triangle
print("---regular triangle---")
for i in range(7):
    print(" "*(7//2-i) + "*"*i)

print("\n\n")
# reverse triangle
print("---reverse triangle---")
for i in range(7):
    print(" " * (6-i) + "*"*i)

print("\n\n")
# diamond
print("---diamond---")
for i in range(7):
    print(" " * (6-i) + "*"*i)

for i in range(7):
    print(" "*i + "*"*(6-i))

a = divmod(7,3)

# reverse diamond
print("---reverse diamond---")


