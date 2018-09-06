#import pygame
#pygame.init()
#zhanshi=["孙策","狂铁","裴擒虎","苏烈","凯","哪吒","雅典娜","杨戬","钟馗","刘备","孙悟空","亚瑟","橘右京","花木兰","韩信","露娜","关羽","老夫子","达摩","李白","宫本武藏","典韦","曹操","夏侯惇","吕布","钟无艳","赵云"]
#fashi=["司马懿","米莱狄","弈星","杨玉环","女娲","梦奇","干将莫邪","诸葛亮","钟馗","不知火舞","张良","王昭君","姜子牙","露娜","安琪拉","貂蝉","武则天","甄姬","周瑜","芈月","扁鹊","孙膑","高渐离","嬴政","妲己","墨子","小乔"]
#cike=["元歌","裴擒虎","百里玄策","百里守约","孙悟空","橘右京","娜可露露","不知火舞","花木兰","兰陵王","韩信","貂蝉","李白","阿轲","赵云"]
#tanke=["孙策","梦奇","苏烈","凯","东皇太一","张飞","牛魔","刘邦","程咬金","关羽","项羽","达摩","夏侯惇","吕布","芈月","白起","钟无艳","刘禅","庄周","墨子","廉颇"]
#sheshou=["公孙离","百里守约","黄忠","成吉思汗","虞姬","李元芳","后羿","狄仁杰","马可波罗","鲁班七号","孙尚香"]
#fuzhu=["杨玉环","明世隐","鬼谷子","大乔","太乙真人","蔡文姬","张飞","牛魔","刘邦","扁鹊","孙膑","庄周"]
#heroes=list(set(zhanshi+fashi+cike+tanke+sheshou+fuzhu))
###background=pygame.image.load("1.jpg")
##h0=pygame.image.load(f"image/{tanke[0]}.jpg")
#QWHITE=(200,200,200)
#RED=(255,0,0)
#font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",26)
#all_text=font.render("全部",True,QWHITE)
#tanke_text=font.render("坦克",True,QWHITE)
#zhanshi_text=font.render("战士",True,QWHITE)
#cike_text=font.render("刺客",True,QWHITE)
#fashi_text=font.render("法师",True,QWHITE)
#sheshou_text=font.render("射手",True,QWHITE)
#fuzhu_text=font.render("辅助",True,QWHITE)
#
#screen=pygame.display.set_mode((800,600))
#
#while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            exit()
#    #screen.blit(background,(0,0))
#    screen.blit(all_text,(70,50))
#    screen.blit(tanke_text, (170, 50))
#    screen.blit(zhanshi_text, (270, 50))
#    screen.blit(cike_text, (370, 50))
#    screen.blit(fashi_text, (470, 50))
#    screen.blit(sheshou_text, (570, 50))
#    screen.blit(fuzhu_text, (670, 50))
#
#    mx,my = pygame.mouse.get_pos()
#    if 70 < mx<70+26+13+26 and \
#        50<my<50+26:
#        #print("您进入全部区域")
#        all_text = font.render("全部", True, RED)
#        #screen.blit(h0,(70,100))
#    else:
#        all_text = font.render("全部", True, QWHITE)
#    if 170<mx<170+26+13+26 and \
#        50<my<50+26:
#        tanke_text = font.render("坦克", True, RED)
#    else:
#        tanke_text = font.render("坦克", True, QWHITE)
#
#    if 270<mx<270+26+13+26 and \
#        50<my<50+26:
#        zhanshi_text = font.render("战士", True, RED)
#    else:
#        zhanshi_text = font.render("战士", True, QWHITE)
#
#
#    pygame.display.update()

