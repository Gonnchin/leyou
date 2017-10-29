from django.shortcuts import render
from home.models import *
from utils.wrappers import *


# 目的地精选详情页面
def detail(request):
    scenes = Scenes.objects.get(id=int(get(request, 'id')))
    # 获取目的地精选中的5个热门景点
    hotview = Scenes.objects.hot_view_byname('目的地精选')[:5]
    return render(request, 'front/detail.html', locals())


# 专题页面
def topics(request):
    # 获取某类景点中的10个热门景点
    hotview = Scenes.objects.hot_view_byid(int(get(request, 'cag')))[:10]
    cag = Category.objects.get(id=int(get(request, 'cag')))
    return render(request, 'front/topics.html', locals())


# 三亚
def sanya(request):
    return render(request, 'front/sanya.html', locals())


# 云南
def yunnan(request):
    return render(request, 'front/yunnan.html', locals())


# 春季
def spring(request):
    return render(request, 'front/spring.html', locals())


def g(request):
    return render(request, 'front/g.html', locals())