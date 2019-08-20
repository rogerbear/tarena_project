import re

pattern = r'\w+'

obj = re.compile(pattern)

result = obj.findall('hello world')

print(result)

pattern2 = r'(ab)cd(ef)'
pattern3 = r'((ab)cd(ef))'

obj2 = re.compile(pattern2)
obj3 = re.compile(pattern3)

result2 = obj2.findall('abcdefgabcdefg')
result3 = obj3.findall('abcdefgabcdefg')

print(result2)
print(result3)

result4 = re.split(r'\s+','hello world china')
print(result4)


result5 = re.sub(r'[A-Z]','**','Hello,I am a Man.',count = 2)
print(result5)