def details(**values):
    print(values)


def fun(*, a, b):
    print(a, b)


fun(a=10, b=20)
details(a=10, b=20, c=30, x="Abc")
