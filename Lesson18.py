#
# 目标是：
# 1.动态绑定属性，方法,
# 2.使用__slots__ , __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
#
from types import MethodType


class Student(object):
    pass


# 给实例绑定一个属性：
s = Student();
s.name = 'Michael'
print(s.name)


# 给实例绑定一个方法：
def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(23)
print(s.age)


# 给一个实例绑定的方法，对另一个实例是不起作用的,为了给所有实例都绑定方法，可以给class绑定方法：
# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中
# 动态给class加上功能，这在静态语言中很难实现
def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)


# 如果我们想要限制实例的属性怎么办？比如，只允许对Person实例添加name和age属性。
class Person(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


try:
    p = Person()
    p.name = 'Michael'  # 绑定属性'name'
    p.age = 25  # 绑定属性'age'
    p.score = 99  # 绑定属性'score'
except AttributeError as err:
    print("限制动态绑定 ： " + str(err))


