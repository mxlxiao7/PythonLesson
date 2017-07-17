#
# 目标是：
# 1.内置派生类
# 2.dir() 显示实例的所有方法
#

from model.NamedList import NamedList

johnny = NamedList("John Paul Jones")

# 打印实例类型
print(type(johnny))

# 打印方法
print(dir(johnny))

# 使用list类提供的一些功能补充数据
johnny.append("Bass Player")
johnny.extend(['Composer', 'Arranger', 'Musician'])

# 显示数据
print(johnny)

for attr in johnny:
    print(johnny.name + " is a " + attr + ".")
