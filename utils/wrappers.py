import hashlib
from django.contrib import messages


def get(request, key):
    return request.GET.get(key, '')


def post(request, key):
    return request.POST.get(key, '')


def post_list(request, key):
    return request.POST.getlist(key, '')


# 加密函数
def password_encryption(user_pwd, str=''):
    sha = hashlib.sha256()
    new_pwd = '%^%' + user_pwd + '&*#'
    sha.update(new_pwd.encode('utf-8'))
    return sha.hexdigest()


# 添加消息
def add_message(request, key, value):
    messages.add_message(request, messages.INFO, key + ":" + value)


# 获取消息
def get_messages(request):
    info_list = messages.get_messages(request)
    info = dict()
    for msg in info_list:
        # 取出来的是对象，转换成字符串
        content = str(msg).split(':')
        info[content[0]] = content[1]
    return info


# 设置cookie
def set_cookie(response, key, value):
    response.set_cookie(key, value, max_age=60*60*12)


# 获取cookie
def get_cookie(request, key):
    return request.cookie.get(key, '')


# 删除cookie
def del_cookie(response, key):
    response.delete_cookie(key)


# 设置session
def set_session(request, key, value):
    request.session[key] = value


# 获取session
def get_session(request, key):
    return request.session.get(key, '')


# 清除session
def del_session(request):
    request.session.flush()



datacheck = """"((^((1[8-9]\d{2})|([2-9]\d{3}))([-\/\._])(10|12|0?[13578])([-\/\._])
        (3[01]|[12][0-9]|0?[1-9])$)|(^((1[8-9]\d{2})|([2-9]\d{3}))([-\/\._])(11|0?[469])
        ([-\/\._])(30|[12][0-9]|0?[1-9])$)|(^((1[8-9]\d{2})|([2-9]\d{3}))([-\/\._])(0?2)
        ([-\/\._])(2[0-8]|1[0-9]|0?[1-9])$)|(^([2468][048]00)([-\/\._])(0?2)([-\/\._])
        (29)$)|(^([3579][26]00)([-\/\._])(0?2)([-\/\._])(29)$)|(^([1][89][0][48])([-\/\._])
        (0?2)([-\/\._])(29)$)|(^([2-9][0-9][0][48])([-\/\._])(0?2)([-\/\._])(29)$)|(^([1][89]
        [2468][048])([-\/\._])(0?2)([-\/\._])(29)$)|(^([2-9][0-9][2468][048])([-\/\._])(0?2)
        ([-\/\._])(29)$)|(^([1][89][13579][26])([-\/\._])(0?2)([-\/\._])(29)$)|(^([2-9][0-9]
        [13579][26])([-\/\._])(0?2)([-\/\._])(29)$))"""