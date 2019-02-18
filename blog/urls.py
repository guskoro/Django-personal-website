from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
   path('', views.index, name="blog"),
   re_path(r'^category/(?P<categoryInput>[\w-]+)/$',views.categoryPost, name="category"),
   re_path(r'^post/(?P<slugInput>[\w-]+)/$',views.detailPost, name="detail"),
   ]