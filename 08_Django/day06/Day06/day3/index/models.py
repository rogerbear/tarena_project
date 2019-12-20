from django.db import models

# 声明自定义的objects - models.Manager


class AuthorManager(models.Manager):
    # 添加自定义函数　－　查询Author表中共有多少条数据
    def auCount(self):
        return self.all().count()

    # 添加自定义函数　－　查询年纪小于指定年纪的作者的信息
    def lt_age(self, age):
        return self.filter(age__lt=age)

# 声明自定义的objects - models.Manager - Book


class BookManager(models.Manager):
    # 查询书名中包含指定关键词的数量
    def title_count(self, keywords):
        return self.filter(title__contains=keywords).count()

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='名称')
    address = models.CharField(max_length=50, verbose_name='地址')
    city = models.CharField(max_length=20, verbose_name='城市')
    country = models.CharField(max_length=20, verbose_name='国家')
    website = models.URLField(verbose_name='网址')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name


class Book(models.Model):
    # 使用　BookManager　覆盖　objects
    objects = BookManager()
    title = models.CharField(max_length=50, verbose_name='名称')
    publicate_date = models.DateField(verbose_name='出版日期')
    # 增加对　Publisher　的引用
    publisher = models.ForeignKey(Publisher, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ["-publicate_date"]


class Author(models.Model):
    # 使用AuthorManager 覆盖　objects
    objects = AuthorManager()
    name = models.CharField(max_length=30, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True, verbose_name='电子邮箱')
    isActive = models.BooleanField(default=True, verbose_name='激活')
    # 增加对　Book的引用，体现多对多的关系
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

    # 定义内部类　Meta 改变其在admin中的表现形式
    class Meta:
        # 指定对应的表的名字(要同步数据库)
        db_table = 'author'
        # 指定该类在后台显示的名称(单数)
        verbose_name = '作者'
        # 指定该类在后台显示的名称(复数)
        verbose_name_plural = verbose_name
        # 指定排序
        ordering = ["-age", "name"]


class Wife(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    # 增加一对一的映射，引用自Author实体
    author = models.OneToOneField(Author, verbose_name='官人')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
        verbose_name = '夫人'
        verbose_name_plural = verbose_name
