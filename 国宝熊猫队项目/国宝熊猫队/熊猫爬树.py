import pygame
import random
pygame.init()
pygame.mixer.init()
backMusic = pygame.mixer.Sound("panda/2.wav")
backMusic.play()
screen = pygame.display.set_mode((449,800))
background = pygame.image.load("panda/bg.png")
start=pygame.image.load("panda/start.png")
end=pygame.image.load("panda/over.png")
pandaz=pygame.image.load("panda/panda_left.png")
panday=pygame.image.load("panda/panda_right.png")
pandax=pygame.image.load("panda/panda_fall.png")
bug_z3=pygame.image.load("panda/bug_2left.png")
bug_y3=pygame.image.load("panda/bug_2right.png")
bug_z3f=pygame.image.load("panda/bug2_leftfall.png")
bug_y3f=pygame.image.load("panda/bug2_rightfall.png")
font=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",40)
px,py=161,350
zuo=[11,161,310]
you=[86,235,385]
speedx=75
speedy=3
change=0
now=0
cx,cy=[],[]
cc=[]
bx,by=[],[]
bb=[]
t=0
flag=0
flag2=0
zx,zy=0,0
yz,yy=0,0
go=0
over=0
fenshu=0
fm=0
for i in range(50):
    c=random.randint(0,2)
    cc.append(c)
    if c == 0:
        x1 = 31
        y1=random.randint(820,10000)
        cx.append(x1)
        cy.append(y1)
    if c == 1:
        x1 = 181
        y1=random.randint(820,10000)
        cx.append(x1)
        cy.append(y1)
    if c == 2:
        x1 = 330
        y1=random.randint(820,10000)
        cx.append(x1)
        cy.append(y1)
