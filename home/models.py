from django.db import models
from db.AbstractModel import *
from tinymce.models import HTMLField


# 自定义景点分类管理器
class CategoryManager(models.Manager):
    # 根据浏览量对景点分类　排序　
    def hot_view(self):
        return self.exclude(id=1).order_by('-cag_look')


# 景点分类模型
class Category(AbstractModel):
    # 类型名称
    cag_name = models.CharField(max_length=20)
    # 该类型浏览量
    cag_look = models.IntegerField(default=0)
    # 标志图片
    cag_image = models.ImageField()
    # 背景图
    background = models.ImageField(default='')
    # 压缩后的图片
    mini_background = models.ImageField(default='')
    # 描述
    cag_describe = models.CharField(max_length=300, default='')
    objects = CategoryManager()


# 自定义景点管理器类
class ScenesManager(models.Manager):
    # 根据景点类型name获取9个热门景点
    def hot_view_byname(self, cag_name):
        cag = Category.objects.filter(cag_name=cag_name)
        return self.filter(view_category=cag).order_by('-view_look')[:9]

    # 根据景点类型id获取10个热门景点
    def hot_view_byid(self, cag_id):
        return self.filter(view_category_id=cag_id).order_by('-view_look')[:10]

    # 根据景点类型name获10个最新景点
    def new_view_byname(self, cag_name):
        cag = Category.objects.filter(cag_name=cag_name)
        return self.filter(view_category=cag).order_by('-id')[:9]


# 景点模型类
class Scenes(AbstractModel):
    # 景点名称
    view_name = models.CharField(max_length=20)
    # 标志图片
    view_image = models.ImageField()
    # 压缩后的图片
    mini_image = models.ImageField(default='')
    # 景点标题
    view_title = models.CharField(max_length=30)
    # 景点推荐指数
    view_score = models.IntegerField(null=True, blank=True)
    # 景区看点
    view_spot = HTMLField()
    # 景点简介/驴友指点
    view_introduce = models.CharField(max_length=100)
    # 景点描述
    view_describe = HTMLField()
    # 景点位置
    view_location = HTMLField()
    # 景点所属类型
    view_category = models.ForeignKey(Category)
    # 景点浏览量
    view_look = models.IntegerField(default=0)
    objects = ScenesManager()