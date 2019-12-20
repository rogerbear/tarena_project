from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ['uname', 'uphone', 'uemail']
    list_display_links = ['uname', 'uphone', 'uemail']
    search_fields = ['uname', 'uphone', 'uemail']
    fields = ['uphone', 'uemail', 'uname', 'isActive']


# Register your models here.
admin.site.register(Users, UsersAdmin)
admin.site.register(GoodsType)
admin.site.register(Goods)
