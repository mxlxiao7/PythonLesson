#
# 目标是：
# 1.操作目录
# 2.shutil模块提供了copyfile()的函数
#

import os
import time
import threading

# 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数
print("\n\n操作系统：")
print("\t" + os.name)  # 操作系统类型

print("\n\n操作系统详细信息：")
print("\t" + str(os.uname()))  # 操作系统类型

print("\n\n环境变量：")
print("\t" + str(os.environ))

# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print("\t" + os.environ.get('PATH'))

print("\n\n操作文件和目录：")
# 查看当前目录的绝对路径:
print("\t" + os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符.
path = os.path.join(os.path.abspath('.'), 'testdir')

# 然后创建一个目录:
try:
    os.mkdir(path)
    print("\t创建目录testdir")
except Exception as err:
    print("创建目录testdir失败 ：" + str(err))
    pass


def del_dir(path, delay):
    print("\t" + str(delay) + "秒后删除目录testdir")
    time.sleep(delay)
    # 删掉一个目录:
    os.rmdir(path)
    print("\t删除目录testdir")


class DelThread(threading.Thread):
    def __init__(self, thread_id, path, delay):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.path = path
        self.delay = delay

    def run(self):
        print("开始线程：" + self.thread_id)
        del_dir(self.path, self.delay)


t = DelThread("删除线程", path, 2)
t.start()
t.join()
print("----------------- 退出主线程 -----------------")

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
(dirt, file) = os.path.split(os.getcwd())
print("dir = " + dirt)
print("file" + file)

# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
print("\n\n创建文件并重命名：")
file_name = "test.txt"
new_file_name = "test.py"
file_path = os.path.join(os.getcwd(), file_name)
new_file_path = os.path.join(os.getcwd(), new_file_name)
print("创建文件: " + file_name)
try:
    with open(file_path, "w") as data:
        pass
except Exception as err:
    print("创建文件" + file_name + "失败 ：" + str(err))

print("重命名文件: " + file_name + " ==>" + new_file_name)
os.rename(file_path, new_file_path)
print("删除文件: " + new_file_name)
os.remove(new_file_path)

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print("\n\n过滤文件：")
l = [x for x in os.listdir('.') if os.path.isdir(x)]
print("\t" + str(l))

# 要列出所有的.py文件
print("\n\n.py文件：")
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print("\t" + str(l))
