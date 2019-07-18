#将文件以二级制方式存储
from pymongo import MongoClient 
import bson.binary 

conn = MongoClient('localhost',27017)

#数据库不存在则自动创建
db = conn.savefile
my_set = db.image 

# file = 'file.png'

# #存储　
# f = open(file,'rb')
# #讲读取的二进制字节流，变为bson格式的二进制子串
# dic = dict(content = bson.binary.Binary(f.read()),\
#     filename = 'img.png')
# '''
# {'content':bson.binary.Binary(f.read()),
#  'filename':'img.png'}
# '''
# #插入文档
# my_set.save(dic) 

# 提取文件

#获取到存储文件的文档字典
data = my_set.find_one({'filename':'img.png'})

with open('img.png','wb') as f:
    f.write(data['content'])

conn.close()


