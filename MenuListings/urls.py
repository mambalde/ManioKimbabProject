from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menuItems'),
    path('<int:menuItem_id>', views.menuList, name='menuItem'),
    path('search', views.search, name='search')
]
