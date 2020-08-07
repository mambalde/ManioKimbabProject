from django.shortcuts import render

from . import views
urlpatterns = [
    path('', views.index, name='menuLists'),
    path('<int: menuItem_id>', views.menuList, name='menuItem')
    path('search', views.search, name='search')
]
