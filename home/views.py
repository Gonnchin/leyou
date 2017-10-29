from django.shortcuts import render
from .models import *


# 网站主页
def index(request):
    # 获取目的地精选中的9个热门景点
    hotview = Scenes.objects.hot_view_byname('目的地精选')
    # 获取多个热门景点类型
    hotcag = Category.objects.hot_view()
    return render(request, 'home/index.html', locals())


# 目的地精选
def destination(request):
    # 获取目的地精选中的9个最新景点
    newview = Scenes.objects.new_view_byname('目的地精选')
    # 获取目的地精选中的景点
    desview = Scenes.objects.all()[:26]
    # 获取最热门景点类型
    hotcag = Category.objects.hot_view()
    return render(request, 'home/dest.html', locals())


# 摄影
def photography(request):
    return render(request, 'home/photos.html', locals())


# 游记
def travelnotes(request):
    return render(request, 'home/notes.html', locals())


# 旅行家
def tourist(request):
    return render(request, 'home/tourist.html', locals())


# 资讯
def info(request):
    return render(request, 'home/info.html', locals())


# 旅行社
def travel_agency(request):
    return render(request, 'home/travel.html', locals())



