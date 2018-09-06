import pygame
pygame.init()
import random
pygame.mixer.init()
pygame.mixer.music.load("1/background_music.ogg")
pygame.mixer.music.play(loops=1000, start=0.0)
screen = pygame.display.set_mode((1000, 600))
sc = pygame.image.load("1/game_cover3.jpg")
fm = pygame.image.load("1/fm.jpg")
kstp = pygame.image.load("1/kstp.jpg")
font = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 30)
font2 = pygame.font.Font("C:\Windows\Fonts\SimHei.ttf", 20)
zk = pygame.image.load("1/zhuankuai2.png")
wdzk = pygame.image.load("1/zhuankuai4.png")
jsyxtb = pygame.image.load("1/jsyxtb.png")
thtp = pygame.image.load("1/thtp.png")
pmtp = pygame.image.load("1/pmtp.png")
cxks = pygame.image.load("1/cxks.png")
qrtp = pygame.image.load("1/qrtp.png")
drms = pygame.image.load("1/daren.png")
taitou = pygame.image.load("1/taitou.jpg")
fsyp = pygame.mixer.Sound("1/button.wav")
jsyp = pygame.mixer.Sound("1/enemy3_down.wav")
wjycg = pygame.mixer.Sound("1/655.wav")
wjecg = pygame.mixer.Sound("1/4951.wav")
hhs = pygame.mixer.Sound("1/10049.wav")
tkl = pygame.image.load("1/黄金圣斗士l.png")
tkr = pygame.image.load("1/黄金圣斗士r.png")
tku = pygame.image.load("1/黄金圣斗士u.png")
tkd = pygame.image.load("1/黄金圣斗士d.png")
djtkl = pygame.image.load("1/黑色闪电l.png")
djtkr = pygame.image.load("1/黑色闪电r.png")
djtku = pygame.image.load("1/黑色闪电u.png")
djtkd = pygame.image.load("1/黑色闪电d.png")
bthl = pygame.image.load("1/霸天虎l.png")
bthr = pygame.image.load("1/霸天虎r.png")
bthu = pygame.image.load("1/霸天虎u.png")
bthd = pygame.image.load("1/霸天虎d.png")
hzzl = pygame.image.load("1/红蜘蛛l.png")
hzzr = pygame.image.load("1/红蜘蛛r.png")
hzzu = pygame.image.load("1/红蜘蛛u.png")
hzzd = pygame.image.load("1/红蜘蛛d.png")
zd = pygame.image.load("1/bullet.png")
zd = pygame.transform.scale(zd, (10, 10))
zk = pygame.transform.scale(zk, (50, 50))
drms = pygame.transform.scale(drms, (200, 50))
djtkl = pygame.transform.scale(djtkl, (50, 50))
djtkr = pygame.transform.scale(djtkr, (50, 50))
djtku = pygame.transform.scale(djtku, (50, 50))
djtku1 = pygame.transform.scale(djtku, (200, 200))
tku1 = pygame.transform.scale(tku, (200, 200))
bthu1 = pygame.transform.scale(bthu, (200, 200))
hzzu1 = pygame.transform.scale(hzzu, (200, 200))
taitou = pygame.transform.scale(taitou, (300, 250))
djtkd = pygame.transform.scale(djtkd, (50, 50))
tkl = pygame.transform.scale(tkl, (50, 50))
tkr = pygame.transform.scale(tkr, (50, 50))
tku = pygame.transform.scale(tku, (50, 50))
tkd = pygame.transform.scale(tkd, (50, 50))
bthl = pygame.transform.scale(bthl, (50, 50))
bthr = pygame.transform.scale(bthr, (50, 50))
bthu = pygame.transform.scale(bthu, (50, 50))
bthd = pygame.transform.scale(bthd, (50, 50))
hzzl = pygame.transform.scale(hzzl, (50, 50))
hzzr = pygame.transform.scale(hzzr, (50, 50))
hzzu = pygame.transform.scale(hzzu, (50, 50))
hzzd = pygame.transform.scale(hzzd, (50, 50))
xztk = font.render("玩家一请选择你的坦克，数字键选择，backpace确认你的选择", True, (0, 255, 255))
xztk2 = font.render("玩家二请选择你的坦克，F键选择，space确认你的选择", True, (255, 255, 255))
hjsdsjs = font2.render("玩家一选择黄金圣斗士，敏捷加2", True, (255, 255, 0))
djatmjs = font2.render("玩家一选择黑色闪电，子弹速度加3", True, (255, 255, 0))
bthjs = font2.render("玩家一选择土豪ZZ式，敏捷加2，子弹速度加5", True, (255, 255, 0))
hzzjs = font2.render("玩家一选择红蜘蛛，没啥特长，就是霸气", True, (255, 255, 0))
hjsds = [tkl, tkr, tkd, tku, djtkl, djtkr, djtkd, djtku, bthl, bthr, bthd, bthu, hzzl, hzzr, hzzd, hzzu]
tkjs = [hjsdsjs, djatmjs, bthjs, hzzjs]
tkzs = [tku1, djtku1, bthu1, hzzu1]
tkzs1 = [tku, djtku, bthu, hzzu]
hjsdsjs2 = font2.render("玩家二选择黄金圣斗士，敏捷加2", True, (255, 255, 0))
djatmjs2 = font2.render("玩家二选择黑色闪电，子弹速度加3", True, (255, 255, 0))
bthjs2 = font2.render("玩家二选择土豪ZZ式，敏捷加2，子弹速度加5", True, (255, 255, 0))
hzzjs2 = font2.render("玩家二选择红蜘蛛，没啥特长，就是霸气", True, (255, 255, 0))
hjsds2 = [tkl, tkr, tkd, tku, djtkl, djtkr, djtkd, djtku, bthl, bthr, bthd, bthu, hzzl, hzzr, hzzd, hzzu]
tkjs2 = [hjsdsjs2, djatmjs2, bthjs2, hzzjs2]
tkzs2 = [tku1, djtku1, bthu1, hzzu1]
tkzs12 = [tku, djtku, bthu, hzzu]

