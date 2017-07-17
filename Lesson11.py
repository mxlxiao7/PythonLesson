#
# 目标是：
# 1.键盘输入
# 2.写文件
#
import os
import pickle

# 存储路径
path = os.getcwd() + "/res/L11_info.txt"

input_str = input('请输入信息：')

try:
    with open(path, "wb+") as file:
        pickle.dump(input_str, file)
except Exception as err:
    print("\n\n生成文件出错,错误信息：\n\t" + str(err))

#显示读取内容
try:
    with open(path, "rb+") as file:
        info = pickle.load(file)
        print("\n输入内容：\n\t" + str(info))
except Exception as err:
    print("\n\n读取文件出错,错误信息：\n\t" + str(err))