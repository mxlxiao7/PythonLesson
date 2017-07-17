#
# 目标是：
# 1.在其他文件定义方法，并调用
# 2.推导表
# 3.列表分片
# 4.集合,通过set()方法
import os


# 文件目录
from utils import CommonUtils

file_dir = os.getcwd() + "/res/Lesson6/"

# 文件名称
path0 = file_dir + "L6_james.txt"
path1 = file_dir + "L6_julie.txt"
path2 = file_dir + "L6_mikey.txt"
path3 = file_dir + "L6_sarah.txt"

# 读取数据
james = CommonUtils.load_data(path0).strip().split(',')
julie = CommonUtils.load_data(path1).strip().split(',')
mikey = CommonUtils.load_data(path2).strip().split(',')
sarah = CommonUtils.load_data(path3).strip().split(',')

print(sorted(CommonUtils.deal_data(james)))
print(sorted(CommonUtils.deal_data(julie)))
print(sorted(CommonUtils.deal_data(mikey)))
print(sorted(CommonUtils.deal_data(sarah)))

# 推到表方式转换数据
print("\n\n列表推导:")
clean_james = sorted([CommonUtils.sanitize(item) for item in james])
print(clean_james)

# 排除重复，并取最大的三个数据
james_1 = sorted([CommonUtils.sanitize(item) for item in james])
unique_james = []
for item in james_1:
    if item not in unique_james:
        unique_james.append(item)

print("\n\n排除重复，并取最大的三个数据:")
print(unique_james[0:3])


#使用集合方式
james = CommonUtils.deal_data(james)
print("\n\n集合方式:")
print(sorted(set(james))[0:3])
