from django.test import TestCase
from .models import *
import random




# cag = Category.objects.all()
# desc = ['您是否还在为普通旅游线路的低效转化而焦虑？\n您是否还在为精品旅游线路的昂贵价格头疼？\n现在，机会来了，十大全景城市等你轻松游！',
#  '历史支离破碎在渐行渐远的记忆中，\n那些褪色的片段一直在重现、倒退、快进、倒退。\n正所谓前事不忘，后事之师，以史为鉴，开创未来，\n历史不应该被忘记，让我们纪念历史\n-----历史的烛光不改，民族的记忆永恒',
#  '静静的古寺已不是昨天的清静之地，人间的烟火，人们的虔诚，为了什么，是信仰的吗？也许只是在寻找心灵中的住所。而你，远离人间的烟火，却存在于人间之中，是社会的需要还是时代的产品。无可否认，世界因你存在，而更加美好,身处在这样一个被信仰笼罩着的地方，每一个人都是幸福的。',
#  '园林美在它那与大自然合而为一的精妙布局，美在它那如同山水画一般的独特意境，美在它那渗透着深厚文化底蕴的一草一木，一砖一石。漫步在园林中，处处充满着诗情画意，时时是洋溢着浓墨温情，来到这里，就仿佛走进人间天堂。',
#  '吃是一种美德，\n吃货是一种境界，\n吃货最高境界就是吃遍天下美食。\n错过美食和错过爱情一样都是令人惋惜的事情，\n所以还等着什么，\n让我们拥抱爱情！\n让我们追逐美食！ \n',
#  '中国湖泊之美自早就被古人以难以数计的诗文词赋称赞，愛上倒影，愛上美丽的湖泊。跟著最美的十大湖泊，一起來看看自然的杰作，看看這些安放倒影的精灵吧。',
#  '建筑的历史是遥远而悠久的，它的年龄几乎和人类的历史一样漫长。人类的进化可以从建筑的演变中得到有力的证明。建筑的丰富性多样性超越了我的想象。现在让我们欣赏下能够流芳千古载入史册的古楼。',
#  '历史文化名城镇远县的古建筑遍布县城内的大街小巷。众多的古建筑成为历史文化名城的主要文化内涵。让我们一起来欣赏下这些瑰宝吧。',
#  '提到瀑布，给人的第一感觉就是力吞山河的磅礴气势，\n与人一种气力之美。站在瀑布边上，聆听落水拍打岩石的声音，是那么的雄壮。\n下面就有我来给您列举几个我国著名的瀑布，带您领略自然之力。',
#  '尽管时空不同，民族有别，人们对宗教的信仰的追求却同样热切，成千上万的信徒到个宗教圣地朝拜，犹太人在耶路撒冷的哭墙前，泣诉两千年来的流离失所；基督教徒沿哭墙不远的苦路，默想耶稣基督的受难与救赎；藏传佛教教徒跋涉千里，一步一磕头，一直磕到拉萨。 他们的虔诚，让人感动不已。让我们来看看这些离神最近的地方---宗教圣地',
#  '名山是神话传说最多的地方，从三皇五帝、君王大臣到民间的凡夫俗子，都留下了或喜、或悲、或怒、或怨的美丽传说，名山也因此而充满了灵性；而历代名人留下的诗词题赋则更增加了这些名山的文化底蕴，留给我们的是无尽的遐想。中国名山以其俊秀的英姿、绚丽的风采吸引着全世界的游客留恋忘返。',
#  '古镇那一座座简朴而凝重的廊桥，回荡过我的喜怒哀乐，承载过我的童年、青年，也弥漫着古镇居民的善良、淳朴、诚实、亲切……长大后，她还会一次次不厌烦地撞击着我的心灵，一趟趟地穿越时空，不期而遇地一起涌入我的梦境。古镇，永久的风景,生命有你真精彩。',
#  '园林美在它那与大自然合而为一的精妙布局，美在它那如同山水画一般的独特意境，美在它那渗透着深厚文化底蕴的一草一木，一砖一石。漫步在园林中，处处充满着诗情画意，时时是洋溢着浓墨温情，来到这里，就仿佛走进人间天堂。',
#  '吃是一种美德，\n吃货是一种境界，\n吃货最高境界就是吃遍天下美食。\n错过美食和错过爱情一样都是令人惋惜的事情，\n所以还等着什么，\n让我们拥抱爱情！\n让我们追逐美食！ \n',
#  '中国湖泊之美自早就被古人以难以数计的诗文词赋称赞，愛上倒影，愛上美丽的湖泊。跟著最美的十大湖泊，一起來看看自然的杰作，看看這些安放倒影的精灵吧。',
#  '建筑的历史是遥远而悠久的，它的年龄几乎和人类的历史一样漫长。人类的进化可以从建筑的演变中得到有力的证明。建筑的丰富性多样性超越了我的想象。现在让我们欣赏下能够流芳千古载入史册的古楼。',
#  '历史文化名城镇远县的古建筑遍布县城内的大街小巷。众多的古建筑成为历史文化名城的主要文化内涵。让我们一起来欣赏下这些瑰宝吧。',
#  '提到瀑布，给人的第一感觉就是力吞山河的磅礴气势，\n与人一种气力之美。站在瀑布边上，聆听落水拍打岩石的声音，是那么的雄壮。\n下面就有我来给您列举几个我国著名的瀑布，带您领略自然之力。',
#  '尽管时空不同，民族有别，人们对宗教的信仰的追求却同样热切，成千上万的信徒到个宗教圣地朝拜，犹太人在耶路撒冷的哭墙前，泣诉两千年来的流离失所；基督教徒沿哭墙不远的苦路，默想耶稣基督的受难与救赎；藏传佛教教徒跋涉千里，一步一磕头，一直磕到拉萨。 他们的虔诚，让人感动不已。让我们来看看这些离神最近的地方---宗教圣地',
#  '名山是神话传说最多的地方，从三皇五帝、君王大臣到民间的凡夫俗子，都留下了或喜、或悲、或怒、或怨的美丽传说，名山也因此而充满了灵性；而历代名人留下的诗词题赋则更增加了这些名山的文化底蕴，留给我们的是无尽的遐想。中国名山以其俊秀的英姿、绚丽的风采吸引着全世界的游客留恋忘返。',
#  '古镇那一座座简朴而凝重的廊桥，回荡过我的喜怒哀乐，承载过我的童年、青年，也弥漫着古镇居民的善良、淳朴、诚实、亲切……长大后，她还会一次次不厌烦地撞击着我的心灵，一趟趟地穿越时空，不期而遇地一起涌入我的梦境。古镇，永久的风景,生命有你真精彩。'
#      ]
#
#
# for i,de in enumerate(cag):
#     de.cag_describe = desc[i]
#     de.save()




