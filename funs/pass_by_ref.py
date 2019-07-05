def add(lst,v):
    print(id(lst))
    lst.append(v)
    print(id(lst))


l = [10,20]
print(id(l))
add(l,100)
print(id(l))
print(l)

