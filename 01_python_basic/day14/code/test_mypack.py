# test_mypack.py

# 以下语法会将 mypack/__init__.py内
# __all__列表里指定的'games' 和'menu' 一同导入
from mypack import *
# import mypack # __all__列表只在from xxx import *语句时起作用
