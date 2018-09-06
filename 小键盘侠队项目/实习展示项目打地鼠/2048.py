import pygame
import random
pygame.init()
pygame.mixer.init()

# 画线
def drawline(screen,color,hole):
    pygame.draw.line(screen, color, (35, 40), (565, 40), 10)
    pygame.draw.line(screen, color, (35, 170), (565, 170), 10)
    pygame.draw.line(screen, color, (35, 300), (565, 300), 10)
    pygame.draw.line(screen, color, (35, 430), (565, 430), 10)
    pygame.draw.line(screen, color, (35, 560), (565, 560), 10)
    pygame.draw.line(screen, color, (40, 35), (40, 565), 10)
    pygame.draw.line(screen, color, (170, 35), (170, 565), 10)
    pygame.draw.line(screen, color, (300, 35), (300, 565), 10)
    pygame.draw.line(screen, color, (430, 35), (430, 565), 10)
    pygame.draw.line(screen, color, (560, 35), (560, 565), 10)
    screen.blit(hole,(45,45))
    screen.blit(hole, (45, 175))
    screen.blit(hole, (45, 305))
    screen.blit(hole, (45, 435))
    screen.blit(hole, (175, 45))
    screen.blit(hole, (175, 175))
    screen.blit(hole, (175, 305))
    screen.blit(hole, (175, 435))
    screen.blit(hole, (305, 45))
    screen.blit(hole, (305, 175))
    screen.blit(hole, (305, 305))
    screen.blit(hole, (305, 435))
    screen.blit(hole, (435, 45))
    screen.blit(hole, (435, 175))
    screen.blit(hole, (435, 305))
    screen.blit(hole, (435, 435))


# 导入图片
screen=pygame.display.set_mode((600,600))
background=pygame.image.load("image/background.jpg")
background2=pygame.image.load("image/background2.jpg")
background3=pygame.image.load("image/background3.jpg")
dishu=pygame.image.load("image/1.png")
dishu=pygame.transform.scale(dishu,(100,100))
dishu2=pygame.image.load("image/dishu2.jpg")
chuizi=pygame.image.load("image/2.png")
chuizi2=pygame.image.load("image/3.png")
start=pygame.image.load("image/start.png")
gameover2=pygame.image.load("image/gameover2.jpg")
gamewin2=pygame.image.load("image/gamewin2.jpg")
hole=pygame.image.load("image/hole.jpg")
# level_1=pygame.image.load("level1.jpg")
# level_2=pygame.image.load("level2.jpg")
# level_3=pygame.image.load("level3.jpg")
# 导入音乐wav
# music=pygame.mixer.Sound("music.ogg")
musicwin=pygame.mixer.Sound("music/musicwin.ogg")
pygame.mixer.music.load("music/music.ogg")
bingo=pygame.mixer.Sound("music/bingo.wav")
gamewin=pygame.mixer.Sound("music/gamewin.wav")
# pygame.mixer.music.load("music.mp3")
# 设置颜色
GREY=(192,192,192)
RED=(255,0,0)
BLACK=(0,0,0)
ORANGE=(255,128,0)
# 列表
linex=[45,175,305,435]
liney=[45,175,305,435]
# 变量
dishux=0
dishuy=0
dishux2=0
dishuy2=0
dishux3=0
dishuy3=0
jishuqi=0
czchange=1
score=0
start_flag=0
jishuqi2=0
level1=5
level2=15
level3=30
level=0
# 文字
font30=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",30)
font50=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",50)
level_1=font50.render("简 单",True,RED)
level_2=font50.render("中 等",True,RED)
level_3=font50.render("困 难",True,RED)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            czchange=0
        else:
            czchange=1
    if start_flag==0:
        # music.play()
        pygame.mixer.music.play()
        screen.blit(background3,(0,0))
        screen.blit(start,(200,80+20))
        screen.blit(level_1,(230,190+30))
        screen.blit(level_2,(230,270+30))
        screen.blit(level_3,(230,350+30))
    m1,m2,m3=pygame.mouse.get_pressed()
    mx,my=pygame.mouse.get_pos()
    if m1:
        if mx in range(200,415) and my in range(100,200):
            start_flag=1
        if mx in range(230,430) and my in range(220,280):
            level=level1
        if mx in range(230,430) and my in range(300,360):
            level =level2
        if mx in range(230,430) and my in range(380,440):
            level=level3
    if start_flag:# 三只松鼠随机位置出现
        screen.blit(background2,(0,0))
        screen.blit(background, (35, 35))
        drawline(screen, GREY,hole)
        jishuqi+=1
        a = random.randint(0, 3)
        b = random.randint(0, 3)
        c = random.randint(0, 3)
        d = random.randint(0, 3)
        e = random.randint(0, 3)
        f = random.randint(0, 3)
        if a==c and b==d:
            a = random.randint(0, 3)
            b = random.randint(0, 3)
            c = random.randint(0, 3)
            d = random.randint(0, 3)
        if a == e and b == f:
            a = random.randint(0, 3)
            b = random.randint(0, 3)
            e= random.randint(0, 3)
            f = random.randint(0, 3)
        if c == e and d == f:
            e = random.randint(0, 3)
            f = random.randint(0, 3)
            c = random.randint(0, 3)
            d = random.randint(0, 3)
        if jishuqi==10:
           dishux=linex[a]
           dishuy=liney[b]
        if jishuqi==30:
           dishux2 = linex[c]
           dishuy2 = liney[d]
        if jishuqi==50:
           dishux3 = linex[e]
           dishuy3 = liney[f]
        if 10<jishuqi<60:
            screen.blit(dishu,(dishux+10,dishuy))
            if czchange==0:
                if int(mx) in range(dishux+10,dishux+120) and\
                        int(my) in range(dishuy,dishuy+120):
                    bingo.play()
                    dishux=-200
                    dishuy=-200
                    score+=1
        if 30<jishuqi<80:
            screen.blit(dishu, (dishux2+10, dishuy2))
            if czchange==0:
                if int(mx) in range(dishux2+10,dishux2+120) and\
                        int(my) in range(dishuy2,dishuy2+120):
                    bingo.play()
                    dishux2 = -200
                    dishuy2 = -200
                    score += 1
        if 50<jishuqi<100:
            screen.blit(dishu, (dishux3+10, dishuy3))
            if czchange==0:
                if int(mx) in range(dishux3+10,dishux3+120) and\
                        int(my) in range(dishuy3,dishuy3+120):
                    bingo.play()
                    dishux3 = -200
                    dishuy3 = -200
                    score += 1
        if jishuqi==110:
            jishuqi=0
            jishuqi2+=1
        # 放锤子
        mx,my=pygame.mouse.get_pos()
        if czchange:
            screen.blit(chuizi,(mx-48,my-48))
        if czchange==0:
            screen.blit(chuizi2,(mx-48,my-48))
        # 敲地鼠，地鼠消失并且得分
        text = font30.render("您的得分是：%d" % score, True, BLACK)
        screen.blit(text,(5,5))
    # 游戏结束
    if jishuqi2==10:
        if score<level:
            start_flag=0
            screen.blit(gameover2,(0,0))
            text2 = font30.render("您的得分是：%d" % score, True, ORANGE)
            screen.blit(text2,(200,20))
        else:
            start_flag = 0
            screen.blit(gamewin2, (0, 0))
            text3 = font30.render("您的得分是：%d" % score, True, ORANGE)
            screen.blit(text3, (200, 50))
            gamewin.play()
    pygame.display.update()



















