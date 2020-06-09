from django.conf.urls import url, re_path
from django.urls import path
from . import views

app_name = 'Info'


urlpatterns = [

path(r'Analyze/', views.IndexView.as_view(), name='IndexView'),
re_path(r'^Mutation/(?P<name>[\w-]+)/$', views.delta , name = 'delta'),
re_path(r'^details/(?P<Mutation>[\w-]+)/$',views.detail,name='detail'),
path(r'help/', views.hlp, name='hlp'),
path(r'contacts/', views.contk, name='contk'),

]