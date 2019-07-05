def change(n):
    print(id(n))
    n = 0
    print(id(n))


v = 10
print(id(v))
change(v)
print(id(v))
print(v)
