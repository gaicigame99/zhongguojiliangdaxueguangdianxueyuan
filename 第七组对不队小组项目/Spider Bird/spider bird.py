import pygame
pygame.init()
import random


screen = pygame.display.set_mode((1540,800))
backMusic = pygame.mixer.Sound("angry_bird.ogg")
jumpMusic = pygame.mixer.Sound("jump.ogg")
scoreMusic = pygame.mixer.Sound("score.ogg")
failMusic = pygame.mixer.Sound("fail.ogg")
backMusic.play(-1) ## 循环播放背景音乐


sun = pygame.image.load("sun.png") ## 96*96
moon = pygame.image.load("moon.png") ## 72*72
font_size = 30
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",font_size)
DBLUE = (60,100,200)

nandu = 1
level_text = font.render(f"Level: {nandu}", True, DBLUE)  ## 难度文字
fenshu = 0
score_text = font.render(f"Score: {fenshu}", True, DBLUE)  ## 得分文字

xmouse, ymouse = pygame.mouse.get_pos()
m1, m2, m3 = pygame.mouse.get_pressed()





### 白天背景
class Bg_day(object):
    def __init__(self,_screen):
        self.image = pygame.image.load("bg_day.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = [0,450,900,1350,1800]
        self.y = 0
        self.speed = 3
    def gundong(self):
        for i in range(len(self.x)):
            self.x[i]-=self.speed
            if self.x[i]<=1540-self.width*5:
                self.x[i]=1540
            self.screen.blit(self.image,(self.x[i],self.y))
    def reset(self):
        for i in range(len(self.x)):
            self.screen.blit(self.image,(self.x[i],self.y))
bg_day = Bg_day(screen)



### 夜晚背景
class Bg_night(object):
    def __init__(self,_screen):
        self.image = pygame.image.load("bg_night.png")
        self.width = bg_day.width
        self.height = bg_day.height
        self.screen = _screen
        self.x = bg_day.x
        self.y = 0
        self.speed = bg_day.speed
    def gundong(self):
        for i in range(len(self.x)):
            self.x[i]-=self.speed
            if self.x[i]<=1540-self.width*5:
                self.x[i]=1540
            self.screen.blit(self.image,(self.x[i],self.y))
bg_night = Bg_night(screen)



### 初始界面
class Ready(object):
    def __init__(self,_screen):
        self.image = pygame.image.load("button_play.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.image1 = pygame.image.load("start.png")
        self.rect1 = self.image1.get_rect()
        self.width1 = self.rect1.width
        self.screen = _screen
        self.x = 1540/2-self.width//2
        self.y = 600
    def show(self):
        self.screen.blit(self.image1,(1540/2-self.width1//2,50))
        self.screen.blit(self.image,(self.x,self.y))
ready = Ready(screen)




### 地面背景
class Land(object):
    def __init__(self,_screen):
        self.image = pygame.image.load("land.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = [0,300,600,900,1200,1500,1800]
        self.y = 700
        self.speed = 5
    def gundong(self):
        for i in range(len(self.x)):
            self.x[i]-=self.speed
            if self.x[i]<=1540-self.width*7:
                self.x[i]=1540
            self.screen.blit(self.image,(self.x[i],self.y))
land = Land(screen)



### 小鸟 ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
class Bird_red(object):
    def __init__(self,_screen):
        self.image = pygame.image.load("bird_red.png")
        self.image1 = pygame.image.load("bird_red1.png")
        self.image_spider = pygame.image.load("bird_spider.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x , self.y = 300,200
        self.speed = 0
    def down(self):
        self.speed+=1.3
        if self.y<land.y-self.height:
            self.y+=self.speed
            if self.y>=land.y-self.height:
                self.y=land.y-self.height
        if nandu==1:
            self.screen.blit(self.image,(self.x,self.y))
        if nandu==2:
            self.screen.blit(self.image_spider,(self.x,self.y))
    def fly(self):
        self.speed = 0
        self.y -= 40
    def reset(self):
        self.screen.blit(self.image_spider,(1540/2-self.width//2,300))
bird = Bird_red(screen)



### 柱子背景
class Zhuzi_up(object):
    def __init__(self,_screen):
        self.image = pygame.image.load("zhu_up.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x ,self.y1 ,self.y= [],[],[]
    def add(self):
        for i in range(100):
            self.x.append(600+i*(self.width+200))
            self.y1.append(800-land.height-60)
            self.y.append(random.randint(800-land.height-300,800-land.height-60))
    def gundong(self):
        for i in range(len(self.x)):
            self.x[i] -= land.speed
            if self.y1[i]>self.y[i] and self.x[i]<1540:
                self.y1[i]-=2
            self.screen.blit(self.image,(self.x[i],self.y1[i]))
zhu_up = Zhuzi_up(screen)
zhu_up.add()


class Zhuzi_down(object):
    def __init__(self,_screen):
        self.image = pygame.image.load("zhu_down.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x , self.y1 ,self.y = [],[],[]
    def add(self):
        for i in range(100):
            self.x.append(zhu_up.x[i])
            self.y1.append(60-self.height)
            self.y.append(zhu_up.y[i]-self.height-200+random.randint(-100,50))
    def gundong(self):
        for i in range(len(self.x)):
            self.x[i] -= land.speed
            if self.y1[i]<self.y[i] and self.x[i]<1540:
                self.y1[i]+=2
            self.screen.blit(self.image,(self.x[i],self.y1[i]))
zhu_down = Zhuzi_down(screen)
zhu_down.add()



### 黑暗模式
class Black_mode(object):
    def __init__(self,_screen):
        self.image = pygame.image.load("light.png")
        self.screen = _screen
    def show(self):
        self.screen.blit(self.image,(xmouse-1540,ymouse-800))
black_mode = Black_mode(screen)




## 得分
# def score(fenshu0):
#     for i in range(len(zhu_up.x)):
#         if bird.y>zhu_down.y1[i]+zhu_down.height and bird.y+bird.height<zhu_up.y1[i] \
#             and zhu_up.x[i]+zhu_up.width+3>+bird.x+bird.width//2>+zhu_up.x[i]+zhu_up.width:
#             fenshu0+=1
#             return fenshu0


## 碰撞
def clide():
    for i in range(len(zhu_up.x)):
        if bird.x + bird.width >= zhu_up.x[i] and bird.x <= zhu_up.x[i] + zhu_up.width and \
            bird.y + bird.height >= zhu_up.y1[i] \
            or bird.x + bird.width >= zhu_down.x[i] and bird.x <= zhu_down.x[i] + zhu_down.width and \
            bird.y <= zhu_down.y1[i] + zhu_down.height \
            or bird.y==land.y-bird.height:
            return False
        else:
            return True


### game over
class Over(object):
    def __init__(self,_screen):
        self.text = pygame.image.load("text_game_over.png")
        self.rect = self.text.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.screen = _screen
        self.x = 1540/2-self.width//2
        self.y = 800/2-self.height//2
    def show(self):
        self.screen.blit(self.text, (self.x, self.y))
over = Over(screen)



playflag=0
### MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()# 退出
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:# 空格按键
                jumpMusic.play()# 播放音效
                bird.fly()

    xmouse, ymouse = pygame.mouse.get_pos()
    m1, m2, m3 = pygame.mouse.get_pressed()



    if nandu==1:
        bg_day.gundong()# 显示背景
        screen.blit(sun,(200,150))# 太阳
    if nandu>1:
        bg_night.gundong()# 显示背景
        screen.blit(moon,(200,150))# 月亮





    if playflag==0:
        ready.show()
    if ready.x<xmouse<ready.x+ready.width and ready.y<ymouse<ready.y+ready.height:
        if m1==1:
            playflag=1




    if playflag==1:
        if clide() == True:

            # for i in range(len(zhu_up.x)):
            #     if bird.y > zhu_down.y1[i] + zhu_down.height and bird.y + bird.height < zhu_up.y1[i] \
            #             and zhu_up.x[i] + zhu_up.width + 3 > +bird.x + bird.width // 2 > +zhu_up.x[i] + zhu_up.width:
            #         fenshu += 1
            # score_text = font.render(f"Score: {fenshu}", True, DBLUE)  ## 得分文字


            zhu_up.gundong()# 地上的柱子
            zhu_down.gundong()# 天上的柱子
            land.gundong()# 地面
            if nandu==2:
                black_mode.show()
            bird.down()# 小鸟



            if zhu_up.x[3]<0:
                nandu=2
            level_text = font.render(f"Level: {nandu}", True, DBLUE)  ## 难度文字
            screen.blit(level_text,(10,10))
            # screen.blit(score_text,(10,15+font_size))


        if clide() == False:
            failMusic.play(loops=0)# 播放音效
            bg_day.reset()
            bird.reset()
            over.show()









    pygame.display.update()