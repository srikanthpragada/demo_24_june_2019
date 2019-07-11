class Time:

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @property
    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    @totalseconds.setter
    def totalseconds(self, value):
        self.h = value // 3600
        value = value % 3600
        self.m = value // 60
        value = value % 60
        self.s = value

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"


t1 = Time(10, 20, 30)
t2 = Time(s=60)
print(t1)
print(t1.totalseconds)

t2.totalseconds = 10000
print(t2)
print(t2.totalseconds)
