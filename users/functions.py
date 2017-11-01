from utils.wrappers import *
import re
from .models import *
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.conf import settings


# 注册页面信息校验
def check_register(request):
    user_pwd1 = post(request, 'user_pwd')
    user_pwd2 = post(request, 'user_pwdsure')
    user_email = post(request, 'user_email')
    get_vcode = post(request, 'verifycode')
    verifycode = get_session(request, 'verifycode')
    flag = True
    # 验证邮箱
    reg = '^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(reg, user_email):
        flag = False
        add_message(request, 'user_email', '邮箱格式不正确')

    # 验证密码
    if not(6 <= len(user_pwd1) <= 20):
        flag = False
        add_message(request, 'user_pwd', '请输入6-20位的密码')

    # 两次密码是否相同
    if user_pwd1 != user_pwd2:
        flag = False
        add_message(request, 'user_pwdsure', '两次密码输入不一致')

    # 注册验证核对
    if get_vcode != verifycode:
        flag = False
        add_message(request, 'verifycode', '验证码不正确')
    return flag


# 基本信息填写页面校验
def check_baseinfo(request):
    user_name = post(request, 'user_name')
    user_tel = post(request, 'user_tel')
    birthday = post(request, 'birthday')
    flag = True
    # 验证昵称
    if (not 2 <= len(user_name) <= 20) and (user_name != ''):
        flag = False
        add_message(request, 'user_name', '请设置2-20位的昵称')

    # 验证生日
    reg = datacheck
    if not re.match(reg, birthday) and (birthday != ''):
        flag = False
        add_message(request, 'brithday', '输入的日期格式不正确')

    # 验证手机号
    regex = '(\\+\\d+)?1[34578]\\d{9}$'
    if not re.match(regex, user_tel) and (user_tel != ''):
        flag = False
        add_message(request, 'user_tel', '输入的手机格式不正确')

    return flag


# 验证用户是否存在
def user_exist(request):
    user_email = get(request, 'user_email')
    user = User.objects.user_by_email(user_email)
    if user:
        return True
    else:
        return False


# 验证用户登录信息
def check_loginfo(request):
    email = post(request, 'user_email')
    pwd = post(request, 'user_pwd')
    user_pwd = password_encryption(pwd)
    # 验证邮箱
    reg = '^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(reg, email):
        return False

    # 验证密码
    if not (6 <= len(pwd) <= 20):
        return False

    user = User.objects.user_by_email(email)
    if user:
        if user.user_pwd == user_pwd:
            return True
    add_message(request, 'user_pwd', '用户名或密码错误')
    return False


# 修改密码
def update_pwd(request):
    original_pwd = post(request, 'original_pwd')
    new_pwd = post(request, 'new_pwd')
    sure_pwd = post(request, 'sure_pwd')
    # 验证密码
    if not (6 <= len(original_pwd) <= 20):
        return False
    if not (6 <= len(new_pwd) <= 20):
        return False
    if new_pwd != sure_pwd:
        return False

    user = User.objects.get(user_email=get_session(request, 'user_email'))
    pwd = password_encryption(original_pwd)
    if user.user_pwd == pwd:
        user.user_pwd = password_encryption(new_pwd)
        user.save()



# 分页
def pagination(request, date, num):
    pag_id = get(request, 'pag')
    if not pag_id:
        pag_id = 1
    # 分页显示
    paginator = Paginator(date, num)
    # 获取指定页码数据
    current_pag = paginator.page(pag_id)
    page_id = int(pag_id)
    return paginator, current_pag, page_id


# ------------------------------------------------------------------

# 记录用户名
def remember_email(request, response):
    reme = post(request, 'reme_email')

    if reme:
        set_cookie(response, 'user_email', post(request, 'user_email'))


# 记录登陆状态
def keep_status(request):
    user = User.objects.user_by_email(post(request, 'user_email'))
    set_session(request, 'user_email', user.user_email)
    set_session(request, 'uid', user.id)
    set_session(request, 'user_name', user.user_name)


# 判断用户是否登陆
def user_is_login(request):
    return get_session(request, 'user_email') and get_session(request, 'uid')


# 获取并保存发布的游记
def get_travnotes(request):
    ntitle = post(request, 'title')
    nkeyword = post(request, 'keywords')
    nimage = post(request, 'image')
    content_short = post(request, 'content_short')
    content = post(request, 'content')
    travelnote = {'ntitle': ntitle, 'nkeyword': nkeyword, 'nimage': nimage,
                'content_short': content_short, 'content': content}
    TravelNotes.objects.travelnotes(get_session(request, 'user_email'), travelnote)
    return travelnote


# 创建相册
def save_album(request):
    album_name = post(request, 'ualbum_name')
    album_short = post(request, 'album_short')
    album_user = User.objects.get(user_email=get_session(request, 'user_email'))
    # 创建相册
    myalbum = UserAlbum()
    myalbum.album_name = album_name
    myalbum.album_short = album_short
    myalbum.album_user = album_user
    myalbum.save()
    return myalbum


# 处理上传图片
def upload_handle(request, album):
    # 获取上传的图片
    my_images = request.FILES.getlist('ualbum_image')
    if not my_images:
        return
    for img in my_images:
        image = AlbumImage()
        image.image = img
        image.image_album = album
        image.save()

        # # 设置文件保存路径
        # image_path = settings.MEDIA_ROOT + img.name
        # with open(image_path, 'wb') as f:
        #     for data in img.chunks():
        #         f.write(data)


# 更新用户信息
def update_uinfo(request):
    user_name = post(request, 'user_name')
    gender = post(request, 'gender')
    signature = post(request, 'signature')
    brithday = post(request, 'brithday')
    user_addr = post(request, 'user_addr')
    user_tel = post(request, 'user_tel')
    # 修该信息
    user = User.objects.get(user_email=get_session(request, 'user_email'))
    user.user_name = user_name
    user.user_addr = user_addr
    user.gender = gender
    user.signature = signature
    user.birthday = brithday
    user.user_tel = user_tel
    user.save()






