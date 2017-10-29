from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.g, name='g'),
    # 目的地精选详情页面
    url(r'^detail/$', views.detail, name='detail'),
    # 专题页面
    url(r'^topics/$', views.topics, name='topics'),
    # 云南
    url(r'^yunnan/$', views.yunnan, name='yunnan'),
    # 三亚
    url(r'^sanya/$', views.sanya, name='sanya'),
    # 春季
    url(r'^spring/$', views.spring, name='spring'),
    ]