l = [x for x in range(1, 100, 2)]
print(l)

l2 = [x for x in range(1, 21) if (x ** 2 + 1) % 5 == 0]
print(l2)

# 列表推导式多层嵌套
l3 = [x + y for x in 'ABC' for y in '123']
print(l3) #['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