image_list = [
 # 'bishushanzhuang.jpg',
 # 'shajiabangjinianguan.jpg',
 # 'ludingqiaojinianguan.jpg',
 # 'lidazhaojinianguan.jpg',
 # 'badashanjinianguan.jpg',
 # 'zhongshanjinianguan.jpg',
 # 'lingyinsi.jpg',
 # 'damingsi.jpg',
 # 'songzanlinsi.jpg',
 # 'wofosi.jpg',
 # 'dazhaosi.jpg',
 # 'linggusi.jpg',
 # 'tianningsi.jpg',
 # 'yanquansi.jpg',
 # 'hanshansi.jpg',
 # 'chongshengsi.jpg',
 # 'zuozhengyuan.jpg',
 # 'liuyuan.jpg',
 'geyuan.jpg',
 'bishushanzhuang.jpg',
 'yuanmingyuan.jpg',
 'yiheyuan.jpg',
 'yuyuan.jpg',
 'jingsiyuan.jpg',
 'gulianhuachi.jpg',
 'shizilin.jpg',
 'tongluowan.jpg',
 'donghu.jpg',
 'xihu.jpg',
 'shanghu.jpg',
 'taihu.jpg',
 'xuanwuhu.jpg',
 'shouxihu.jpg',
 'yunlonghu.jpg',
 'yangchenghu.jpg',
 'weiminghu.jpg',
 'qinghaihu.jpg',
 'tiananmenchenglou.jpg',
 'yueyanglou.jpg',
 'yuejianglou.jpg',
 'yueyalou.jpg',
 'tengwangge.jpg',
 'kejiatulou.jpg',
 'yanyulou.jpg',
 'daguanlou.jpg',
 'penglaige.jpg',
 'huanghelou.jpg',
 'gugong.jpg',
 'budalagong.jpg',
 'yiheyuan.jpg',
 'badalingchangcheng.jpg',
 'zhuozhengyuan.jpg',
 'beijingtiantan.jpg',
 'mogaoku.jpg',
 'huanghelou.jpg',
 'wudangshan.jpg',
 'yueyanglou.jpg',
 'jiuzhaigou.jpg',
 'taiyangdao.jpg',
 'lushan.jpg',
 'gudongsenlin.jpg',
 'laya.jpg',
 'dieshuihe.jpg',
 'jingbohu.jpg',
 'malinghe.jpg',
 'huanggushu.jpg',
 'xiningqingzhen.jpg',
 'budalagong.jpg',
 'emeishan.jpg',
 'qingchengshan.jpg',
 'dazhaosi.jpg',
 'wutaishan.jpg',
 'wofosi.jpg',
 'putuoshan.jpg',
 'wudangshan.jpg',
 'wuyishan.jpg',
 'taishan.jpg',
 'emeishan.jpg',
 'huangshan.jpg',
 'huashan.jpg',
 'wudangshan.jpg',
 'hengshan.jpg',
 'lushan.jpg',
 'wuyishan.jpg',
 'putuoshan.jpg',
 'wutaishan.jpg',
 'tongliguzhen.jpg',
 'hexiaguzhen.jpg',
 'jingdezhen.jpg',
 'zhujiajiaoguzhen.jpg',
 'shuheguzhen.jpg',
 'baishaguzhen.jpg',
 'huangyuanguzhen.jpg',
 'xianggelilaguzhen.jpg',
 'dangeerguzhen.jpg',
 'xitangguzhen.jpg',
 'yiheyuan.jpg',
 'yuntaishan.jpg',
 'taishan.jpg',
 'laohushatan.jpg',
 'xiangshawan.jpg',
 'jingbohu.jpg',
 'qingjiang.jpg',
 'xikou.jpg',
 'qingchengshan.jpg',
 'nanjingdatushajinianguan.jpg',
 'zhouenlaijinainguan.jpg',
 'baiseqiyijinianguan.jpg',
 'yangzhoubaguaijinianguan.jpg',
 'leifengjinianguan.jpg'
              ]

