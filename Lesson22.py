#
# 目标是：
# 1.内存读写
#     StringIO和BytesIO
#


from io import StringIO, BytesIO

# 很多时候，数据读写不一定是文件，也可以在内存中读写。
print("\n\nStringIO示例：")
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO('\nHello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# 如果要操作二进制数据，就需要使用BytesIO
print("\n\nBytesIO示例：")
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print(str(f.getvalue(), 'utf-8'))


f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
