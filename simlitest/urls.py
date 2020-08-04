"""simlitest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('main/', views.main, name="main"),
    # 2~4번 바다
    path('sea1/', views.sea1, name="sea1"),
    path('sea2/', views.sea2, name="sea2"),
    path('sea3/', views.sea3, name="sea3"),
    # 2~4번 산
    path('mountain1/', views.mountain1, name="mountain1"),
    path('mountain2/', views.mountain2, name="mountain2"),
    path('mountain3/', views.mountain3, name="mountain3"),
    # 2~4번 사막
    path('desert1/', views.desert1, name="desert1"),
    path('desert2/', views.desert2, name="desert2"),
    path('desert3/', views.desert3, name="desert3"),
    # 영화 결과 페이지
    path('act/', views.act, name="act"),
    path('ani/', views.ani, name="ani"),
    path('com/', views.com, name="com"),
    path('hor/', views.hor, name="hor"),
    path('rom/', views.rom, name="rom"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