for i in range(50):
    b=random.randint(0,2)
    bb.append(b)
    if b == 0:
        x = 89
        y=random.randint(820,10000)
        bx.append(x)
        by.append(y)
    if b == 1:
        x = 238
        y=random.randint(820,10000)
        bx.append(x)
        by.append(y)
    if b == 2:
        x = 488
        y=random.randint(820,10000)
        bx.append(x)
        by.append(y)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(start,(0,0))
    keys = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()
    m1,m2,m3 = pygame.mouse.get_pressed()
    if m1:
        go=1
    if go:
        screen.blit(background, (0, 0))
        score = font.render("%d" % fenshu, True, (255, 255, 255))
        screen.blit(score, (10, 10))

        for i in range(len(cx)):
            if cc[i] == 0:
                screen.blit(bug_z3, (cx[i], cy[i]))
                cy[i] -= 1
                if cy[i] < py + 54 < cy[i] + 32 and px < cx[i] < px + 54:
                    if keys[pygame.K_DOWN]:
                        flag = 1
                    else:
                        over=1
                    cc[i] = 4
                    zx = cx[i]
                    zy = cy[i]
                if px<cx[i]+10<px+54 and py<cy[i]+16<py+64:
                    if keys[pygame.K_DOWN]:
                        flag = 1
                        fenshu += 1
                    else:
                        over = 1
            if cc[i] == 1:
                screen.blit(bug_z3, (cx[i], cy[i]))
                cy[i] -= 1
                if cy[i] < py + 54 < cy[i] + 32 and px < cx[i] < px + 54:
                    if keys[pygame.K_DOWN]:
                        flag = 1
                        fenshu+=1
                    else:
                        over=1
                    cc[i] = 4
                    zx = cx[i]
                    zy = cy[i]
                if px<cx[i]+10<px+54 and py<cy[i]+16<py+64:
                    over = 1
            if cc[i] == 2:
                screen.blit(bug_z3, (cx[i], cy[i]))
                cy[i] -= 1
                if cy[i] < py + 54 < cy[i] + 32 and px < cx[i] < px + 54:
                    if keys[pygame.K_DOWN]:
                        flag = 1
                        fenshu += 1
                    else:
                        over=1
                    cc[i] = 4
                    zx = cx[i]
                    zy = cy[i]
                if  px<cx[i]+10<px+54 and py<cy[i]+16<py+64:
                    over = 1
            if cy[i] < -30:
                cc[i] = random.randint(0, 2)
                cy[i] = random.randint(820, 2000)
        if flag:
            screen.blit(bug_z3f, (zx, zy))
            zy += 3

        for i in range(len(bx)):
            if bb[i] == 0:
                screen.blit(bug_y3, (bx[i], by[i]))
                by[i] -= 1
                if by[i] < py + 54 < by[i] + 32 and px < bx[i] < px + 54:
                    if keys[pygame.K_DOWN]:
                        flag2 = 1
                        fenshu += 1
                    else:
                        over=1
                    bb[i] = 4
                    yx = bx[i]
                    yy = by[i]
                if px<bx[i]+10<px+54 and py<by[i]+16<py+64:
                    over = 1
            if bb[i] == 1:
                screen.blit(bug_y3, (bx[i], by[i]))
                by[i] -= 1
                if by[i] < py + 54 < by[i] + 32 and px < bx[i] < px + 54:
                    if keys[pygame.K_DOWN]:
                        flag2 = 1
                        fenshu += 1
                    else:
                        over=1
                    bb[i] = 4
                    yx = bx[i]
                    yy = by[i]
                if px<bx[i]+10<px+54 and py<by[i]+16<py+64:
                    over=1
            if bb[i] == 2:
                screen.blit(bug_y3, (bx[i], by[i]))
                by[i] -= 1
                if by[i] < py + 54 < by[i] + 32 and px < bx[i] < px + 54:
                    if keys[pygame.K_DOWN]:
                        flag2 = 1
                        fenshu += 1
                    else:
                        over=1
                    bb[i] = 4
                    yx = bx[i]
                    yy = by[i]
                if px<bx[i]+10<px+54 and py<by[i]+16<py+64:
                    over=1
            if by[i] < -30:
                bb[i] = random.randint(0, 2)
                by[i] = random.randint(820, 2000)
        if flag2:
            screen.blit(bug_y3f, (yx, yy))
            yy += 3

        if event.type == pygame.KEYDOWN:
            if px < 385:
                if event.key == 275:
                    px += speedx
                    if px > 385:
                        px = 385
                    event.key = 0
                    change += 1
            if px > 11:
                if event.key == 276:
                    px -= speedx
                    if px < 11:
                        px = 11
                    event.key = 0
                    change += 1
            if event.key == 273:
                if py > 0:
                    py -= speedy
            if event.key == 274:
                if py < 800 - 64:
                    py += speedy
        if change % 2 == 0:
            screen.blit(pandaz, (px, py))
        if change % 2 == 1:
            screen.blit(panday, (px, py))
    if over:
        screen.blit(pandax,(px,py))
    if over:
        py+=4
        if py>800:
            screen.blit(end, (0, 0))
            screen.blit(score, (210, 319))
            if m1==1 and 185<mx<266 and 491<my<571:
                over=0
                go=1
                py=350
                cx, cy = [], []
                cc = []
                bx, by = [], []
                bb = []
                t = 0
                flag = 0
                flag2 = 0
                zx, zy = 0, 0
                yz, yy = 0, 0
                fenshu = 0
                for i in range(250):
                    c = random.randint(0, 2)
                    cc.append(c)
                    if c == 0:
                        x1 = 31
                        y1 = random.randint(820, 10000)
                        cx.append(x1)
                        cy.append(y1)
                    if c == 1:
                        x1 = 181
                        y1 = random.randint(820, 10000)
                        cx.append(x1)
                        cy.append(y1)
                    if c == 2:
                        x1 = 330
                        y1 = random.randint(820, 10000)
                        cx.append(x1)
                        cy.append(y1)
                for i in range(250):
                    b = random.randint(0, 2)
                    bb.append(b)
                    if b == 0:
                        x = 89
                        y = random.randint(820, 10000)
                        bx.append(x)
                        by.append(y)
                    if b == 1:
                        x = 238
                        y = random.randint(820, 10000)
                        bx.append(x)
                        by.append(y)
                    if b == 2:
                        x = 488
                        y = random.randint(820, 10000)
                        bx.append(x)
                        by.append(y)


    pygame.display.update()