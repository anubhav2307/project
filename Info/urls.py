from django.conf.urls import url, re_path
from django.urls import path
from . import views

app_name = 'Info'


urlpatterns = [

 path(r'Analyze/', views.Index, name='Index'),
 path(r'Mutation/<name>/', views.delta , name = 'delta'),
 path(r'details/<Mutation>/',views.detail,name='detail'),
 path(r'help/', views.hlp, name='hlp'),
 path(r'contacts/', views.contk, name='contk'),
 path('file/<id>',views.sheet,name='sheet'),
 path('download/',views.downl,name='downl'),
 path('upload/',views.upload,name='upload'),
 path('see_uploads/',views.see_uploads,name='see_uploads'),
 path('upload_file/<id>',views.upload_file,name="upload_file")

]