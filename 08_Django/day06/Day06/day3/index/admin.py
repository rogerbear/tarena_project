from django.contrib import admin
from .models import *

# 声明　Author的高级管理类


class AuthorAdmin(admin.ModelAdmin):
    # 1.指定在列表页中显示的字段们
    list_display = ('name', 'age', 'email')

    # 2.指定能够链接到详情页的字段们
    list_display_links = ('name', 'email')

    # 3.指定能够在列表页中修改的字段们
    list_editable = ['age']

    # 4. 指定允许被搜索的字段们
    search_fields = ['name', 'email']

    # 5.指定右侧过滤器中筛选的字段们
    list_filter = ('name', 'age', 'email')

    # 6. 指定在详情页中显示的字段　以及　顺序
    # fields = ('email', 'name')

    # 7. 指定在详情页面中字段的分组信息
    fieldsets = (
        (
            '基本信息', {
                'fields': ('name', 'age', 'book'),
            }
        ),
        (
            '高级信息', {
                'fields': ('email', 'isActive'),
                'classes': ('collapse',),
            }
        ),
    )


# 声明Book的高级管理类
class BookAdmin(admin.ModelAdmin):
    # 1. 指定时间选择器
    date_hierarchy = 'publicate_date'


# 声明Publisher的高级管理类
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')
    list_editable = ('address', 'city')
    # list_filter = ('address', 'city')
    fieldsets = (
        (
            '基本选项', {
                'fields': ('name', 'address', 'city'),
            }
        ),
        (
            '可选选项', {
                'fields': ('country', 'website'),
                'classes': ('collapse',)
            }
        )
    )


# 在此注册需要管理的Models
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Wife)
