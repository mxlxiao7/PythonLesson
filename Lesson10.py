#
# 目标是：
# 1.生成器 yield函数
# 2.菲波那切数列
#

import sys


def fibonacci(n):
    a = 0
    b = 1
    counter = 0

    while True:
        if counter > n:
            return

        yield a
        a, b = b, a + b
        counter += 1


# f是一个迭代器，由生成器返回生成
f = fibonacci(10)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration as ste:
        sys.exit()
