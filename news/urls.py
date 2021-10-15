from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.post, name='news'),
    url(r'^(?P<slug>[\w-]+)/$', views.Post_detail, name='post_detail'),
    path('search/', views.search, name='search')


]

