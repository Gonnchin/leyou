from haystack import indexes
from .models import Scenes  # 导入当前应用中models中的模型类


# 指定对于某个类的某些数据建立索引
class ScenesIndex(indexes.SearchIndex, indexes.Indexable):
    # document=True,将要检索的信息放到text中存储，　使用模本显示检索出的内容
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Scenes

    # 返回查询结果集
    def index_queryset(self, using=None):
        return self.get_model().objects.all()