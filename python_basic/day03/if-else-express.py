#满100减20，if-else条件表达式

money = int(input("enter a price:"))

pay = money - 20 if money >= 100 else money

print("must pay:",pay)