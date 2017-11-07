from django.shortcuts import render
from home.models import *
from utils.wrappers import *
from users.models import *


# 目的地精选详情页面
def detail(request):
    scenes = Scenes.objects.get(id=int(get(request, 'id')))
    # 获取目的地精选中的5个热门景点
    hotview = Scenes.objects.hot_view_byname('目的地精选')[:5]
    return render(request, 'front/detail.html', locals())


# 专题页面
def topics(request):
    # 获取某类景点中的10个热门景点
    hotview = Scenes.objects.hot_view_byid(int(get(request, 'cag')))
    cag = Category.objects.get(id=int(get(request, 'cag')))
    return render(request, 'front/topics.html', locals())


# 用户主页
def userhome(request):
    user = User.objects.get(id=int(get(request, 'id')))
    return render(request, 'front/userHome.html', locals())


# 用户游记
def usernotes(request):
    user = User.objects.get(id=int(get(request, 'id')))
    return render(request, 'front/userNotes.html', locals())


# 用户个人资料
def userinfo(request):
    user = User.objects.get(id=int(get(request, 'id')))
    return render(request, 'front/userInfo.html', locals())


# 用户相册
def userphotos(request):
    user = User.objects.get(id=int(get(request, 'id')))
    return render(request, 'front/userPhotos.html', locals())


# 游记详细页面
def noteview(request):
    note = TravelNotes.objects.get(id=int(get(request, 'id')))
    # 热门游记
    hotnote = TravelNotes.objects.get_hot_travel_notes()
    return render(request, 'front/NoteView.html', locals())


# 资讯详细页面
def infoshow(request):
    info = Information.objects.get(id=int(get(request, 'id')))
    # 热门资讯
    hotinfo = Information.objects.get_read_many()
    return render(request, 'front/info_show.html', locals())


# 用户相册内图片
def photos(request):
    user_album = UserAlbum.objects.get(id=int(get(request, 'id')))
    # 热门相册
    hotalbum = UserAlbum.objects.get_hot_album()
    print('----', hotalbum[0].albumimage_set.all()[0].image)
    return render(request, 'front/photolist.html', locals())



# # 三亚
# def sanya(request):
#     return render(request, 'front/sanya.html', locals())
#
#
# # 云南
# def yunnan(request):
#     return render(request, 'front/yunnan.html', locals())
#
#
# # 春季
# def spring(request):
#     return render(request, 'front/spring.html', locals())


def g(request):
    return render(request, 'front/g.html', locals())