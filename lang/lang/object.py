class Node:
    def __init__(self, name, link):
        self.name = name
        self.next = link

    def __str__(self):
        return self.name

s = Node("morning", None)
s = Node("good", s)
s = Node("hello", s)

print(s)
print(s.next)
print(s.next.next)