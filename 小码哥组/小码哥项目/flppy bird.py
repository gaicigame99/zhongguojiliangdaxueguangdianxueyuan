import pygame
import random
pygame.init()
pygame.mixer.init()
font =pygame.font.Font("C:\Windows\Fonts\STENCIL.ttf", 60)
font2 =pygame.font.Font("C:\Windows\Fonts\STENCIL.ttf", 20)
fly_music=pygame.mixer.Sound("flappybird/fly.ogg")
peng_music=pygame.mixer.Sound("flappybird/peng.ogg")
score_music=pygame.mixer.Sound("flappybird/get_score.ogg")
screen=pygame.display.set_mode((288,512))
#随机获取背景
day_night=random.randint(0,1)
if day_night==0:
    bk="bg_night"
else:
    bk="bg_day"
#随机获取小鸟
bird=random.randint(0,2)

background=pygame.image.load(f"flappybird/{bk}.png")
land=pygame.image.load(f"flappybird/land.png")


class Bird(object):
    def __init__(self,screen):
        self.image = pygame.image.load(f"flappybird/bird{bird}_0.png")
        image1 = pygame.image.load(f"flappybird/bird{bird}_0.png")
        image2 = pygame.image.load(f"flappybird/bird{bird}_1.png")
        image3 = pygame.image.load(f"flappybird/bird{bird}_2.png")
        self.images = [image1, image2, image3]
        self.jishi=0
        self.x=85
        self.y=250
        self.screen=screen
        self.start_x=85
        self.start_y=250
        self.over=0
    def move(self,):
        if self.y<=400-35:
            self.y+=0.5
        if interface.up==1:
            if self.y>=0:
                self.y-=3
                #fly_music.play()
        bird.motion(bird.jishi)
    def show(self):
        bird.motion(bird.jishi)
    def motion(self, jishiqi):
        #振动翅膀
        if jishiqi // 10 == 0:
            screen.blit(self.images[0], (self.x, self.y))
        if jishiqi // 10 == 1:
            screen.blit(self.images[1], (self.x,self.y))
        if jishiqi // 10 == 2:
            screen.blit(self.images[2], (self.x,self.y))
    def peng(self):
        if pipe.pipe_x<self.x+40<pipe.pipe_x+52 and (self.y<=pipe.pipe_y-105 or self.y+42>=pipe.pipe_y):
            self.over=1
            peng_music.play()
        if pipe.pipe_x2 < self.x + 40< pipe.pipe_x2 + 52 and (self.y <= pipe.pipe_y2 - 105 or self.y + 42>= pipe.pipe_y2):
            self.over = 1
            peng_music.play()
        if self.y+48==400:
            self.over = 1
            peng_music.play()


class Interface(object):
    def __init__(self):
        self.ready = pygame.image.load(f"flappybird/text_ready.png")
        self.tutorial=pygame.image.load(f"flappybird/tutorial.png")
        self.land_x=0
        self.game_start=0
        self.up=0
    def show(self):
        screen.blit(background, (0, 0))
        bird.motion(bird.jishi)
        if self.game_start==0:
            screen.blit(self.ready, (60, 160))
            screen.blit(self.tutorial,(100,230))



class Pipe(object):
    def __init__(self):
        self.pipe_up=pygame.image.load(f"flappybird/pipe_up.png")
        self.pipe_down = pygame.image.load(f"flappybird/pipe_down.png")
        self.pipe_x=300
        self.pipe_y=random.randint(150,300)
        self.pipe_x2 = 460
        self.pipe_y2 = random.randint(150, 300)
    def show(self):
        screen.blit(self.pipe_up,(self.pipe_x,self.pipe_y))
        screen.blit(self.pipe_down, (self.pipe_x, self.pipe_y-420))
        screen.blit(self.pipe_up, (self.pipe_x2, self.pipe_y2))
        screen.blit(self.pipe_down, (self.pipe_x2, self.pipe_y2 - 420))
    def move(self):
        self.pipe_x-=0.5
        self.pipe_x2 -= 0.5
        if self.pipe_x<=-52:
            self.pipe_x=300
            self.pipe_y = random.randint(150, 300)
        if self.pipe_x2<=-52:
            self.pipe_x2=300
            self.pipe_y2 = random.randint(150, 300)
        pipe.show()




class Over(object):
    def __init__(self):
        self.over = pygame.image.load(f"flappybird/text_game_over.png")
        self.finnal = pygame.image.load(f"flappybird/score_panel.png")
        self.restart=pygame.image.load(f"flappybird/button_play.png")
        self.text_score = 0
        self.highest_score=0
        self.m1, self.m2, self.m3 = pygame.mouse.get_pressed()
        self.mx, self.my = pygame.mouse.get_pos()
    def show(self):
        if bird.over:
            interface.land_x += 0.5
            bird.y=500
            bird.x=-100
            pipe.pipe_x+=0.5
            pipe.pipe_x2+=0.5
        over.score()
        screen.blit((font.render(f"{str(self.text_score)}", True, (255,255,255))), (138, 100))
        if bird.over:
            screen.blit(self.over, (45, 160))
            screen.blit(self.finnal,(25,220))
            screen.blit(self.restart, (25, 335))
            over.rrestart()
            screen.blit((font2.render(f"{str(self.text_score)}", True, (255, 255, 255))), (210, 260))
            screen.blit((font2.render(f"{str(self.highest_score)}", True, (255, 255, 255))), (210, 305))
    def score(self):
        if pipe.pipe_x == 85 - 52 or pipe.pipe_x2 == 85 - 52:
            score_music.play()
            self.text_score += 1
        if self.highest_score<self.text_score:
            self.highest_score=self.text_score
    def rrestart(self):
        if bird.over:
            self.m1, self.m2, self.m3 = pygame.mouse.get_pressed()
            self.mx, self.my = pygame.mouse.get_pos()
            if self.m1:
                if 25<self.mx<25+116 and 335<self.my<335+70:
                    bird.over=0
                    interface.game_start = 0
                    interface.up = 0
                    bird.y =250
                    bird.x = 85
                    pipe.pipe_x = 300
                    pipe.pipe_y = random.randint(150, 300)
                    pipe.pipe_x2 = 460
                    pipe.pipe_y2 = random.randint(150, 300)
                    self.text_score=0


interface=Interface()
bird=Bird(screen)
pipe=Pipe()
over=Over()
while True:
    #逐条获取事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            m1, m2, m3 = pygame.mouse.get_pressed()
            if m1:
                if interface.game_start:
                    interface.up=1
                interface.game_start=1
        else:
            interface.up=0
    #计时器自加
    bird.jishi += 1
    if bird.jishi == 30:
        bird.jishi = 0
    #显示游戏界面
    interface.show()
    # 游戏开始
    if interface.game_start == 1:
        # 显示小鸟运动
        bird.move()
        # 显示水管运动
        pipe.move()
    # 显示下栏
    screen.blit(land, (interface.land_x, 400))
    interface.land_x -= 0.5
    if interface.land_x == 288 - 336:
        interface.land_x = 0
    #判断碰撞
    bird.peng()
    #游戏结束界面
    over.show()
    # 显示屏幕
    pygame.display.update()