from django.db import models


# 定义抽象基类模型
class AbstractModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    updata_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        # 设置为抽象基类不为其创建表　
        abstract = True
