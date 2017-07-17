#
# 目标是：
# 1.在其他文件定义方法，并调用
# 2.推导表
# 3.列表分片
# 4.集合,通过set()方法
import os

from utils import CommonUtils

print("\n")

# 文件目录
file_dir = os.getcwd() + "/res/"

# 文件名称
file_name = "L7_sarah2.txt"

content = CommonUtils.load_res_file(file_dir, file_name)
print(content)
