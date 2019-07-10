class Product:
    # class attributes
    taxrate = 18

    # Static method or class method
    @staticmethod
    def set_taxrate(newtaxrate):
        Product.taxrate = newtaxrate

    # Constructor
    def __init__(self, name, price=0):
        # object attributes
        self.name = name
        self.price = price

    # Method
    def print_details(self):
        """
        Prints details of object
        :return: None
        """
        print("Name  : ", self.name)
        print("Price : ", self.price)

    def get_price(self):
        return self.price + self.price * Product.taxrate / 100

    # Special methods
    def __eq__(self, other):
        print("__eq__")
        return self.name == other.name and self.price == other.price

    def __str__(self):
        return f"{self.name} - {self.price}"


if __name__ == '__main__':  # run code only when module is run as script

    print(Product.set_taxrate(30))

    p1 = Product("One Plus 7", 35000)
    print(p1.get_price())

    # p2 = Product("One Plus 7", 35000)
    # print(p1 == p2)  # p1.__eq__(p2)
    # print(p1)  # str(p1) ->  p1.__str__
