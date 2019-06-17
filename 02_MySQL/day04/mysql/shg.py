import pymysql
#1.创建数据库连接
db = pymysql.connect("localhost","root",\
                     "123456","day03",charset="utf8")
#2.利用connect对象创建一个游标对象
cursor = db.cursor()

#3.利用游标对象的方法操作MySQL数据库
cursor.execute("update sheng set s_id=266666\
 where s_name='四川省';")
cursor.execute("delete from sheng where\
 s_name='河北省';")

#4.提交到数据库执行
db.commit()
#5.关闭游标对象
cursor.close()
#6.关闭数据库连接
db.close() 