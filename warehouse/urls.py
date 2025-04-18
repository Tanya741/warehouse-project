
from django.urls import path, re_path
from . import views




urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'^product/(?P<pk>[0-9a-fA-F]{24})$', views.product_detail, name='product_detail'),
    path('product/new/', views.product_new, name='product_new'),
    re_path(r'^product/(?P<pk>[0-9a-fA-F]{24})/edit/$', views.product_edit, name='product_edit'),
    re_path(r'^product/(?P<pk>[0-9a-fA-F]{24})/delete/$', views.product_delete, name='product_delete'),
    path('product/<str:name>/fetch/', views.product_fetch, name='product_fetch'),
    path('category/', views.product_category, name='product_category'),
    re_path(r'^category/(?P<pk>[0-9a-fA-F]{24})$', views.category_detail, name='category_detail'),
    path('category/new', views.category_new, name='category_new'),
    re_path(r'^category/(?P<pk>[0-9a-fA-F]{24})/edit/$', views.category_edit, name='category_edit'),
    re_path(r'^category/(?P<pk>[0-9a-fA-F]{24})/delete/$', views.category_delete, name='category_delete'),
    re_path(r'^category/(?P<pk>[0-9a-fA-F]{24})/fetch/$', views.category_fetch, name='category_fetch'),
    re_path(r'^category/(?P<pk>[0-9a-fA-F]{24})/(?P<cat>[\w\s]+)/new/', views.product_new_cat, name='product_new_cat'),

]