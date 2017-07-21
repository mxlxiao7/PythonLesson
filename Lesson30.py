#!/usr/bin/python3

#
# 目标是：
# 1.协程:Python对协程的支持是通过generator实现的。


# 注意到consumer函数是一个generator，把一个consumer传入produce后：
#     1.首先调用c.send(None)启动生成器；
#     2.然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#     3.consumer通过yield拿到消息，处理，又通过yield把结果传回；
#     4.produce拿到consumer处理的结果，继续生产下一条消息；
#     5.produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

def consumer():
    r = ''
    while True:
        n = yield r
        # 上面就相当于
        # n = yield 这里yield 就是用来接收参数的
        # yield r 这里用来记录并且返回r的
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
