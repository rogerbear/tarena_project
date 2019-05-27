import pymysql

db = pymysql.connect("localhost","root",\
    "123456","day03",charset="utf8",port=3306)
cursor = db.cursor()

sql_select = "select * from sheng;"
cursor.execute(sql_select)
# print(cursor.rowcount)

data = cursor.fetchone()
print("fetchone的结果为:")
print(data)
print()

data2 = cursor.fetchmany(3)
print("fetchmany的结果为:")
for i in data2:
    print(i)
print()

data3 = cursor.fetchall()
print("fetchall的结果为:")
for i in data3:
    print(i)
print()

db.commit()
cursor.close()
db.close()
