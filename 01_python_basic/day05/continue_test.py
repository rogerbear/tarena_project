begin = int(input("num1:"))
end = int(input("num2:"))

# for i in range(begin, end):
#     if i % 2 == 0:
#         continue
#     print(i)

i = begin
while i < end:
    if i % 2 == 0:
        i += 1#如果不加这句，例如i=4时，就死循环了，下面两行的i+=1就不会执行
        continue
    print(i)
    i += 1
