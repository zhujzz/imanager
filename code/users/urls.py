# -*- coding: utf-8 -*-
"""
@author: zhujz
@file: urls.py
@time: 2018/4/14-23:04
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_users, name='users'),
]
