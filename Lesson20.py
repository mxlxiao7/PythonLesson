#
# 目标是：
# 1.定制类：
#     __str__、__repr__
#     __iter__、__next__
#     __getitem__
#     __getattr__
#     __call__
#


class Student(object):
    def __init__(self, name):
        self.name = name

    # 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
    # 而__repr__(),返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    __repr__ = __str__


print("\n\n__str__、__repr__示例：")
print(Student('Michael'))


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    # 如果一个类想被用于for...in循环，类似list或tuple那样，就必须实现一个__iter__()方法
    def __iter__(self):
        return self

    # 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()
    # 方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    # Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
    # def __getitem__(self, n):
    #     a, b = 1, 1
    #     for x in range(n):
    #         a, b = b, a + b
    #     return a

    # 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


print("\n\n__iter__、__next__示例：")
for n in Fib():
    print(n, end=",")

print("\n\n__getitem__示例：")
f = Fib()
print(f[0], end=" ")
print(f[3])
print(f[0:5])


# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

    def __call__(self):
        print('My name is %s.' % self.name)


print("\n\n__getattr__示例：")
s = Student('Michael')
print(s.score)

print("\n\n__call__示例：")
s = Student('Michael')
print(s())  # self参数不要传入

# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print(callable(Student('Michael')))  # True
print(callable(max))  # True
print(callable([1, 2, 3]))  # False
print(callable(None))  # False
print(callable('str'))  # False
