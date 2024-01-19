# #类
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#     def ADD(self):
#         print(self.r+self.i)
# x = Complex(3.0, -5)
# x.ADD()   # 输出结果：3.0 -4.5


# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)


# t = Test()
# t.prt()

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __str__(self):
    #     return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        print(self.a + other.a, self.b + other.b)
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
v1 + v2

