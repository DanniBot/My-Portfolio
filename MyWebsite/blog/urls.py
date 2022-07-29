from xml.etree.ElementInclude import include
from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.all_blogs,name='blogpage'),
    path('<int:blog_id>',views.detail,name='detail'),
]