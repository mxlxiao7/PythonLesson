#!/usr/bin/python3

#
# 目标是：
# 1.WSGI接口
#   了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：
#     浏览器发送一个HTTP请求；
#     服务器收到请求，生成一个HTML文档；
#     服务器把HTML文档作为HTTP响应的Body发送给浏览器；
#     浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。


# http://localhost:8000/michael

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
