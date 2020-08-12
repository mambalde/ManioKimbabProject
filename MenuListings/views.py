from django.shortcuts import render

def index (request):
  return  render(request, 'menuItems/menuItems.html')


def menuList (request):
   return render(request, 'menuItems/menuItem.html')


def search (request):
   return render(request, 'menuItems/search.html')