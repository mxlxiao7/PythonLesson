#
# 目标是：
# 1.使用@property
# 2.把方法定义为属性
# 3.定义一个只读属性
#

# score 数值只能是0-100 ，防止设置数值越界，所以做如下处理

class Student(object):
    def get_score(self):
        return self.score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.score = value


try:
    s = Student()
    s.set_score(60)  # ok!
    s.get_score()
    s.set_score(9999)
except ValueError as err:
    print(str(err))


# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，
# 这是必须要做到的！还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


try:
    s = Student()
    s.score = 60  # OK，实际转化为s.set_score(60)
    print(s.score)  # OK，实际转化为s.get_score()
    s.score = 9999
except ValueError as err:
    print(str(err))


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
# age就是一个只读属性
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


try:
    s = Student()
    s.birth = 1988
    print("birth = " + str(s.birth) + " age = " + str(s.age))
    s.age = 25
except AttributeError as err:
    print(str(err))
