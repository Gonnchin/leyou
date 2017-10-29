from django.shortcuts import render, redirect
from .functions import *
from .models import *
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from .tasks import *
import random

user_email = ''


# 注册
def register(request):
    return render(request, 'user/regist.html', locals())


# 登录
def login(request):
    info = get_messages(request)
    # 修改密码
    if request.method == 'POST':
        update_pwd(request)
    return render(request, 'user/login.html', locals())


# 注册信息填写（昵称..）
def reg_info(request):
    try:
        info = get_messages(request)
    except:
        pass
    return render(request, 'user/reg_info.html', locals())


# 用户中心主页
def index(request):
    # # 判断是否登录
    # if not user_is_login(request):
    #     return redirect(reverse('users:login'))
    user_name = get_session(request, 'user_name')
    return render(request, 'user/index.html', locals())


# 用户相册
def user_album(request):
    # 判断是否登录
    # if not user_is_login(request):
    #     return redirect(reverse('users:login'))

    user_email = get_session(request, 'user_email')
    if request.method == 'POST':
        # 相册入库
        album = save_album(request)
        # 处理上传图片
        upload_handle(request, album)

    # 获取用户所有相册
    albums = UserAlbum.objects.get_album(user_email)
    # 用户相册分页
    paginator, current_pag, page_id = pagination(request, albums, 8)
    return render(request, 'user/photos.html', locals())


# 用户游记
def utravel_notes(request):
    # 判断是否登录
    # if not user_is_login(request):
    #     return redirect(reverse('users:login'))

    user_email = get_session(request, 'user_email')

    # 用户游记入库
    if request.method == 'POST':
        TravelNotes.objects.save_travelnotes(request, user_email)

    # 获取用户所有游记
    travelnotes_all = TravelNotes.objects.get_travel_notes(user_email)

    # 用户游记分页
    paginator, current_pag, page_id = pagination(request, travelnotes_all, 2)
    return render(request, 'user/utravel_notes.html', locals())


# 用户消息
def user_message(request):
    # 判断是否登录
    # if not user_is_login(request):
    #     return redirect(reverse('users:login'))
    return render(request, 'user/umsg.html', locals())


# 用户关注
def user_concern(request):
    # 判断是否登录
    # if not user_is_login(request):
    #     return redirect(reverse('users:login'))
    return render(request, 'user/unotice.html', locals())


# 个人信息
def user_info(request):
    # 判断是否登录
    # if not user_is_login(request):
    #     return redirect(reverse('users:login'))
    if request.method == 'POST':
        # 更新用户信息
        update_uinfo(request)
    user = User.objects.get(user_email=get_session(request, 'user_email'))
    return render(request, 'user/uinfo.html', locals())


# 修改个人信息
def uinfo_update(request):
    user = User.objects.get(user_email=get_session(request, 'user_email'))
    return render(request, 'user/uinfo_update.html', locals())


# 密码管理
def pwd_manage(request):
    # 判断是否登录
    # if not user_is_login(request):
    #     return redirect(reverse('users:login'))
    return render(request, 'user/upwd.html', locals())


# 创建相册
def create_album(request):
    return render(request, 'user/create_album.html')


# 发布游记
def pub_travnotes(request):
    return render(request, 'user/pub_travnotes.html')


# 处理注册信息
def register_handel(request):
    # 校对注册信息
    if check_register(request):
        # 1.信息入库
        User.objects.uinfo_save(request)
        global user_email
        user_email = post(request, 'user_email')
        # 2.跳转基本信息填写页面
        return redirect(reverse('users:reginfo'))
    else:
        # 跳转到注册页面
        return redirect(reverse('users:register'))


# 处理注册后填写的信息
def baseinfo_handle(request):
    # 校对基本信息
    if check_baseinfo(request):
        # 1.基本信息入库
        User.objects.baseinfo_save(request, user_email)
        # 2.跳转登陆页面
        return redirect(reverse('users:login'))
    else:
        # 跳转到注册页面
        return redirect(reverse('users:reginfo'))


# 验证用户名是否存在
def check_exist(request):
    if user_exist(request):
        return JsonResponse({"ret": 1})
    else:
        return JsonResponse({"ret": 0})


# 发送邮件
def send_email(request):
    content = str(random.randint(111111, 999999))
    set_session(request, 'verifycode', content)
    # 异步发送注册邮件
    email_regiester.delay(get(request, 'mailbox'), content)
    return JsonResponse({'ret': 1})


# 处理登陆信息
def login_handle(request):
    # 用户信息正确　
    if check_loginfo(request):
        response = redirect(reverse('users:index'))
        # 记住用户登陆邮箱
        remember_email(request, response)
        # 保存用户登陆信息
        keep_status(request)
        # 跳转到用户中心
        return response
    # 用户信息不正确　
    else:
        # 跳转到登陆页面
        return redirect(reverse('users:login'))


# 退出登录
def logoff(request):
    # 退出后还在当前页面
    # url = get_redirect_url(request)
    del_session(request)
    return redirect(reverse("users:login"))




