from django.shortcuts import render
from .models import *
from users.models import *
from django.http import JsonResponse


# 网站主页
def index(request):
    # 获取目的地精选中的9个热门景点
    hotview = Scenes.objects.hot_view_byname('目的地精选')
    # 获取多个热门景点类型
    hotcag = Category.objects.hot_view()
    # 获取最新资讯信息
    infos = Information.objects.get_new_info()
    # 获取热门相册
    albums = UserAlbum.objects.get_hot_album()[:6]
    # 获取旅游达人
    travel_users = User.objects.get_travel_user()[:5]
    # 获取2条精彩游记
    notes = TravelNotes.objects.get_hot_travel_notes()[:2]

    return render(request, 'home/index.html', locals())


def mini_image(request):
    data = get(request, 'id').split(':')
    type1 = data[1]
    id = int(data[0])
    if type1 == 'cag':
        image = '/static/' + str(Category.objects.get(id=id).mini_background)
    elif type1 == 'view':
        image = '/static/' + str(Scenes.objects.get(id=id).mini_image)
    return JsonResponse({"image": image})


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
    # 获取所有相册
    albums = UserAlbum.objects.all().order_by('-id')
    return render(request, 'home/photos.html', locals())


# 游记
def travelnotes(request):
    # 获取所有游记
    notes = TravelNotes.objects.all().order_by('-id')
    return render(request, 'home/notes.html', locals())


# 旅行家
def tourist(request):
    users = User.objects.all()
    return render(request, 'home/tourist.html', locals())


# 资讯
def info(request):
    # 获取资讯信息
    infos = Information.objects.all()
    # 资讯阅读排序
    order_infos = Information.objects.get_read_many()
    return render(request, 'home/info.html', locals())


# 旅行社
def travel_agency(request):
    return render(request, 'home/travel.html', locals())



