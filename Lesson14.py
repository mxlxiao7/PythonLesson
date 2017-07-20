#
# 目标是：
# 1.迭代
# 2.列表生成式


from collections import Iterable

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关
# 心该对象究竟是list还是其他数据类型。那么，如何判断一个对象是可迭代对象呢？方法是通过
# collections模块的Iterable类型判断：

print("\nIterable类型判断：")
# str是否可迭代 True
print(isinstance('abc', Iterable))
# list是否可迭代 True
print(isinstance([1, 2, 3], Iterable))
# 整数是否可迭代 False
print(isinstance(123, Iterable))

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一
# 个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
print("\nenumerate函数：")
for i, value in enumerate(['A', 'B', 'B']):
    print(i, value)

print("\n同时引用两个变量：")
# 同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

print("\n列表生成式：")
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
data = list(range(0, 10))
print(data)

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
data = [x * x for x in list(range(0, 10))]
print(data)

# 还可以使用两层循环，可以生成全排列：
data = [m + n for m in 'ABC' for n in 'XYZ']
print(data)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
data = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in data.items():
    print(k, '=', v)

L = {'x': 'A', 'y': 'B', 'z': 'C'}
data = [k + '=' + v for k, v in L.items()]
print(data)

# 最后把一个list中所有的字符串变成小写,如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L = ['Hello', 'World', 18, 'Apple', None]
data = []
for s in L:
    if isinstance(s, str):
        data.append(s.lower())
    else:
        pass
print(data)
