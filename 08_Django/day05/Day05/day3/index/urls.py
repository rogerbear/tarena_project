from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_parent/$', parent_views),
    url(r'^02_child/$', child_views),
]

urlpatterns += [
    url(r'03_addauthor/$', addauthor_views),
    url(r'04_all/$', authorall_views),
    url(r'05_all/$', all_views),
    url(r'06_update/$', updateAuthor_views),
    url(r'07_delete/(\d+)/$', delete_views, name='delete'),
    url(r'08_upau/(\d+)/$', upau_views, name='update'),
    url(r'09_doF/$', doF_views),
    url(r'10_doQ/$', doQ_views),
]

urlpatterns += [
    url(r'^11_oto/$', oto_views),
]
