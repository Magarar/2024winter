# 循环
import copy

for x1 in range(5):
    for x2 in range(5):
        print(x1,end='\t')
    print()
print()
for x1 in range(1,10):
    for x2 in range(1, x1+1):
        print(x1, '*', x2, '=', x1*x2,end='\t')
    print('')

a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)
o1, o2 = zip(*zipped)
print(list(o1),list(o2))
print(list(zip(o1,o2)))
#异常处理
# try:
#     x = int(input("Please enter a number: "))
# except ValueError:
#     print("Oops!  That was no valid number.  Try again...")

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)

# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# def func():
#     raise ConnectionError
#
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc

# def f():
#     raise OSError('operation failed')

# excs = []
# for i in range(3):
#     try:
#         f()
#     except Exception as e:
#         e.add_note(f'Happened in Iteration {i+1}')
#         excs.append(e)
#
# raise ExceptionGroup('We have some problems', excs)
print("我是分割线")
a = [1,2,[3,4]]
b = copy.copy(a)
print(a)
print(b)
print("我是分割线")
b.append(5)
b[2].append(6)
print(a)
print(b)
print("我是分割线")
a.append(7)
print(a)
print(b)