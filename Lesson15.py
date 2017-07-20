#
# 目标是：
# 1.生成器:
#   通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100
#   万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白
#   白浪费了。所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#   这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。


# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
print("\n列表推导式：")
L = [x * x for x in range(10)]
print(type(L))
print(L)

print("\n生成器：")
g = (x * x for x in range(10))
print(type(g))
for n in g:
    print(n, end=', ')

print("\n\n函数实现：")


# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib0(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end=', ')
        a, b = b, a + b  ##
        n += 1
    return 'done'


fib0(10)

# 注意，赋值语句：a, b = b, a + b
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]

print("\n\n函数generator实现：")


# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


for i in fib1(10):
    print(i, end=', ')


# 练习:杨辉三角定义如下
#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1




