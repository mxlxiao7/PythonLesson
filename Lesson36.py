#!/usr/bin/python3

#
# 目标是：
# 1.MySql
# 导入MySQL驱动:


# 注意把password设为你的root口令:
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='license',
    db='leon_2017',
    charset='utf8'
)

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount

# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values

# 关闭Cursor和Connection:
cursor.close()
conn.close()
