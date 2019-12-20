from django.db import models

# Create your models here.

# 1. Users - 用户表


class Users(models.Model):
    uphone = models.CharField(max_length=20, verbose_name='电话号码')
    upwd = models.CharField(max_length=20, verbose_name='密码')
    uemail = models.EmailField(verbose_name='电子邮件')
    uname = models.CharField(max_length=50, verbose_name='用户名')
    isActive = models.BooleanField(default=True, verbose_name='是否激活')

    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

# 2.GoodsType - 商品类型表


class GoodsType(models.Model):
    title = models.CharField(max_length=30, verbose_name='类型标题')
    desc = models.TextField(verbose_name='描述')
    picture = models.ImageField(
        upload_to='static/upload/goodstype', verbose_name='图片')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goodstype'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name


# 3.Goods - 商品表
class Goods(models.Model):
    title = models.CharField(max_length=100, verbose_name='商品名称')
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='商品价格')
    spec = models.CharField(max_length=30, verbose_name='商品规格')
    picture = models.ImageField(
        upload_to='static/upload/goods', verbose_name='商品图片')
    isActive = models.BooleanField(default=True, verbose_name='是否上架')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
