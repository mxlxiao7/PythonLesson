#
# 目标是：
#    1.文件数据写操作
#    2.str(err)
#
#


import os

# 文件名称
file_name = "sketch.txt"

# 文件目录
dir = os.getcwd() + "/res/"

# 文件路径
path = dir + file_name

# 判断目标文件是否存在
os.chdir(dir)
if os.path.exists(file_name):
    # 文件数据
    data = open(path)

    man = []
    other = []
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

    print(man, end='')
    print("\n\n", end='')
    print(other, end='')

    # 关闭文件资源
    data.close()

    try:
        # 写文件
        target_path = dir + "L3_target.txt"
        target_out = open(target_path, "w")
        print("要开始写数据了!\n\n", file=target_out)
        print(man, file=target_out)
        print("\n\n", file=target_out)
        print(content, file=target_out)
        target_out.flush()

    except Exception as err:
        print("\n\n生成文件出错,错误信息：" + str(err))

    finally:
        if "target_out" in locals() and not target_out.closed:
            target_out.close()
            print("\n\n关闭文件 ==> target_out.txt")

else:
    print("目标文件不存在")
