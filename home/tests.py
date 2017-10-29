from django.test import TestCase
from .models import *
import random
#
#
# # 创建分类
# cags = ['目的地精选', '古镇', '名山', '宗教', '小吃', '智慧旅游', '瀑布', '三亚', '古建筑',
#         '古楼', '云南', '名湖', '园林', '名寺', '纪念馆', '春天', '井冈山']
# for cag in cags:
#     c = Category()
#     c.cag_name = cag
#     c.cag_image = str(random.randint(1, 18)) + '.jpg'
#     c.save()
#


# cags = Category.objects.all()
# for cag in cags:
#     cag.cag_describe = '园林美在它那与大自然合而为一的精妙布局，美在它那如同山水画一般的独特意境，美在它那渗透着深厚文化底蕴的一草一木，一砖一石。漫步在园林中，处处充满着诗情画意，时时是洋溢着浓墨温情，来到这里，就仿佛走进人间天堂。'
#     cag.save()


# num = ['','guzhen','mingshan','zongjiao','xiaochi','jingqu','pubu','sanya','gujianzhu','gulou'
#     ,'yunnan','minghu','yuanlin','mingsi','jinianguan','chuntian','jinggangshan']
# cags = Category.objects.all()
# for i,cag in enumerate(cags):
#     cag.background = 'front/image/background/'+num[i] +'.png'
#     cag.save()





# a = "故宫博物院、什刹海、蓟门烟树、西山晴雪、天津文庙、九龙山国家森林公园、陆家嘴、天生三桥、仙女山、芙蓉洞、酉阳桃花源景区、重庆抗战遗址博物馆、綦江黑山谷景区、南川金佛山、涪陵武陵山大裂谷、张飞庙"
#
# view_names = a.split('、')
#
# for i in view_names:
#     scenes = Scenes()
#     scenes.view_name = i
#     scenes.view_image = str(random.randint(1, 60)) + '.jpg'
#     scenes.view_title = '泰安登泰山，一览众山小'
#     scenes.view_score = 5
#     scenes.view_spot = '天烛峰 日观峰 岱庙'
#     scenes.view_introduce = '泰山山体雄伟壮观，景色秀丽，因其气势之磅礴为五岳之首，故又有"天下名山第一"的美誉。泰山多松柏，显其葱郁，又多溪泉，故而不乏灵秀。'
#     scenes.view_describe = """景区景点
# 六大风景区：
# 泰山风景旅游区包括幽区、旷区、奥区、妙区、秀区、丽区六大风景区。
# 泰山四大奇观：
# 游泰山的最佳时间为每年的5月到11月。游泰山看四个奇观：泰山日出、云海玉盘、晚霞夕照、黄河金带。
#
# 交通线路
# 泰山与泰安市区山城紧连，泰安城区位于泰山南麓。泰山在泰安城区正北方向，天晴的日子，泰山主峰玉皇顶清晰可见。泰山正式的售门票登山进口有四处，分别是：红门宫进山口、天外村（天地广场）进山口、桃花峪进山口、天烛峰进山口。
# 红门宫进山口即泰山东路，天外村进山口即泰山西路。四处进山口之中，有两处在泰安城区北缘：徒步登山的红门进山口在火车站东北方向2.5公里（在火车站乘K3路公交车往东终点站）；乘车上山的天外村登山口在火车站正北约2公里（在火车站乘3路公交车往西终点站）；桃花源登山口在泰山西麓，距泰山火车站约12公里（在火车站乘18路公交车往西到终点站）；天烛峰进山口在泰山东麓，距泰山火车站约18公里。K3路是一条便捷的旅游线路，两头的终点站分别是红门和天外村，都是登山的入口，红门是步行线，天外村是汽车线，不要坐反！泰安老火车站叫泰山站，位于市中心偏南。新的高铁站叫泰安站，位于西部新区，坐17路，18路，K37路可以到达市区。从泰山火车站前往以上介绍的几处登山口最为方便，均有公交车或旅游公交车直通。泰山火车站是泰山旅游交通的中心枢纽，泰安的几处汽车站也在火车站周围，所以建议不熟悉泰山旅游交通的游客，到达泰安后都先去火车站（城区大部分公交都通往火车站，车票一元或两元），然后分乘各路车去往不同的进山口或景区。
# """
#     scenes.view_location = '华北地区 北京市 东城区'
#     scenes.view_category_id = 1
#     scenes.save()

