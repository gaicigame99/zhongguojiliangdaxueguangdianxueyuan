import sys, time, random, math, pygame, locale
from pygame.locals import *
pygame.mixer.init()
pygame.init()
backMusic = pygame.mixer.Sound("run/background.ogg")
backMusic.play()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()    #帧率设置


class Background(object):
    def __init__(self, _screen, _x, _y):
        self.x = _x
        self.y = _y
        self.image = pygame.image.load("run/background.png")
        self.first = pygame.image.load("run/surface.jpg")
        self.button1 = pygame.image.load("run/game_start_up.png")
        self.button2 = pygame.image.load("run/game_start_down.png")
        self.button3 = pygame.image.load("run/again_up.jpg")
        self.button4 = pygame.image.load("run/again_down.jpg")
        self.gameover = pygame.image.load("run/gameover.jpg")
        self.prop = pygame.image.load("run/fruit.bmp")
        self.screen = _screen
        self.px = 700
        self.py = 150

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))
        if self.x < -800:
            self.x = 800
        else:
            self.x -= 5

    def move(self):
        self.show()

    #def prop(self, _flag):
    #    if _flag == 0:
    #        chance = random.randint(0, 30000)
    #    if chance == 30000:
    #        _flag = 1
#
    #def prop_true(self):
    #    self.screen.blit(self.prop, (self.px, self.py))
    #    self.px -= 2
    #    if self.py - 20 < player.y < self.py and self.px < player.x < self.px + 75:
    #        player.x += 10


class Dragon(object):
    def __init__(self, _screen):
        self.tick = 0
        self.image = pygame.image.load("run/long.png")
        self.image_fire = pygame.image.load("run/long_fire.png")
        self.fire = pygame.image.load("run/bullet.jpg")
        self.screen = _screen
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.x = 10
        self.y = 366 - self.height + 10
        self.bx = self.x + self.width
        self.by = self.y + 58

    def show(self, _tick):
        if _tick % 50 < 25:
            self.screen.blit(self.image, (self.x, self.y))
        else:
            self.screen.blit(self.image, (self.x, self.y-10))


class Player(object):
    def __init__(self, _screen):
        self.image1 = pygame.image.load("run/player1.png")
        self.image2 = pygame.image.load("run/player2.png")
        self.image3 = pygame.image.load("run/player3.png")
        self.image4 = pygame.image.load("run/player4.png")
        self.rect = self.image1.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.x = 400
        self.y = 366 - self.height + 10
        self.flag = 0
        self.screen = _screen

    def move(self, _tick):
            if _tick % 50 < 25:
                self.screen.blit(self.image2, (self.x, self.y))
            else:
                self.screen.blit(self.image1, (self.x, self.y))

    def hit(self):  # 被火球击中后后退
        if self.x < dragon.bx and dragon.bx + 30 < self.x + self.width:
            if dragon.by - 30 < self.y or dragon.by < self.y + self.height:
                self.x -= 10

    def die(self, _mx, _my, _m1):  # 结算界面
        self.screen.blit(background1.gameover, (0, 0))
        if 320 < _mx < 476 and 230 < _my < 272:
            self.screen.blit(background1.button4, (320, 230))
            if _m1 == 1:
                _start = 0
        else:
            self.screen.blit(background1.button3, (320, 230))

    def restart(self):  # 重新开始游戏
        self.x = 400


font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 26)
text = font.render("Score:", True, (200, 200, 200))
background1 = Background(screen, 0, 0)
background2 = Background(screen, 800, 0)
dragon = Dragon(screen)
player = Player(screen)
judge = 0
tick = 0
speed = -12
start = 0
shoot = 0
score = 0
flag = 0
chance = 0
speed_fire = 5
while True:
    # 鼠标轮询
    mx, my = pygame.mouse.get_pos()
    m1, m2, m3 = pygame.mouse.get_pressed()
    clock.tick(60)    # 60帧
    if start == 0:  # 开始界面
        screen.blit(background1.first, (0, 0))
        if 250 < mx < 550 and 500 < my < 541:
            screen.blit(background1.button2, (250, 500))
            if m1:
                start = 1
        else:
            screen.blit(background1.button1, (250, 500))
    else:
        background1.move()
        background2.move()

    if judge == 0:
        player.move(tick)
        tick += 1
    else:  # 跳跃
        player.y += speed
        speed += 0.3
        screen.blit(player.image3, (player.x, player.y))
        if player.y > 276:
            judge = 0
            player.y = 276
            speed = -12
    if m1:
        judge = 1
    if start == 1:  # 游戏界面
        dragon.show(tick)
        number = random.randint(0, 100)  # 火球发射判断
        if number == 100:
            shoot = 1
        if shoot:
            dragon.bx += speed_fire
            screen.blit(dragon.fire, (dragon.bx, dragon.by))
        if dragon.bx > 835:
            score += 1
            shoot = 0
            dragon.bx = dragon.x + dragon.width
        screen.blit(text, (660, 0))
        text_score = font.render(str(score), True, (200, 200, 200))
        screen.blit(text_score, (740, 0))
        player.hit()
        if flag == 0:  # 道具判定
            chance = random.randint(0, 3)
        if chance == 3:
            flag = 1
        if flag:
            screen.blit(background1.prop, (background1.px, background1.py))
            background1.px -= 5
            if background1.py - 20 < player.y < background1.py or background1.py - 20 < player.y - player.height < background1.py:
                if background1.px < player.x + player.width // 2 < background1.px + 75:
                    score += 1
                    if player.x < 500:
                        player.x += 10  # 吃到道具向前移动
                    background1.px = 820
                    flag = 0
                if background1.px < -80:
                    flag = 0
                    background1.px = 820
        if score // 1 == 1:  # 速度变换
            speed_fire = 6
        if score // 1 == 2:
            speed_fire = 7
        if score // 1 == 3:
            speed_fire = 8
        if score // 1 == 4:
            speed_fire = 9
        if score // 1 == 5:
            speed_fire = 10
        if score // 1 == 6:
            speed_fire = 11
        if player.x < dragon.x + dragon.width:  # 结算界面
            player.die(mx, my, m1)
            if 320 < mx < 476 and 230 < my < 272:
                if m1 == 1:
                    start = 0
                    score = 0
                    player.restart()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()

