#
# 目标是：
# 1.装饰器
# 2.

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改
# now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

import time


def log(func):
    def wrapper(*args, **kw):
        print('前置新增功能 ==. call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print(time.ctime())


now()


