class Marks_Itertor:
    def __init__(self,marks):
        self.pos = 0
        self.marks = marks

    def __next__(self):
        if self.pos == len(self.marks):
            raise StopIteration
        else:
            self.pos += 1
            return self.marks[self.pos - 1]


class Marks:
    def __init__(self):
        self.marks = [20, 30, 40, 25, 66]

    def __iter__(self):
        return Marks_Itertor(self.marks)




m = Marks()
mi1 = iter(m)
mi2 = iter(m)

print(mi1.__next__())   # 20
print(mi1.__next__())   # 30

print(mi2.__next__())   # 20