tkx = 500 - 100
tky = 300 - 250
fx = 0
hjzdx = [1000, -1000, 1000, 1000]
hjzdy = [1000, 1000, -1000, 1000]
zdfx = [0, 0, 0, 0]
tkx2 = 500 - 100
tky2 = 300
fx2 = 0
hjzdx2 = [1000, -1000, 1000, 1000]
hjzdy2 = [1000, 1000, -1000, 1000]
zdfx2 = [0, 0, 0, 0]
a = 4
zdsd = 7
e, b, c, d, f = 0, 1, 2, 3, 0
a2 = 4
zdsd2 = 7
e2, b2, c2, d2, f2 = 0, 1, 2, 3, 0
ks = 0
ks2 = 0
zkx = []
zky = []
fen1 = 0
fen2 = 0
ksyx = 0
ksyx2 = 0
jsyx = 0
jsyxx = -600
jfks = 0
kaka = 0
list = [0, 1, 2, 3, 4]
cxksx = 1000
tkbz = 0

hxbd = 0
dr = 0
drjs = 0
for i in range(100):
    zkxx = random.randint(0, 20) * 50
    zkyy = random.randint(1, 10) * 50
    zkx.append(zkxx)
    zky.append(zkyy)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(sc, (0, 0))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1 and ks == 0:  # 选择坦克
            e, b, c, d, f = 0, 1, 2, 3, 0
            a = 4
            zdsd = 5
        if event.key == pygame.K_2 and ks == 0:
            e, b, c, d, f = 4, 5, 6, 7, 1
            a = 2
            zdsd = 10
        if event.key == pygame.K_3 and ks == 0:
            e, b, c, d, f = 8, 9, 10, 11, 2
            a = 4
            zdsd = 10
        if event.key == pygame.K_4 and ks == 0:
            e, b, c, d, f = 12, 13, 14, 15, 3
            a = 2
            zdsd = 5
        if event.key == pygame.K_BACKSPACE and ks == 0 and ksyx == 1:
            wjycg.play()
            ks = 1
        if event.key == pygame.K_BACKSPACE and ks == 0 and hxbd == 1:
            wjycg.play()
            ks = 1
            dr = 1
        if event.key == pygame.K_ESCAPE and hxbd == 1:
            drjs = 1
        if event.key == pygame.K_F1 and ks2 == 0:  # 选择坦克
            e2, b2, c2, d2, f2 = 0, 1, 2, 3, 0
            a2 = 4
            zdsd = 5
        if event.key == pygame.K_F2 and ks2 == 0:
            e2, b2, c2, d2, f2 = 4, 5, 6, 7, 1
            a2 = 2
            zdsd2 = 10
        if event.key == pygame.K_F3 and ks2 == 0:
            e2, b2, c2, d2, f2 = 8, 9, 10, 11, 2
            a2 = 4
            zdsd2 = 10
        if event.key == pygame.K_F4 and ks2 == 0:
            e2, b2, c2, d2, f2 = 12, 13, 14, 15, 3
            a2 = 2
            zdsd2 = 5
        if event.key == pygame.K_SPACE and ks2 == 0 or dr == 1:
            if ksyx == 1:
                wjecg.play()
            ks2 = 1

        if ks == 1 and ks2 == 1 and kaka == 0:
            tkx = 0
            tky = 0
            tkx2 = 1000 - 50
            tky2 = 600 - 50
            kaka += 1

        if ks == 1 and ks2 == 1:
            if event.key == pygame.K_LEFT:  # fx和fx2表示坦克方向，
                fx = 1  # 1,-1,2,-2 分别表示 l,r,d,u
            if event.key == pygame.K_RIGHT:  # -1
                fx = -1
            if event.key == pygame.K_DOWN:  # 2
                fx = 2
            if event.key == pygame.K_UP:  # -2:
                fx = -2
            if event.key == pygame.K_a:  # 1
                fx2 = 1
            if event.key == pygame.K_d:  # -1
                fx2 = -1
            if event.key == pygame.K_s:  # 2
                fx2 = 2
            if event.key == pygame.K_w:  # -2:
                fx2 = -2
    m1, m2, m3 = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    if ksyx == 0 and hxbd == 0:
        screen.blit(fm, (0, 0))
        screen.blit(kstp, (500 - 207, 600 - 250))
        pygame.mixer.music.unpause()
        screen.blit(drms, (500 - 100, 600 - 100))
        screen.blit(taitou, (0, 600-300))
    if m1 == 1 and 500 - 207 <= mx <= 500 - 207 + 415 and 600 - 250 <= my <= 600 - 250 + 149:
        ksyx = 1
    if m1 == 1 and 500 - 100 <= mx <= 500 - 100 + 200 and 600 - 100 <= my <= 600 -100 + 50:
        hxbd = 1
    if (ks == 0 or ks2 == 0) and ksyx == 1:
        screen.blit(xztk, (0, 0))
        screen.blit(xztk2, (0, 600 - 30))
        screen.blit(tkzs[f], (tkx, tky))
        screen.blit(tkjs[f], (tkx - 50, tky + 200))
        screen.blit(tkzs2[f2], (tkx2, tky2))
        screen.blit(tkjs2[f2], (tkx2 - 50, tky2 + 200))
    if (ks == 0 or ks2 == 0) and hxbd == 1:
        screen.blit(xztk, (0, 0))
        screen.blit(tkzs[f], (tkx, tky))
        screen.blit(tkjs[f], (tkx - 50, tky + 200))
    if fx == 0 and ks == 1 and ks2 == 0:
        screen.blit(qrtp, (tkx+100, tky+100))
    if fx2 == 0 and ks2 == 1 and ks == 0:
        screen.blit(qrtp, (tkx2+100, tky2+100))
    if fx == 0 and ks == 1 and ks2 == 1:
        screen.blit(tkzs1[f], (tkx, tky))
    if fx2 == 0 and ks2 == 1 and ks == 1 and dr == 0:
        screen.blit(tkzs12[f2], (tkx2, tky2))
    if fx == 1 and jsyx == 0:  # 坦克一
        if tkx >= 0:
            tkx += -a
        for g in range(100):
            if zkx[g] >= 0:
                if zkx[g]+50 >= tkx >= zkx[g] and zky[g] - 50 < tky < zky[g] + 50:
                    tkx += a
        tky = tky
        screen.blit(hjsds[e], (tkx, tky))
    if fx == -1 and jsyx == 0:
        if tkx <= 1000 - 50:
            tkx += a
        for g in range(100):
            if zkx[g] >= 0:
                if zkx[g]+50 >= tkx+50 >= zkx[g] and zky[g] - 50 < tky < zky[g] + 50:
                    tkx -= a
        tky = tky
        screen.blit(hjsds[b], (tkx, tky))
    if fx == 2 and jsyx == 0:
        tkx = tkx
        if tky <= 600 - 50:
            tky += a
        for g in range(100):
            if zkx[g] >= 0:
                if zkx[g]+100 > tkx+50 > zkx[g] and zky[g] <= tky+50 <= zky[g] + 50:
                    tky -= a
        screen.blit(hjsds[c], (tkx, tky))
    if fx == -2 and jsyx == 0:
        tkx = tkx
        if tky >= 0:
            tky += -a
        for g in range(100):
            if zkx[g] >= 0:
                if zkx[g] + 100 > tkx + 50 > zkx[g] and zky[g] <= tky <= zky[g] + 50:
                    tky += a
        screen.blit(hjsds[d], (tkx, tky))
    if fx2 == 1 and jsyx == 0 and dr == 0:  # 坦克二 l
        if tkx2 >= 0:
            tkx2 += -a2
        for g in range(100):
            if zkx[g] >= 0:
                if zkx[g]+50 >= tkx2 >= zkx[g] and zky[g] - 50 < tky2 < zky[g] + 50:
                    tkx2 += a2
        tky2 = tky2
        screen.blit(hjsds2[e2], (tkx2, tky2))
    if fx2 == -1 and jsyx == 0 and dr == 0:  # 坦克二 r
        if tkx2 <= 1000 - 50:
            tkx2 += a2
        for g in range(100):
            if zkx[g] >= 0:
                if zkx[g]+50 >= tkx2+50 >= zkx[g] and zky[g] - 50 < tky2 < zky[g] + 50:
                    tkx2 -= a2
        tky2 = tky2
        screen.blit(hjsds2[b2], (tkx2, tky2))
    if fx2 == 2 and jsyx == 0 and dr == 0:  # 坦克二 down
        tkx2 = tkx2
        if tky2 <= 600 - 50:
            tky2 += a2
        for g in range(100):
            if zkx[g] >= 0:
                if zkx[g]+100 > tkx2+50 > zkx[g] and zky[g] <= tky2+50 <= zky[g] + 50:
                    tky2 -= a2
        screen.blit(hjsds2[c2], (tkx2, tky2))
    if fx2 == -2 and jsyx == 0 and dr == 0:  # 坦克二 up
        tkx2 = tkx2
        if tky2 >= 0:
            tky2 += -a2
        for g in range(100):
            if zkx[g] >= 0:
                if zkx[g] + 100 > tkx2 + 50 > zkx[g] and zky[g] <= tky2 <= zky[g] + 50:
                    tky2 += a2
        screen.blit(hjsds2[d2], (tkx2, tky2))

    if fx == 1 and zdfx[0] == 0 and ks == 1 and jsyx == 0 and ks2 == 1:  # 子弹一l
        hjzdx[0] = tkx
        hjzdy[0] = tky + 25 - 5
        zdfx[0] = 1
    hjzdx[0] -= zdsd
    if hjzdx[0] <= 0 - 10:
        zdfx[0] = 0
    screen.blit(zd, (hjzdx[0], hjzdy[0]))

    if fx == -1 and zdfx[1] == 0 and ks == 1 and jsyx == 0 and ks2 == 1:  # 子弹一 r
        hjzdx[1] = tkx + 50
        hjzdy[1] = tky + 25 - 5
        zdfx[1] = 1
    hjzdx[1] += zdsd
    if hjzdx[1] >= 1000 - 10:
        zdfx[1] = 0
    screen.blit(zd, (hjzdx[1], hjzdy[1]))

    if fx == 2 and zdfx[2] == 0 and ks == 1 and jsyx == 0 and ks2 == 1:  # 子弹一 down
        hjzdx[2] = tkx + 25 - 5
        hjzdy[2] = tky + 50
        zdfx[2] = 1
    hjzdy[2] += zdsd
    if hjzdy[2] >= 600 - 10:
        zdfx[2] = 0
    screen.blit(zd, (hjzdx[2], hjzdy[2]))

    if fx == -2 and zdfx[3] == 0 and ks == 1 and jsyx == 0 and ks2 == 1:  # 子弹一 up
        hjzdx[3] = tkx + 25 - 5
        hjzdy[3] = tky
        zdfx[3] = 1
    hjzdy[3] -= zdsd
    if hjzdy[3] <= 0 - 10:
        zdfx[3] = 0
    screen.blit(zd, (hjzdx[3], hjzdy[3]))

    if fx2 == 1 and zdfx2[0] == 0 and ks == 1 and jsyx == 0 and ks2 == 1:  # 子弹二 l
        hjzdx2[0] = tkx2
        hjzdy2[0] = tky2 + 25 - 5
        zdfx2[0] = 1
    hjzdx2[0] -= zdsd2
    if hjzdx2[0] <= 0 - 10:
        zdfx2[0] = 0
    screen.blit(zd, (hjzdx2[0], hjzdy2[0]))

    if fx2 == -1 and zdfx2[1] == 0 and ks == 1 and jsyx == 0 and ks2 == 1:  # 子弹二 r
        hjzdx2[1] = tkx2 + 50
        hjzdy2[1] = tky2 + 25 - 5
        zdfx2[1] = 1
    hjzdx2[1] += zdsd2
    if hjzdx2[1] >= 1000 - 10:
        zdfx2[1] = 0
    screen.blit(zd, (hjzdx2[1], hjzdy2[1]))

    if fx2 == 2 and zdfx2[2] == 0 and ks == 1 and jsyx == 0 and ks2 == 1:  # 子弹二down
        hjzdx2[2] = tkx2 + 25 - 5
        hjzdy2[2] = tky2 + 50
        zdfx2[2] = 1
    hjzdy2[2] += zdsd2
    if hjzdy2[2] >= 600 - 10:
        zdfx2[2] = 0
    screen.blit(zd, (hjzdx2[2], hjzdy2[2]))

    if fx2 == -2 and zdfx2[3] == 0 and ks == 1 and jsyx == 0 and ks2 == 1:  # 子弹二up
        hjzdx2[3] = tkx2 + 25 - 5
        hjzdy2[3] = tky2
        zdfx2[3] = 1
    hjzdy2[3] -= zdsd2
    if hjzdy2[3] <= 0 - 10:
        zdfx2[3] = 0
    screen.blit(zd, (hjzdx2[3], hjzdy2[3]))

    if ks == 1 and jsyx == 0 and ks2 == 1:
        for i in range(100):  # 输出砖块
            screen.blit(zk, (zkx[i], zky[i]))
        for p in range(5):
            screen.blit(wdzk, (zkx[p], zky[p]))
        # 分别判断每颗子弹是否与砖相撞，相撞就消失
        for i in range(100):
            if (zkx[i] <= hjzdx[0] + 5 <= zkx[i] + 50) and (zky[i] <= hjzdy[0] + 5 <= zky[i] + 50) or \
                    (zkx[i] <= hjzdx2[0] + 5 <= zkx[i] + 50) and (zky[i] <= hjzdy2[0] + 5 <= zky[i] + 50):
                if i not in list:
                    zkx[i], zky[i] = -100, -100
                hjzdx[0] = -200
                hjzdy[0] = -200
                if fx == 1:
                    hjzdx[0] = tkx
                    hjzdy[0] = tky + 25 - 5
                    zdfx[0] = 1
                hjzdx2[0] = -100
                hjzdy2[0] = -200
                if fx2 == 1:
                    hjzdx2[0] = tkx2
                    hjzdy2[0] = tky2 + 25 - 5
                    zdfx2[0] = 1
            if (zkx[i] <= hjzdx[1] + 5 <= zkx[i] + 50 and zky[i] <= hjzdy[1] + 5 <= zky[i] + 50) or \
                    (zkx[i] <= hjzdx2[1] + 5 <= zkx[i] + 50 and zky[i] <= hjzdy2[1] + 5 <= zky[i] + 50):
                if i not in list:
                    zkx[i], zky[i] = -100, -100
                hjzdx[1] = 1200
                hjzdy[1] = -200
                if fx == -1:
                    hjzdx[1] = tkx + 50
                    hjzdy[1] = tky + 25 - 5
                    zdfx[1] = 1
                hjzdx2[1] = 1200
                hjzdy2[1] = -200
                if fx2 == -1:
                    hjzdx2[1] = tkx2 + 50
                    hjzdy2[1] = tky2 + 25 - 5
                    zdfx2[1] = 1
            if (zkx[i] <= hjzdx[2] + 5 <= zkx[i] + 50 and zky[i] <= hjzdy[2] + 5 <= zky[i] + 50) or \
                    (zkx[i] <= hjzdx2[2] + 5 <= zkx[i] + 50 and zky[i] <= hjzdy2[2] + 5 <= zky[i] + 50):
                if i not in list:
                    zkx[i], zky[i] = -100, -100
                hjzdx[2] = -200
                hjzdy[2] = 700
                if fx == 2:
                    hjzdx[2] = tkx + 25 - 5
                    hjzdy[2] = tky + 50
                    zdfx[2] = 1
                hjzdx2[2] = -200
                hjzdy2[2] = 700
                if fx2 == 2:
                    hjzdx2[2] = tkx2 + 25 - 5
                    hjzdy2[2] = tky2 + 50
                    zdfx2[2] = 1
            if (zkx[i] <= hjzdx[3] + 5 <= zkx[i] + 50 and zky[i] <= hjzdy[3] + 5 <= zky[i] + 50) or \
                    (zkx[i] <= hjzdx2[3] + 5 <= zkx[i] + 50 and zky[i] <= hjzdy2[3] + 5 <= zky[i] + 50):
                if i not in list:
                    zkx[i], zky[i] = -100, -100
                hjzdx[3] = -200
                hjzdy[3] = -100
                if fx == -2:
                    hjzdx[3] = tkx + 25 - 5
                    hjzdy[3] = tky
                    zdfx[3] = 1
                hjzdx2[3] = -200
                hjzdy2[3] = -200
                if fx2 == -2:
                    hjzdx2[3] = tkx2 + 25 - 5
                    hjzdy2[3] = tky2
                    zdfx2[3] = 1
    if ks == 1 and jsyx == 0 and ks2 == 1 and dr == 0 and hxbd == 0:
        # 判断坦克二被坦克玩家一子弹击中，击中子弹就消失
        for i in range(4):
            if (tkx <= hjzdx2[i] <= tkx + 50 and tky <= hjzdy2[i] + 25 - 5 <= tky + 50):
                fsyp.play()
                if i == 0:
                    hjzdx2[i] = -100
                    hjzdy2[i] = -200
                    if fx2 == 1:
                        hjzdx2[i] = tkx2
                        hjzdy2[i] = tky2 + 25 - 5
                        zdfx2[i] = 1
                if i == 1:
                    hjzdx2[i] = 1200
                    hjzdy2[i] = -200
                    if fx2 == -1:
                        hjzdx2[i] = tkx2 + 50
                        hjzdy2[i] = tky2 + 25 - 5
                        zdfx2[i] = 1
                if i == 2:
                    hjzdx2[i] = -200
                    hjzdy2[i] = 700
                    if fx2 == 2:
                        hjzdx2[i] = tkx2 + 25 - 5
                        hjzdy2[i] = tky2 + 50
                        zdfx2[i] = 1
                if i == 3:
                    hjzdx2[i] = -200
                    hjzdy2[i] = -200
                    if fx2 == -2:
                        hjzdx2[i] = tkx2 + 25 - 5
                        hjzdy2[i] = tky2
                        zdfx2[i] = 1
                if (tkx - 100 <= tkx2 <= tkx + 100 and tky - 100 <= tky2 <= tky + 100) == False:
                    fen2 += 1
        # 判断坦克一被坦克玩家二子弹击中，击中子弹就消失
        for j in range(4):
            if (tkx2 <= hjzdx[j] <= tkx2 + 50 and tky2 <= hjzdy[j] + 25 - 5 <= tky2 + 50):
                fsyp.play()
                if j == 0:
                    hjzdx[j] = -100
                    hjzdy[j] = -200
                    if fx2 == 1:
                        hjzdx[j] = tkx
                        hjzdy[j] = tky + 25 - 5
                        zdfx[j] = 1
                if j == 1:
                    hjzdx[j] = 1200
                    hjzdy[j] = -200
                    if fx == -1:
                        hjzdx[j] = tkx + 50
                        hjzdy[j] = tky + 25 - 5
                        zdfx[j] = 1
                if j == 2:
                    hjzdx[j] = -200
                    hjzdy[j] = 700
                    if fx == 2:
                        hjzdx[j] = tkx + 25 - 5
                        hjzdy[j] = tky + 50
                        zdfx[j] = 1
                if j == 3:
                    hjzdx[j] = -200
                    hjzdy[j] = -200
                    if fx == -2:
                        hjzdx[j] = tkx + 25 - 5
                        hjzdy[j] = tky
                        zdfx[j] = 1
                if (tkx2 - 100 <= tkx <= tkx2 + 100 and tky2 - 100 <= tky <= tky2 + 100) == False:
                    fen1 += 1
        # 判断坦克与坦克距离，近就不发炮
        if tkx2 - 100 <= tkx <= tkx2 + 100 and tky2 - 100 <= tky <= tky2 + 100:
            for i in range(4):
                hjzdx[i] = -100
                hjzdy[i] = -200
        if tkx - 100 <= tkx2 <= tkx + 100 and tky - 100 <= tky2 <= tky + 100:
            for i in range(4):
                hjzdx2[i] = -100
                hjzdy2[i] = -200

    fenshu2 = font.render("玩家二得分：%d" % fen2, True, (255, 255, 255))
    fenshu1 = font.render("玩家一得分：%d" % fen1, True, (255, 255, 255))
    fenshu11 = font.render("玩家一最终得分：%d" % fen1, True, (255, 255, 255))
    fenshu22 = font.render("玩家二最终得分：%d" % fen2, True, (255, 255, 255))
    if ks == 1 and jsyx == 0 and ks2 == 1 and dr == 0:
        screen.blit(fenshu2, (1000 - 400, 600 - 40))
        screen.blit(fenshu1, (0, 600 - 40))
    if fen1 == 10 or fen2 == 10:
        if tkbz == 0:
            jsyp.play()
            pygame.mixer.music.pause()
            tkbz = 2
        jsyx = 1
    if drjs == 1:
        screen.blit(sc, (0, 0))
    if (jsyx == 1 and jsyxx <= 0) or drjs == 1:
        if jsyxx <= -100:
            jsyxx += 5
        if jsyxx == -95:
            jsyxx = -100
        screen.blit(jsyxtb, (0, jsyxx - 50))
    if fen1 <= fen2 and jsyxx == -100 and dr == 0:
        screen.blit(thtp, (500 - 200, 600 - 300))
        screen.blit(fenshu11, (0, 600 - 40))
        screen.blit(fenshu22, (1000-300, 600 - 40))
    if fen1 > fen2 and jsyxx == -100 and dr == 0:
        screen.blit(pmtp, (500 - 150, 600 - 300))
        screen.blit(fenshu11, (0, 600 - 40))
        screen.blit(fenshu22, (1000-300, 600 - 40))
    if jsyxx == -100:
        if tkbz == 2:
            hhs.play()
        tkbz = 3
        if cxksx >= 1000 - 128:
            cxksx -= 8
        if cxksx == 1000-128-8:
            cxksx = 1000-128
        screen.blit(cxks, (cxksx, 300-64))
    if cxksx == 1000-128 and cxksx <= mx <=1000 and 300-64 <= my <= 300-64+80:
        if m1 == 1:
            tkx = 500 - 100
            tky = 300 - 250
            fx = 0
            hjzdx = [1000, -1000, 1000, 1000]
            hjzdy = [1000, 1000, -1000, 1000]
            zdfx = [0, 0, 0, 0]
            tkx2 = 500 - 100
            tky2 = 300
            fx2 = 0
            hjzdx2 = [1000, -1000, 1000, 1000]
            hjzdy2 = [1000, 1000, -1000, 1000]
            zdfx2 = [0, 0, 0, 0]
            a = 4
            zdsd = 7
            e, b, c, d, f = 0, 1, 2, 3, 0
            a2 = 4
            zdsd2 = 7
            e2, b2, c2, d2, f2 = 0, 1, 2, 3, 0
            ks = 0
            ks2 = 0
            zkx = []
            zky = []
            fen1 = 0
            fen2 = 0
            ksyx = 0
            ksyx2 = 0
            jsyx = 0
            jsyxx = -600
            jfks = 0
            kaka = 0
            list = [0, 1, 2, 3, 4]
            cxksx = 1000
            tkbz = 0
            hxbd = 0
            dr = 0
            drjs = 0
            for i in range(100):
                zkxx = random.randint(0, 20) * 50
                zkyy = random.randint(1, 10) * 50
                zkx.append(zkxx)
                zky.append(zkyy)
    pygame.display.update()