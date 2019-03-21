from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^users/',views.view_usr,name='view_usr'),
	url(r'^transactions/',views.view_trans,name='transactions'),
	url(r'^transfer/',views.transfer,name='transfer'),
	url(r'^transfer_to/',views.transfer_to,name='transfer_to'),
	url(r'^detail/',views.detail,name='detail'),
	url(r'^detail1/',views.detail1,name='detail1'),

]