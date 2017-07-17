#
# 目标是：
#    1.文件数据读取
#    2.if条件语句
#    3.异常判断
#


import os

# 文件名称
file_name = "sketch.txt"

# 文件目录
dir = os.getcwd() + "/res/"

# 文件路径
path = dir + file_name

# 打印文件地址
print("path " + path)

# 判断目标文件是否存在
os.chdir(dir)
if os.path.exists(file_name):

    # 文件数据
    data = open(path)

    # 打印文件第一行内容
    print(data.readline(), end='')

    # 退回到文件起始位置
    data.seek(0)

    print("------------------------------------------------\n", end='')
    print("----------------打印文件内容开始------------------\n", end='')
    print("------------------------------------------------\n", end='')

    try:
        for line in data:
            if not line.find(":") == -1:
                (line_num, content) = line.split(":", 1)
                print(line_num, end='')
                print(" #### ", end='')
                print(content, end='')
            else:
                print(line, end='')
    except ValueError:
        pass

    print("------------------------------------------------\n", end='')
    print("----------------打印文件内容结束------------------\n", end='')
    print("------------------------------------------------\n", end='')

    # 关闭文件资源
    data.close()

else:
    print("目标文件不存在")
