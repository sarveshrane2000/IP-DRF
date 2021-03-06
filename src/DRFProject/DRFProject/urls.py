"""DRFProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('logout/<str:token>', views.logout_view, name='logout_view'),
    path('delete_user_data_item/<str:token>/<str:item_field>', views.handle_user_delete_data, name='delete_user_data_item'),
    path('signup/', views.signup_view, name='signup_view'),
    path('user/<str:token>', views.user_view, name='user_view'),
    path('api/v1/', include('api.urls'))
]
