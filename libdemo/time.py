import json

class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"


t1 = Time(10, 20, 30)
json_str = json.dumps(t1.__dict__)
print("Json str : ", json_str)
py_object = json.loads(json_str)
print("Python Object : ", py_object)
