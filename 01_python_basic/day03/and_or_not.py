#and  x and y  优先返回假值对象，当x的布尔值为False，返回x，否则返回y

0 and 0.0#返回0
100 and 200#返回200

#or x or y，优先返回真值对象
0 or 100#返回100
100 or 200 #返回100

#输出学生成绩
s = input("score:") or '0'#如果没有 (or '0') 时直接回车会报错，因为直接返回空字符串，即FALSE值，加上or语句代表带上真值，直接回车就会返回or后面的值
score = int(s)
print(score)

