import pygame
import random

pygame.init()  # 初始化
pygame.mixer.init()
pygame.mouse.set_visible(0)  # 鼠标指针隐藏
Music = pygame.mixer.music.load("CTAG.mp3")
pygame.mixer.music.play(-1)  # 循环播放
shoot = pygame.mixer.Sound("shoot.ogg")
screen = pygame.display.set_mode((1000, 500))

start = pygame.image.load("start.png")
background = pygame.image.load("jungle2.jpg")
cloud = pygame.image.load("cloud.png")
hand = pygame.image.load("hand.png")
hand2 = pygame.image.load("hand2.png")
mute = pygame.image.load("mute.png")
play = pygame.image.load("play.png")

font = pygame.font.Font("C:\Windows\Fonts\msyh.ttc", 30)

# 怪物目标
target1 = pygame.image.load("m1.png")
target2 = pygame.image.load("m2.png")
target3 = pygame.image.load("m3.png")
target4 = pygame.image.load("m4.png")
targetsize = 72

# 导入狙击镜
sniper = pygame.image.load("jjj2.png")
snp_rect = sniper.get_rect()
snpH = snp_rect.height
snpW = snp_rect.width

fenshu = 0  # 分数初始化
number = 2  # 怪物数量
f = 0  # 开镜事件计数器
f1 = 0  # 开始界面事件计数器
f2 = 0  # 音乐事件计数器

stx, sty = 0, 0  # 开始界面坐标

cx1, cy1 = 50, 50  # 云坐标初始化
cx2, cy2 = 400, 50
cx3, cy3 = 750, 50

ty1, ty2, ty3, ty4 = -80, -80, -80, -80  # 开始界面怪物纵坐标
# 怪物的数量
lx1 = []
ly1 = []
for i in range(number):
    x1, y1 = random.randint(0, 923), random.randint(350, 428)
    lx1.append(x1)
    ly1.append(y1)

lx2 = []
ly2 = []
for i in range(number):
    x2, y2 = random.randint(0, 923), random.randint(120, 278)
    lx2.append(x2)
    ly2.append(y2)

lx3 = []
ly3 = []
for i in range(number):
    x3, y3 = random.randint(0, 923), random.randint(350, 428)
    lx3.append(x3)
    ly3.append(y3)

lx4 = []
ly4 = []
for i in range(number):
    x4, y4 = random.randint(0, 923), random.randint(20, 48)
    lx4.append(x4)
    ly4.append(y4)

# 速度属性
sp = 0
ls = []

for i in range(number):
    j = random.randint(-4, 4)
    if j == 0:
        j = random.randint(-4, 4)
    ls.append(j)

while True:
    mx, my = pygame.mouse.get_pos()
    m1, m2, m3 = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # 击中检测
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if 950 < mx-7 < 990 and 0 < my < 42:
                f2 += 1
            if 800 < mx-7 < 945 and 320 < my < 360:
                f1 = 1
            if 830 < mx-7 < 920 and 220 < my < 250:
                f2 += 1
            # 怪物的集中检测
            for i in range(number):
                if f == 1:
                    shoot.play()
                    if lx1[i] < mx < lx1[i]+targetsize:
                        if ly1[i] < my < ly1[i]+targetsize:
                            fenshu += 1
                            lx1[i] = -100
                            ly1[i] = random.randint(350, 428)
                            ls[i] = random.randint(-4, 4)
                            if ls[i] == 0:
                                ls[i] = random.randint(-4, 4)
                    if lx2[i] < mx < lx2[i]+targetsize:
                        if ly2[i] < my < ly2[i]+targetsize:
                            fenshu += 1
                            lx2[i] = -100
                            ly2[i] = random.randint(120, 278)
                            ls[i] = random.randint(-4, 4)
                            if ls[i] == 0:
                                ls[i] = random.randint(-4, 4)
                    if lx3[i] < mx < lx3[i]+targetsize:
                        if ly3[i] < my < ly3[i]+targetsize:
                            lx3[i] = -100
                            ly3[i] = random.randint(350, 428)
                            fenshu += 1
                            ls[i] = random.randint(-4, 4)
                            if ls[i] == 0:
                                ls[i] = random.randint(-4, 4)
                    if lx4[i] < mx < lx4[i]+targetsize:
                        if ly4[i] < my < ly4[i]+targetsize:
                            lx4[i] = -100
                            ly4[i] = random.randint(20, 48)
                            fenshu += 1
                            ls[i] = random.randint(-4, 4)
                            if ls[i] == 0:
                                ls[i] = random.randint(-4, 4)

    screen.blit(background, (0, 0))
    if f == 0:
        screen.blit(hand2, (mx - 7, my))
    # 云
    cx1 += 0.5
    screen.blit(cloud, (cx1, cy1))
    if cx1 > 1000:
        cx1 = -250

    cx2 += 0.5
    screen.blit(cloud, (cx2, cy2))
    if cx2 > 1000:
        cx2 = -250

    cx3 += 0.5
    screen.blit(cloud, (cx3, cy3))
    if cx3 > 1000:
        cx3 = -250
    # 控制怪物
    for i in range(number):
        x1 = lx1[i]
        y1 = ly1[i]
        lx1[i] += ls[i]
        if lx1[i] > 1050:
            lx1[i] = -20
        if lx1[i] < -72:
            lx1[i] = 1020
        screen.blit(target1, (x1, y1))

        x2 = lx2[i]
        y2 = ly2[i]
        lx2[i] += ls[i]
        if lx2[i] > 1050:
            lx2[i] = -20
        if lx2[i] < -72:
            lx2[i] = 1020
        screen.blit(target2, (x2, y2))

        x3 = lx3[i]
        y3 = ly3[i]
        lx3[i] += ls[i]
        if lx3[i] > 1050:
            lx3[i] = -20
        if lx3[i] < -72:
            lx3[i] = 1020
        screen.blit(target3, (x3, y3))

        x4 = lx4[i]
        y4 = ly4[i]
        lx4[i] += ls[i]
        if lx4[i] > 1050:
            lx4[i] = -20
        if lx4[i] < -72:
            lx4[i] = 1020
        screen.blit(target4, (x4, y4))
    # 控制射击
    sx, sy = mx - 998, my - 572
    if m3:
        f = 1
    if f == 1:
        screen.blit(sniper, (sx, sy))
        score = font.render(f"Score：{fenshu}", True, (255, 255, 255))
    if m2:
        f = 0
    # 分数
    score = font.render(f"Score：{fenshu}", True, (0, 0, 0))
    screen.blit(score, (0, 0))

    # 控制开始界面
    if f1 == 0:
        screen.blit(start, (stx, sty))
        screen.blit(target1, (435, ty1))
        if ty1 < 205:
            ty1 += 2
        screen.blit(target2, (290, ty2))
        if ty2 < 300:
            ty2 += 2
        screen.blit(target3, (590, ty3))
        if ty3 < 300:
            ty3 += 2
        screen.blit(target4, (145, ty4))
        if ty4 < 205:
            ty4 += 2
        screen.blit(hand, (mx-7, my))
    if f1 == 1:
        if f2 == 1:
            screen.blit(mute, (940, 0))
        if f2 == 2:
            screen.blit(play, (949, 0))
        screen.blit(start, (1005, 505))
    # 控制声音播放
    if f2 == 0:
        screen.blit(play, (949, 0))
        pygame.mixer.music.unpause()
    if f2 == 1:
        screen.blit(mute, (940, 0))
        pygame.mixer.music.pause()
    if f2 == 2:
        f2 = 0

    pygame.display.update()
