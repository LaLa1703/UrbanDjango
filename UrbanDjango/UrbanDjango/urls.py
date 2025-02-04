"""
URL configuration for UrbanDjango project.

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
from task2.views import ClassView, function_view
#from task3 import views as task3_views
from task4 import views as task4_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/class_view', ClassView.as_view(), name='class_view'),
    path('task2/function_view', function_view, name='function_view'),
    path('', task4_views.platform, name='platform'),
    path('task4/games/', task4_views.games, name='games'),
    path('task4/cart/', task4_views.cart, name='cart'),

]
