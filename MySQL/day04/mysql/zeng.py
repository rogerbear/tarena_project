import pymysql

#1.创建数据库连接
db = pymysql.connect("localhost","root",\
                     "123456",charset="utf8")
#2.利用connect对象创建一个游标对象
cursor = db.cursor()

#3.利用游标对象的方法操作MySQL数据库
cursor.execute("use day03;")
cursor.execute("insert into sheng values \
                (NULL,240000,'四川省');")
#4.提交到数据库执行
db.commit()
#5.关闭游标对象
cursor.close()
#6.关闭数据库连接
db.close()












