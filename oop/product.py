class Product:

    # Constructor
    def __init__(self, name, price=0):
        # object attributes
        self.name = name
        self.price = price

    # Method
    def print_details(self):
        print("Name  : ", self.name)
        print("Price : ", self.price)


p1 = Product("One Plus 7", 35000)
p2 = Product("One Plus 7", 35000)
print(p1 == p2)


l = [10,20]
l2  = [10,20]
print( l == l2)









