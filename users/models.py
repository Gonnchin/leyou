from django.db import models
from utils.wrappers import *
from db.AbstractModel import *
from tinymce.models import HTMLField


# 自定义管理器
class UserManage(models.Manager):

    # 增加函数,用户名查询用户
    def user_by_email(self, email):
        try:
            return self.get(user_email=email)
        except User.DoesNotExist:
            return None

    # 将用户注册信息入库
    def uinfo_save(self, request):
        user = User()
        email = post(request, 'user_email')
        # 注册页面信息入库
        user.user_email = email
        user.user_pwd = password_encryption(post(request, 'user_pwd'))
        user.save()

    # 基本信息填写页面入库
    def baseinfo_save(self, request, email):
        user = self.get(user_email=email)
        user.user_name = post(request, 'user_name')
        if not user.user_name:
            user.user_name = email
        user.birthday = post(request, 'birthday')
        user.user_tel = post(request, 'user_tel')
        user.user_addr = post(request, 'user_addr')
        user.signature = post(request, 'sign')
        user.save()


# 用户模型类
class User(AbstractModel):
    user_name = models.CharField(max_length=30)
    # 用户名密码
    user_pwd = models.CharField(max_length=70)
    user_email = models.CharField(max_length=50, unique=True)
    user_tel = models.CharField(max_length=11, blank=True, null=True)
    user_addr = models.CharField(max_length=50, blank=True, null=True)
    # 个性签名
    signature = models.CharField(max_length=60, blank=True, null=True)
    gender = models.BooleanField(default=1)
    birthday = models.CharField(max_length=10,  blank=True, null=True)
    user_photo = models.ImageField(default='')
    objects = UserManage()


# 用户游记管理类
class TravelNotesManager(models.Manager):

    # 获取用户所有游记
    def get_travel_notes(self, user_email):
        user = User.objects.get(user_email=user_email)
        # 获取用户的所有游记
        user_notes = user.travelnotes_set.all()
        # 用户对应的所有游记
        travelnotes_all = []
        for notes in user_notes:
            travelnotes_all.append(notes)
        return travelnotes_all

    # 用户游记入库
    def save_travelnotes(self, request, email):
        user = User.objects.get(user_email=email)
        tnotes = TravelNotes()
        tnotes.travel_user_id = user.id
        tnotes.travel_title = post(request, 'ntitle')
        tnotes.travel_kwd = post(request, 'nkeyword')
        tnotes.travel_image = post(request, 'nimage')
        tnotes.travel_content = post(request, 'content')
        tnotes.content_short = post(request, 'content_short')
        tnotes.save()


# 用户游记类
class TravelNotes(AbstractModel):
    # 创建游记的用户
    travel_user = models.ForeignKey(User)
    # 游记标题
    travel_title = models.CharField(max_length=20)
    # 游记关键字
    travel_kwd = models.CharField(max_length=20)
    # 游记图片
    travel_image = models.ImageField()
    # 游记内容简介
    content_short = models.CharField(max_length=100)
    # 游记内容
    travel_content = models.TextField()
    # 浏览量
    notes_look = models.IntegerField(default=0)

    objects = TravelNotesManager()


# 用户相册管理类
class UserAlbumManager(models.Manager):
    # 获取用户所有相册
    def get_album(self, user_email):
        user = User.objects.get(user_email=user_email)
        # 获取用户的所有相册
        user_albums = user.useralbum_set.all()
        #
        albums = []
        for album in user_albums:
            albums.append(album)
        return albums


# 用户相册
class UserAlbum(AbstractModel):
    # 相册名称
    album_name = models.CharField(max_length=8)
    # 相册简介
    album_short = models.CharField(max_length=14)
    # 相册所属用户
    album_user = models.ForeignKey(User)
    # 浏览量
    album_look = models.IntegerField(default=0)
    objects = UserAlbumManager()


# 相册图片管理类
class AlbumImageManager(models.Manager):
    pass


# 相册图片模型
class AlbumImage(AbstractModel):
    # 图片
    image = models.ImageField(default='')
    # 所属相册
    image_album = models.ForeignKey(UserAlbum)
    objects = AlbumImageManager()


# 资讯模型管理类
class InformationManager(models.Manager):
    pass


# 资讯信息模型类
class Information(AbstractModel):
    # 标题
    info_title = models.CharField(max_length=20)
    # 发布者
    info_user = models.CharField(max_length=20)
    # 资讯浏览量
    info_look = models.IntegerField(default=0)
    # 资讯内容
    info_content = HTMLField()
    objects = InformationManager()