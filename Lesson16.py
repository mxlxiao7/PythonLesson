#
# 目标是：高阶函数
# 1.map/reduce
# 2.filter

from functools import reduce


# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。
def f(x):
    return x * x


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = list(map(f, l))
print(r)

# 把这个list所有数字转为字符串：
r = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(r)


# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce
# 把结果继续和序列的下一个元素做累积计算，其效果就是

# 一个序列求和，就可以用reduce实现：
def add(x, y):
    return x + y


r = reduce(add, [1, 3, 5, 7, 9])
print(r)


# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y


r = reduce(fn, [1, 3, 5, 7, 9])
print(r)


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


r = reduce(fn, map(char2num, '13579'))
print(r)

# 练习:
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
print("\n\n练习1：")


def normalize(name):
    name = name.lower()
    c = name[0].upper() + name[1:]
    return c


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是
# True还是False决定保留还是丢弃该元素。





# 例:在一个list中，删掉偶数，只保留奇数，可以这么写：
print("\n\n练习2：")


def is_odd(n):
    return n % 2 == 1


l = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l)

# 例:把一个序列中的空字符串删掉，可以这么写：
print("\n\n练习3：")


def not_empty(s):
    return s and s.strip()


l = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(l)

# 练习:回数是指从左向右读和从右向左读都是一样的数
print("\n\n练习4：")


def is_palindrome(n):
    n = str(n)
    left = 0
    right = len(n) - 1
    flag = True
    while left < right:
        if n[left] == n[right]:
            left += 1
            right -= 1
        else:
            flag = False
            break
    return flag


L1 = list(range(1, 1000))
L2 = list(filter(is_palindrome, L1))
print(L2)
