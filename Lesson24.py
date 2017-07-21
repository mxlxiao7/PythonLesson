#
# 目标是：进程和线程
# 1.多进程
#     如果你打算编写多进程的服务程序，Unix / Linux无疑是正确的选择。由于Windows没有fork调用，难道在
#     Windows上无法用Python编写多进程的程序？由于Python是跨平台的，自然也应该提供一个跨平台的多进程
#     支持。multiprocessing模块就是跨平台版本的多进程模块。multiprocessing模块提供了一个Process
#     类来代表一个进程对象
# 2.进程间通信是通过Queue、Pipes等实现的。
# 3.多线程
#   多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
#   Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
#


import os, time, random, subprocess, threading
from multiprocessing import Process, Pool, Queue

print("\n\n创建子进程：\n")


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


# 主进程要执行的代码
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())

    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('Child process end.')

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
print("\n\n批量创建子进程：\n")


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.close()
    p.join()
    print('All subprocesses done.')

# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
print("\n\n子进程：\n")
# 如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print("\n\n子进程-communicate()：\n")
# 如果子进程还需要输入，则可以通过communicate()方法输入：
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
print("\n\n进程间通信：\n")


# 写数据进程执行的代码:
def write(que):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        que.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(que):
    print('Process to read: %s' % os.getpid())
    while True:
        value = que.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    que = Queue()
    pw = Process(target=write, args=(que,))
    pr = Process(target=read, args=(que,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

print("\n\n---------------------------------------------------")
print("----------------------- 线程 ----------------------")
print("---------------------------------------------------\n")


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0.5)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

print("\n\n---------------------------------------------------")
print("----------------------- 同步 ----------------------")
print("---------------------------------------------------\n")
# 假定这是你的银行存款:
balance = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

balance = 0
lock = threading.Lock()


def run_thread1(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


t1 = threading.Thread(target=run_thread1, args=(5,))
t2 = threading.Thread(target=run_thread1, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
