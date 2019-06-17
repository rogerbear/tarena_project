import pymysql

db = pymysql.connect("localhost","root",\
    "roger0809","MOSHOU",charset="utf8",port=3306)
cursor = db.cursor()

try:
    cursor.execute("update CCB set money=95000 \
                    where name='转钱';")
    cursor.execute("update ICBC set money=5000 \
                    where name='借钱';")
    db.commit()
    print("ok")
except Exception as e:
    db.rollback()
    print("Failed")
    print(e)

cursor.close()
db.close()