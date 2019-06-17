import pymysql

#创建数据库连接
db = pymysql.connect("localhost",'root','roger0809',charset='utf8')

#创建游标对象
cursor = db.cursor()

#操作数据库
cursor.execute('use MOSHOU;')
# cursor.execute("insert into sheng values(11,'240000','四川省')")
cursor.execute('select * from sheng;')
print(cursor.rowcount)
# data = cursor.fetchmany(3)
data = cursor.fetchall()
for i in data:
    print(i)
# data = cursor.fetchone()
print(data)

#提交执行
db.commit()

#关闭游标
cursor.close()

#关闭数据库
db.close()