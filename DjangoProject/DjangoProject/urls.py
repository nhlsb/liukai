"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app01 import views
## 编写URL与视图函数的对于关系
urlpatterns = [
    ## path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user_list/', views.user_list),
    path('user_add/', views.user_add),
    path('user_html_list/', views.user_html_list),
    path('user_html_add/', views.user_html_add),
    path('tpl/', views.tpl),
    path('news/', views.news),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
    path('user_management/',views.user_management),
    path('user_management_add/',views.user_management_add),
    path('user_management_delete/',views.user_management_delete)
]