# views = Scenes.objects.all()
#
# for i,image in enumerate(views):
#     image.view_image = image_list[i]
#     image.save()







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





# a = "西湖、阅江楼、烟雨楼、青海湖、月牙楼、云龙湖、东湖、玄武湖"
#
#
# view_names = a.split('、')
#
# for i,name in enumerate(view_names):
#     scenes = Scenes()
#     scenes.view_name = name
#     scenes.view_image = image_list[i]
#     scenes.view_title = '体味浓郁的伊斯兰特色'
#     scenes.view_score = random.randint(1,6)
#     scenes.view_spot = '雕梁画栋小经筒馏金宝瓶'
#     print('************')
#     scenes.view_category_id = 7
#     scenes.view_introduce = '规模日臻宏大，建造雄奇，具有我国古典建筑和民族风格的建筑特点，雕梁彩檐、金碧辉煌'
#     scenes.view_location = '西北地区 青海省 西宁市'
#     scenes.view_describe = '大殿内宽敞，殿内和整个大寺处处都显得古朴雅致，是我国西北地区伊斯兰教的最高学府。寺院宽敞，平时可容三千人礼拜，最多达万人。'
#     scenes.save()
    # scenes.view_describe = """主要景点：

# 明清商业街
# 是徽饶古商道上最为繁华的商业街之一，全长一千多米，分为上街头、中街头、下街头三部分。整条街共有上百幢店铺，鳞次栉比地分布在街道两旁，大部分保存得非常完好。窑里曾有民谣这样描述这条街：“上街头，下街头，街长不见头；丝绸缎，糖醋油，店面八百九”，生动的再现了唐诗中“浮梁歙州，万国来求”盛世景象。
# 程氏宗祠
# 又名“惇睦”堂，背靠狮山，面临瑶河，始建于明代中叶，清代道光年间重新整修过。由于风水的缘故，其建筑风格不同于其他祠堂，上、中、下三堂的朝向各不相同。建筑内砖雕、石雕和木雕的题材丰富、玲珑剔透、层次分明、栩栩如生，显示了雕刻工匠高超的艺术才能。一九三八年初，开国元帅陈毅同志来瑶里主持新四军改编，曾在祠堂内召开抗日动员大会。
# 狮冈胜览
# 建于清代，是一幢中西合璧的徽派合院式民居建筑，融高雅、简洁、富丽为一体，整个建筑精美如诗。内部的梁门、窗上有一百多幅木雕，题材均取材于中国古代名著和戏文，具有深厚的文化内涵和极高的艺术价值。
# 宏毅祠
# 是吴家祠堂的分祠，是吴氏分支进行祭祀祖先和从事其它宗族活动的地方。一九三八年初，参加瑶里新四军改编的红军游击队曾驻扎此地，进行文化和纪律教育。现为江西省级文物保护单位。
# 陈毅旧居
# 是老一辈无产阶级革命家、开国元帅陈毅同志1937年-1938年来到瑶里指导新四军的改编工作生活过的地方。现为陈毅图片展览馆，集中介绍了新四军瑶里改编的过程和陈毅同志的简要生平，是一处人们接受革命传统教育和革命先辈思想熏陶的场所。
# 张氏宗祠
# 张氏宗祠始建于唐末，元末焚于战火，现存宗祠兴建于明初。宗祠气势恢宏，拥有三堂两天井，占地1999平方米，祠内砖、木、石雕十分精细。宗祠前有一月形水塘，而且旁边还修有两个一样的水塘。这与风水有关，对面是“火焰山”，由于张氏宗祠正对火焰山，故经常遭火灾，在风水先生的指导下建立。
# 复源桥
# 明朝时期所建造，是当年从徽州（安徽）至饶州（江西）古道必经之桥。走上它，便可遐想起 “枯藤老树昏鸦，小桥流水人家，古道西风瘦马，夕阳西下，断肠人在天涯” 古诗中的意境。
# [徽饶古道]历来是古徽州通往饶州的交通要道，昔日徽商享誉大江南北，徽州古道功不可没。此古道从梅岭村前的河对岸一直通向贯穿虎头山，连接皖赣两省，10公里，宽三尺，进入安徽可到休宁、屯溪，全部由麻石铺砌而成。踏着蜿蜒古朴的山道，观赏着苍劲古木，葱翠竹海，倾听着宁静之中的声声鸟鸣，别有一番情趣。
# 绕南陶瓷
# 绕南陶瓷主题园区按照以旧修旧的原则复建了釉果手工作坊、陶瓷手工
# 作坊、龙窑遗址、水碓小世界等陶瓷文化遗址，让人们可觅远古瓷韵，感悟这里厚重的历史文化沉淀和古代劳动人民质朴的生活。
# 高际禅林寺坐落于江西省浮梁县瑶里镇境内，海拔1681.4米的五股尖半山腰，其建筑面积最盛时期达9000多平方米，现存建筑面积1200多平方米，是始建于宋代时期的赣东北著名寺庙。
# 高岭国家矿山公园
# 高岭国家矿山公园的核心是高岭古采矿遗址，位于瓷都景德镇市东北部浮梁县瑶里镇高岭村。矿物主要是用于陶瓷生产的瓷土矿石。1965年后，高岭山的瓷土矿经数百年的开采后停产。昔日曾经轰轰烈烈的采矿场---高岭山，只剩下一些供人凭吊的采掘遗迹。
#
# 交通指南
#
# 瑶里自驾游指南
# 过瑶湖大桥，走昌万公路，过军山湖，过余干，直奔景德镇，从浮梁县穿过到瑶里古镇。
# 瑶里公共交通指南
# 到景德镇后，去里村短途汽车站乘坐从“景德镇-瑶里古镇”的班车。每天两班，早上7：30从景德镇出发，9：00左右到景德镇瑶里古镇；下午2：00从景德镇出发，4：00左右到瑶里古镇车站东北方向2.5公里（在火车站乘K3路公交车往东终点站）；乘车上山的天外村登山口在火车站正北约2公里（在火车站乘3路公交车往西终点站）；桃花源登山口在泰山西麓，距泰山火车站约12公里（在火车站乘18路公交车往西到终点站）；天烛峰进山口在泰山东麓，距泰山火车站约18公里。K3路是一条便捷的旅游线路，两头的终点站分别是红门和天外村，都是登山的入口，红门是步行线，天外村是汽车线，不要坐反！泰安老火车站叫泰山站，位于市中心偏南。新的高铁站叫泰安站，位于西部新区，坐17路，18路，K37路可以到达市区。从泰山火车站前往以上介绍的几处登山口最为方便，均有公交车或旅游公交车直通。泰山火车站是泰山旅游交通的中心枢纽，泰安的几处汽车站也在火车站周围，所以建议不熟悉泰山旅游交通的游客，到达泰安后都先去火车站（城区大部分公交都通往火车站，车票一元或两元），然后分乘各路车去往不同的进山口或景区。
# """

