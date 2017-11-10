from django.conf.urls import url
from . import views

urlpatterns = [
    # 网站主页
    url(r'^$', views.index, name='index'),
    # 目的地精选
    url(r'^destination/$', views.destination, name='destination'),
    # 摄影
    url(r'^photography/$', views.photography, name='photography'),
    # 游记
    url(r'^travelnotes/$', views.travelnotes, name='travelnotes'),
    # 旅行家
    url(r'^tourist/$', views.tourist, name='tourist'),
    # 资讯
    url(r'^info/$', views.info, name='info'),
    # 旅行社
    url(r'^travel_agency/$', views.travel_agency, name='travel'),
    # 压缩图片
    url(r'^mini_image/$', views.mini_image, name='mini_image'),

    ]


