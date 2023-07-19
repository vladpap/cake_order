a = [1, 2, 3, 4, 5]
print(id(a))
for i in a:
    print(i)
    a = []
print(id(a))
