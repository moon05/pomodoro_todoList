from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views



urlpatterns = [
	
	url(r'^$', views.Index.as_view(), name='Index'),
	url(r'^api/todo/$', views.ToDoItemList.as_view(), name='item-list'),
	url(r'^api/todo/(?P<pk>[0-9]+)$', views.ToDoItemDetail.as_view(), name='item-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)