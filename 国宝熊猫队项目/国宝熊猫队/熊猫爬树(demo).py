import pygame
import random
pygame.init()
pygame.mixer.init()
backMusic = pygame.mixer.Sound("panda/2.wav")
backMusic.play()
screen=pygame.display.set_mode((450,800))
background=pygame.image.load("panda/bg.png")
start=pygame.image.load("panda/start.png")
panda_l=pygame.image.load("panda/panda_left.png")
panda_r=pygame.image.load("panda/panda_right.png")
panda_d=pygame.image.load("panda/panda_fall.png")
insect_l=pygame.image.load("panda/bug_2left.png")
insect_r=pygame.image.load("panda/bug_2right.png")
insect_lf=pygame.image.load("panda/bug2_leftfall.png")
insect_rf=pygame.image.load("panda/bug2_rightfall.png")
overtp=pygame.image.load("panda/over.png")
font=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",30)
px,py=161,350
zuo=[11,161,310]
you=[86,235,385]
s=random.randint(0,2)
t=random.randint(0,2)
speedx=75
speedy=2
change=0
go=0
flag_z=1
flag_y=1
over=0
fenshu=0
cyx=you[s]
cyy=900+32
czx=zuo[t]+20
czy=800+32

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(start,(0,0))
    mx, my = pygame.mouse.get_pos()
    m1, m2, m3 = pygame.mouse.get_pressed()
    if m1==1 and 150<mx<290 and 530<my<570:
        go=1
    if go:
        screen.blit(background,(0,0))
        if event.type == pygame.KEYDOWN:
            if px<385:
                if event.key==275:
                    px+=speedx
                    if px>385:
                        px=385
                    event.key=0
                    change+=1
            if px>11:
                if event.key==276:
                    px-=speedx
                    if px<11:
                        px=11
                    event.key=0
                    change+=1
            if event.key==273:
                if py>0:
                    py-=speedy
            if event.key==274:
                if py<800-64:
                    py+=speedy
        if change%2==0 :
            screen.blit(panda_l,(px,py))
        if change%2==1 :
            screen.blit(panda_r,(px,py))
        if flag_y==1:
            screen.blit(insect_r, (cyx, cyy))
            cyy-=1
            if cyy < -32:
                cyy = 832
        if flag_z==1:
            screen.blit(insect_l, (czx, czy))
            czy -= 1
            if czy < -32:
                czy = 832
        keys = pygame.key.get_pressed()
        if px<cyx+10<px+54 and py<cyy+16<py+64:
            if keys[pygame.K_DOWN]:
                flag_y=0
            else:
                over=1
        if px<czx+10<px+54 and py<czy+16<py+64:
            if keys[pygame.K_DOWN]:
                flag_z=0
            else:
                over=1
        if flag_y==0:
            screen.blit(insect_rf, (cyx+20, cyy))
            cyy+=3
            if 832<cyy-32<836:
                fenshu+=1
                flag_y=1
                s=random.randint(0,2)
                cyx=you[s]
                cyy=800+32

        if flag_z==0:
            screen.blit(insect_lf, (czx-20, czy))
            czy += 3
            if 832<czy-32<836:
                fenshu+=1
                flag_z=1
                t = random.randint(0, 2)
                czx = zuo[s] + 20
                czy = 800 + 32

        if over:
            screen.blit(panda_d,(px,py))
            py+=4
            if py>850:
                screen.blit(overtp,(0,0))
                screen.blit(score, (210, 319))
                if m1 == 1 and 185 < mx < 266 and 491 < my < 571:
                    over=0
                    fenshu=0
                    go=1
                    py=350
                    cyy=900+32
                    czy=800+32
        score = font.render("%d" % fenshu, True, (255, 255, 255))
        if over==0:
            screen.blit(score, (10, 10))

    pygame.display.update()
