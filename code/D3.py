# 数据类型
print("数据类型")
print(float('inf'))     # 无穷大

# 时间
import time
b = time.time()
print("\n时间")
print(b)
print(b//(24*3600))
del b

# 运算
print("\n逻辑运算")
print(True and False)  # &&
print(True or False)  # ||
print(not False)  # !

print("\n拼接")
# 加法拼接
print("str" + "哈基米")
print([10, 20] + [300])
# 乘法
print("哈基米"*3)  # 字符串复制
print([10]*3)  # 元组复制
# 同一运算符
print("\n同一运算符")
print("20 is 20 is",20 is 20)
a = b = 20
print("a is b is", a is b)
a = b = 258
print(a is b) # 文件模式下返回true
# 成员运算符
print("\n成员运算符")
print(10 in [10,20,30])
del a,b
# 字符串
print("\n多行字符串")
s = '''see
you
again'''
print(s)
# print("\n输入")
# myname = input("哈基米:")
# print(myname)
print("\n字符串替换")
a = ("闪电旋风劈")
a = a.replace('劈', '批')
print("a is "+a)
print(a[0])
# 切片
print("\n字符串切片")
print("abcdefg"[:4])
print("\n字符串分割")
a = "to be or not to be"
a = a.split()
print(a)
# 合并
print("\n字符串合并")
a = ' '.join(a)
print(a)
del a
# 格式化
print("\n字符串格式化")
a = "{0}打断别人的{1}啊"
a = a.format('Q','E')
print(a)
a = "{str},为什么不{str}"
print(a.format(str='Q'))
# 填充与对齐
print("\n字符串填充")
print("{str}哥就是{str}{a:!^8}".format(str='龙',a='test'))
# 可变字符串
print("\n可变字符串")
import io
sio = io.StringIO('爆爆爆爆爆')
print(sio.getvalue())
sio.seek(1) # 索引
sio.write("啵啵啵") # 替换
print(sio.getvalue())

# 序列
print("\n序列")
a = [10,20,30]
b = a.pop() #删除
print(a)

# 字典
print('\n字典')
k = ['name', 'age','class']
v = ['哈基米','10','5']
d = dict(zip(k,v))
print(d)
a,b = d
print(a)

# 集合
