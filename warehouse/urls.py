
from django.urls import path, re_path
from . import views




urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'^product/(?P<pk>[0-9a-fA-F]{24})$', views.product_detail, name='product_detail'),
    path('product/new/', views.product_new, name='product_new'),
    re_path(r'^product/(?P<pk>[0-9a-fA-F]{24})/edit/$', views.product_edit, name='product_edit'),
    re_path(r'^product/(?P<pk>[0-9a-fA-F]{24})/delete/$', views.product_delete, name='product_delete'),
    path('product/<str:name>/fetch/', views.product_fetch, name='product_fetch'),
]