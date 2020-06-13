from django.conf.urls import url, re_path
from django.urls import path
from . import views

app_name = 'Info'


urlpatterns = [

 path(r'Analyze/', views.IndexView.as_view(), name='IndexView'),
 path(r'Mutation/<name>/', views.delta , name = 'delta'),
 path(r'details/<Mutation>/',views.detail,name='detail'),
 path(r'help/', views.hlp, name='hlp'),
 path(r'contacts/', views.contk, name='contk'),

]