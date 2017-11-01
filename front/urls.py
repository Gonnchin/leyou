from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.g, name='g'),
    # 目的地精选详情页面
    url(r'^detail/$', views.detail, name='detail'),
    # 专题页面
    url(r'^topics/$', views.topics, name='topics'),
    # 用户主页
    url(r'^userhome/$', views.userhome, name='userhome'),
    # 用户游记
    url(r'^usernotes/$', views.usernotes, name='usernotes'),
    # 用户个人资料
    url(r'^userinfo/$', views.userinfo, name='userinfo'),
    # 用户相册
    url(r'^userphotos/$', views.userphotos, name='userphotos'),
    # 游记详细页面
    url(r'^noteview/$', views.noteview, name='noteview'),
    # 资讯详细页面
    url(r'^infoshow/$', views.infoshow, name='infoshow'),
    # 用户相册内图片
    url(r'^photos/$', views.photos, name='photos'),




    # # 云南
    # url(r'^yunnan/$', views.yunnan, name='yunnan'),
    # # 三亚
    # url(r'^sanya/$', views.sanya, name='sanya'),
    # # 春季
    # url(r'^spring/$', views.spring, name='spring'),
    ]