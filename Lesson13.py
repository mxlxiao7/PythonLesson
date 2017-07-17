#
# 目标是：
# 1.多线程
#   内核线程：由操作系统内核创建和撤销。
#   用户线程：不需要内核支持而在用户程序中实现的线程
# 2.Python3 线程中常用的两个模块为：
#   _thread
#   threading(推荐使用)
# 3.线程优先级队列（ Queue）
#   Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
#


# 数式：调用 _thread 模块中的start_new_thread()函数来产生新线程。语法如下:
# _thread.start_new_thread ( function, args[, kwargs] )
# 参数说明:
#   function - 线程函数。
#   args - 传递给线程函数的参数,他必须是个tuple类型。
#   kwargs - 可选参数。

import _thread
import time
import threading
import queue

# 线程
threads = []

"""
方式一：
"""


def print_time0(thread_name, delay, counter):
    print("开始线程：" + thread_name)
    while counter:
        time.sleep(delay)
        print("%s : %s" % (thread_name, time.ctime(time.time())))
        counter -= 1
    print("退出线程：" + thread_name)


# 创建两个线程
try:
    thread0 = _thread.start_new_thread(print_time0, ("Thread-0", 2, 5))
    thread1 = _thread.start_new_thread(print_time0, ("Thread-1", 4, 5))

    threads.append(thread0)
    threads.append(thread1)
except:
    print("Error: 无法启动线程")

"""
方式二：
"""


class Thread0(threading.Thread):
    def __init__(self, thread_id, name, delay, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time1(self.name, self.delay, self.counter)
        print("退出线程：" + self.name)


def print_time1(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread2 = Thread0(2, "Thread-2", 2, 5)
thread3 = Thread0(3, "Thread-3", 3, 5)

# 开启新线程
thread2.start()
thread3.start()

threads.append(thread2)
threads.append(thread3)

"""
同步：
"""


class Thread1(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程：" + self.name)
        # 获取锁，用于线程同步
        thread_lock.acquire()
        print_time2(self.name, self.counter, 5)
        # 释放锁，开启下一个线程
        thread_lock.release()
        print("退出线程：" + self.name)


def print_time2(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 加锁工具
thread_lock = threading.Lock()
# 创建新线程
thread4 = Thread1(4, "Thread-4", 4)
thread5 = Thread1(5, "Thread-5", 5)

# 开启新线程
thread4.start()
thread5.start()

threads.append(thread4)
threads.append(thread5)

"""
线程优先级队列（ Queue）：
这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。
Queue
模块中的常用方法:
Queue.qsize()                   返回队列的大小
Queue.empty()                   如果队列为空，返回True, 反之False
Queue.full()                    如果队列满了，返回True, 反之False
Queue.full                      与 maxsize 大小对应
Queue.get([block[, timeout]])   获取队列，timeout等待时间
Queue.get_nowait()              相当Queue.get(False)
Queue.put(item)                 写入队列，timeout等待时间
Queue.put_nowait(item)          相当Queue.put(item, False)
Queue.task_done()               在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join()                    实际上意味着等到队列为空，再执行别的操作
"""


class Thread2(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(thread_name, q):
    while not exitFlag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release
            print("%s processing %s" % (thread_name, data))
        else:
            queue_lock.release()
        time.sleep(1)


exitFlag = 0
thread_list = ["Thread-6", "Thread-7", "Thread-8"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threadID = 6

# 创建新线程
for tName in thread_list:
    thread = Thread2(threadID, tName, work_queue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queue_lock.acquire()
for word in nameList:
    work_queue.put(word)
queue_lock.release()

# 等待队列清空
while not work_queue.empty():
    print("----------------- 线程队列不为空 -----------------")
    time.sleep(1)
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
print([type(t) for t in threads])
for t in threads:
    try:
        t.join()
    except AttributeError:
        pass
print("----------------- 退出主线程 -----------------")
