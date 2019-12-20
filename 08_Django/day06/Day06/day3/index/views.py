from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F, Q

# Create your views here.


def parent_views(request):
    return render(request, '01_parent.html')


def child_views(request):
    return render(request, '02_child.html')

# 向　index_author　表中增加数据


def addauthor_views(request):
    # １．使用　Entry.objects.create()
    Author.objects.create(name='莫言',
                          age=65,
                          email='moyan@163.com')

    # 2.　使用实体对象　save() 完成增加
    au = Author(name='老舍',
                age=70,
                email='laoshe@163.com')
    au.save()

    # 3. 使用字典构建对象，并调用save()　完成增加
    dic = {
        'name': '郭敬明',
        'age': 85,
        'email': 'xiaosi@163.com',
    }

    au1 = Author(**dic)
    au1.save()

    return HttpResponse("Add OK")


# 查询　Author 实体中所有的数据
def authorall_views(request):
    # 1 . 通过　all() 查询所有的数据
    # authors = Author.objects.all()
    # for au in authors:
    #     print(au.name + ',', au.age, ',', au.email)

    # ２．通过　values()查询部分列的数据
    # authors = Author.objects.all().values('name', 'age')
    # for au in authors:
    #     print(au['name'] + ',', au['age'])

    # 3. 通过　order_by 实现排序查询
    # authors = Author.objects.order_by('-age')
    # for au in authors:
    #     print(au.name, ',', au.age, ',', au.email)

    # 4. 通过　exclude() 实现条件取反
    # authors = Author.objects.exclude(id=3, age=40)
    # for au in authors:
    #     print(au.name, ',', au.age, ',', au.email)

    # 5. 使用　filter()实现部分行查询
    # authors = Author.objects.filter(id=1)
    # for au in authors:
    #     print(au.name, ',', au.age, ',', au.email)

    # 6. 使用　查询谓词实现部分行查询
    # authors = Author.objects.filter(id__exact=1)

    # 7. 使用　__contains 查询　Author实体中　email 中包含　s 的信息
    # authors = Author.objects.filter(email__contains='s')

    # 8. 使用　get() 查询一条记录
    au = Author.objects.get(id__gt=1)
    print(au.name, ',', au.age, ',', au.email)

    # for au in authors:
    #     print(au.name, ',', au.age, ',', au.email)
    return HttpResponse('Query OK')


def all_views(request):
    # 1. 查询　Author　Models中所有的数据
    # authors = Author.objects.all().order_by('-age')

    # 1. 查询Author中所有　isActive 为　True 的人的信息
    authors = Author.objects.filter(isActive=True)
    # 2. 将查询结果作为变量传递到模板中03_authors.html
    return render(request, '03_authors.html', locals())


def updateAuthor_views(request):
    # 1. 获取id为１的用户信息
    # au = Author.objects.get(id__exact=1)
    # 2.　通过实体对象的属性修改值
    # au.name = '王宝强'
    # au.age = 35
    # au.email = 'wangbaoqiang@sina.com'
    # 3. 通过实体对象将信息保存回数据库
    # au.save()

    # 批量修改所有人的年龄为　７５
    Author.objects.all().update(age=75)
    return HttpResponse('Update OK')


def delete_views(request, id):
    # Author.objects.get(id=id).delete()

    # 通过修改对象的isActive属性值为False来模拟删除
    au = Author.objects.get(id=id)
    au.isActive = False
    au.save()

    # return HttpResponse('删除OK')
    # 使用转发跳转到　all_views()视图上
    # return all_views(request)

    # 使用重定向到　05_all 上
    return HttpResponseRedirect('/05_all/')


def upau_views(request, id):
    # 1. 根据ＩＤ查询author的信息
    au = Author.objects.get(id=id)
    # 2. 将查询出来的信息作为变量传递给04_au.html
    return render(request, '04_au.html', locals())


def doF_views(request):
    # 更新Author实体中所有人的年龄＋１０岁
    Author.objects.all().update(age=F('age') + 10)
    return HttpResponse('Update OK')


def doQ_views(request):
    # 通过　Q 查询　年纪>=85　或　id=1的人的信息
    authors = Author.objects.filter(Q(id=1) | Q(age__gte=85))
    return render(request, '03_authors.html', locals())


def oto_views(request):
    # 1.获取　id 为１　的Wife的信息
    # w = Wife.objects.get(id=1)
    # 2. 获取w对应的Author的信息
    # a = w.author

    # 1. 获取id为7的Author的信息
    a = Author.objects.get(id=7)
    # 2. 获取a对应的Wife的信息
    w = a.wife
    return render(request, '05_oto.html', locals())


def otm_views(request):
    # 1. 通过　Book 查询　对应的　Publisher
    book = Book.objects.get(id=1)
    publisher = book.publisher

    # 2. 通过　Publisher 查询对应的所有的　Book
    pub = Publisher.objects.get(id=2)
    books = pub.book_set.all()
    return render(request, '06_otm.html', locals())


def mtm_views(request):
    # 1.正向查询: 通过Author 查询　Book
    author = Author.objects.get(id=1)
    bookList = author.book.all()

    # 2.反向查询:通过　Book 查询　Author
    book = Book.objects.get(id=1)
    authorList = book.author_set.all()
    return render(request, '07_mtm.html', locals())


def aucount_views(request):
    # count = Author.objects.auCount()
    # return HttpResponse(count)

    # authors = Author.objects.lt_age(35)
    # for au in authors:
    #     print(au.name)

    count = Book.objects.title_count('钢铁')
    print('数量为:', count)
    return HttpResponse('执行OK')
