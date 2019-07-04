
def math_op(fun,a,b):
    print( fun(a,b))


def add(n1,n2):
    return n1 + n2


math_op(add,10,20)
math_op( lambda x,y: x * y,10,20)



