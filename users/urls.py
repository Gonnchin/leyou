from django.conf.urls import url
from . import views

urlpatterns = [
    # 用户中心主页
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    # 注册后基本信息填写
    url(r'^reginfo/$', views.reg_info, name='reginfo'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logoff/$', views.logoff, name='logoff'),
    # 用户相册
    url(r'^ualbum/$', views.user_album, name='ualbum'),
    # 用户游记
    url(r'^travnotes/$', views.utravel_notes, name='travnotes'),
    # 用户消息
    url(r'^umessage/$', views.user_message, name='umessage'),
    # 个人关注
    url(r'^uconcern/$', views.user_concern, name='uconcern'),
    # 个人信息
    url(r'^uinfo/$', views.user_info, name='uinfo'),
    # 修改个人信息
    url(r'^updateinfo/$', views.uinfo_update, name='updateinfo'),
    # 发布游记
    url(r'^pub_travnotes/$', views.pub_travnotes, name='pub_travnotes'),
    # 创建相册
    url(r'^create_album/$', views.create_album, name='create_album'),
    # 密码管理
    url(r'^pwdmanage/$', views.pwd_manage, name='pwdmanage'),
    # 处理注册信息
    url(r'^register_handel/$', views.register_handel, name='register_handel'),
    url(r'^baseinfo_handle/$', views.baseinfo_handle, name='baseinfo_handle'),
    url(r'^check_exist/$', views.check_exist, name='check_exist'),
    url(r'^send_email/$', views.send_email, name='send_email'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    # 用户游记入库
    # url(r'^save_travnotes/$', views.save_travnotes, name='save_travnotes'),


]

