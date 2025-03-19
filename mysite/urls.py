"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from warehouse import views

handler400 = 'warehouse.views.error_400'
handler401 = 'warehouse.views.error_401'
handler403 = 'warehouse.views.error_403'
handler404 = 'warehouse.views.error_404'
handler500 = 'warehouse.views.error_500'
handler502 = 'warehouse.views.error_502'
handler503 = 'warehouse.views.error_503'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('warehouse.urls')),
     
]
