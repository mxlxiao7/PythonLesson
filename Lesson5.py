#
# 目标是：
# 1.pickle操作数据， dump() 写入(默认是以二进制形式)  load()读区
# 2.str()
# 3.locals() 返回当前作用域中的变量集合


import pickle
import os

# 文件名称
file_name = "sketch.txt"

# 文件目录
path_dir = os.getcwd() + "/res/"

# 文件路径
path = path_dir + file_name

# 判断目标文件是否存在
os.chdir(path_dir)
if os.path.exists(file_name):

    man = []
    other = []
    target_path = ''
    content = ''

    # 文件数据
    with open(path, "r") as data:
        try:
            for line in data:
                if not line.find(":") == -1:
                    (line_num, content) = line.split(":", 1)
                    # 删除content中的空白字符
                    content = content.strip()
                    man.append(line_num)
                    other.append(content)
                else:
                    pass
        except ValueError:
            pass

        try:
            # 写文件
            target_path = path_dir + "L5_target.txt"

            # with语句利用了名为上下文管理协议的python技术
            with open(target_path, "wb") as target_out:
                pickle.dump(["要开始写数据了!\n\n", 1, "2", 'three'], target_out)
                pickle.dump(man, target_out)
                pickle.dump("\n\n", target_out)
                pickle.dump(content, target_out)
        except Exception as err:
            print("\n\n生成文件出错,错误信息：" + str(err))

    # 读取文件信息
    with open(target_path, "rb") as target_in:
        file_data = pickle.load(target_in)

    print(file_data)
else:
    print("目标文件不存在")
