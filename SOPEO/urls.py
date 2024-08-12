"""SOPEO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path
from EMS.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('create-employee', createEmployeee, name="create_employee"),
    path('employee-list', employee_list, name="employee_list"),
    path('employee-edit/<int:pid>', edit_employee, name="edit_employee"),
    path('delete_employee/<int:pid>', delete_employee, name="delete_employee"),
    path('leave-status/<int:pid>', leave_status, name="leave_status"),
]
