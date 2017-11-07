from django.test import TestCase
from .models import *
import random

image_list = [
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
 'daguanlou.jpg'
 'jingsiyuan.jpg',
 'gulianhuachi.jpg',
 'shizilin.jpg',
 'tongluowan.jpg',
 'donghu.jpg',
 'xihu.jpg',
 'weiminghu.jpg',
 'qinghaihu.jpg',
 'tiananmenchenglou.jpg',
 'yueyanglou.jpg',
 'yuejianglou.jpg',
 'yueyalou.jpg',
 'tengwangge.jpg',
 'kejiatulou.jpg',
 'yanyulou.jpg',
 'tengwangge.jpg',
 'kejiatulou.jpg',
 'yanyulou.jpg',
 'daguanlou.jpg'
 'jingsiyuan.jpg',
 'gulianhuachi.jpg',
 'shizilin.jpg',
 'tongluowan.jpg',
 'donghu.jpg']
# for i in range(1, 20):
#     for i in image_list:
#         img = AlbumImage()
#         img.image_album_id = int(random.randint(1, 20))
#         img.image = i
#         img.save()

# photo_list = ['u1.jpg', 'u2.jpg', 'u3.jpg', 'u4.jpg', 'u5.jpg']
#
# users = User.objects.all()
# print('-----', len(users[1:]))
# for i,u in enumerate(users[1:]):
#     u.user_photo = photo_list[i]
#     u.save()

# a = "太湖风光、江南水乡、西湖、阅江楼、烟雨楼、青海湖、月牙楼、云龙湖、东湖、西湖、阅江楼、烟雨楼、青海湖、月牙楼、云龙湖、东湖、玄武湖、阅江楼、烟雨楼、青海湖、月牙楼、云龙湖、东湖、玄武湖"
# view_names = a.split('、')
# name = UserAlbum.objects.all()
# for i,n in enumerate(name):
#     n.album_name = view_names[i]
#     n.save()







#
# s = ['薄荷街的香草先生', '海蓝了夏迷了眼睛', '青春谁作伴']
# users = User.objects.all()
# for i,u in enumerate(users[3:]):
#     u.signature = s[i]
#     u.save()
#
# con = ['以其秀丽的湖光山色和众多的名胜古迹而成为闻名中外的旅游胜地。西湖是目前中国列入《世界遗产名录》的世界遗产中唯一一处湖泊类文化遗产。',
# '颐和园是我国现存规模最大，保存最完整的皇家园林。它原是清朝帝王的行宫和花园，以杭州西湖风景为蓝本，汲取江南园林的某些设计手法和意境而建成的一座大型天然山水园。']
#
# content = TravelNotes.objects.all()[:2]
# for i,cont in enumerate(content):
#     cont.content_short = con[i]
#     cont.save()




# note_list = TravelNotes.objects.all()
# for i,note in enumerate(note_list):
#     note.travel_image = image_list[i]
#     note.save()
#
#
# photo = AlbumImage.objects.all()
# for i,image in enumerate(photo):
#     image.image = image_list[i]
#     image.save()





# info = Information.objects.get(id=2)
# info.info_title = '走进婺源，邂逅春天'
# info.info_image = './infowuyuan1.jpeg'
# info.info_user = '管理员'
# info.info_look = 78
# info.info_content = """景区信息
# 扬州，古称广陵、江都、维扬，建城史可上溯至公元前486年[1]  ，是江苏省地级市，地处江苏中部、长江与京杭大运河交汇处，有“淮左名都，竹西佳处”之称，又有着“中国运河第一城”的美誉；被誉为扬一益二、淮南第一州、月亮城 。
# 扬州是江苏长江经济带重要组成部分、南京都市圈成员城市和长三角城市群城市，是南水北调东线工程水源地。下辖邗江区、广陵区、江都区3个市辖区和宝应县1个县，代管高邮市、仪征市2个县级市，是联合国人居奖获奖城市、全国文明城市、中国温泉名城。
# 扬州是首批国家历史文化名城。历史上，扬州因其优越的地理位置，自汉至清几乎经历了通史式的繁荣，并伴随着文化的兴盛。扬州在历史上有曾有过三次鼎盛：第一次是在西汉中叶；第二次是在隋唐到赵宋时期；第三次是在明清时期。总体上，扬州城市的繁荣总是和国家的盛世重合。历史上繁华的扬州城，即今扬州市老城区——广陵区。
# 景点
# 扬州位于中国东南，江苏中部，是名副其实的交通枢纽，如今是集工商、科教、旅游、生态为一体的地域中心城市。扬州旅游资源丰富，名胜古迹众多。清代扬州曾有“园林甲天下”之誉，至今还保留着许多优秀的古典园林，如瘦西湖、大明寺、个园、何园等为扬州最著名的旅游景点。当然扬州的美食也不容错过，包括“富春”、“五亭”牌速冻包子，“三和四美”牌酱菜，牛皮糖，扬州 “三把刀”(理发刀、修脚刀、厨刀），高邮双黄蛋等。"""
# print('------11')
# info.save()
#
# for i in range(3, 8):
#     album = UserAlbum.objects.get(id=int(i))
#     # album.album_user_id = int(i)
#     album.album_name = '太湖风光'
#     album.album_short = '碧水辽阔，烟波浩淼'
#     album.album_look = 20
#     album.save()

# 10-13

#
# for i in range(20, 21):
#     image = AlbumImage()
#     image.image_album_id = int(i)
#     image.image = './dahufenfguang.jpg'
#     image.save()
#
# image = AlbumImage.objects.get(id=10)
# image.image = './dahufenfguang.jpg'
# image.save()


# for i in range(3, 5):
#     note = TravelNotes.objects.get(id=int(i))
#     note.notes_look = 56
#     note.travel_image = './lijiang.jpg'
#     note.save()






