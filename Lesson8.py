#
# 目标是：
# 1.字典使用 cleese = {}  cleese = dict()
# 2.类的创建
# 3.
# 4.

from utils import CommonUtils

print("\n")

# 文件名称
file_name = "L7_sarah2.txt"

# 创建实例对象
sarah = CommonUtils.load_coach_data(file_name)
print(type(sarah))

# 打印数据
print(sarah.top3())

sarah.add_time('2.11')
# 打印数据
print(sarah.top3())

sarah.add_times(['2.10'])
# 打印数据
print(sarah.top3())
