l = [{'name': 'aaa', 'age': 18, 'score': 88},
     {'name': 'bbb', 'age': 4, 'score': 77},
     {'name': 'ccc', 'age': 5, 'score': 99}]

d = {'name': 'aaa', 'age': 18, 'score': 88}

def age_sort(l):
    return l['age']


# print(age_sort(l))
# l.sort(key=lambda k: k['age'], reverse=True)
l.sort(key=age_sort, reverse=True)
print(l)


for i in l:
    if 'aaa' == i['name']:
        print(i)

