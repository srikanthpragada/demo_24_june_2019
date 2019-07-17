def squares(num):
    for i in range(1, num + 1):
        yield i * i


for n in squares(5):
    print(n)
