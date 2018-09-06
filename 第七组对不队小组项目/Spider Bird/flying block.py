import pygame
import random
pygame.init()



PIPE = (0,0,255)
BIRD = (220,20,60)
gameState = 1
pipes=[]


screen=pygame.display.set_mode((800,650))
font=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",40)
pygame.display.set_caption("Flappy Block")
bk=pygame.image.load("bk1.jpg")
ready=pygame.image.load("text_ready.png")
gmover=pygame.image.load("text_game_over.png")

class Bird(object):
    def __init__(self):
        self.x = 250  # 小鸟x坐标
        self.y = 250  # 小鸟y坐标
        self.yV = 0  # 小鸟的位置初始化

    # 定义小鸟的下降振幅
    def flap(self):
        self.yV =-7# 每次下降的位移


    def update(self):    # 定义小鸟的上升振幅和y轴的上下边界
        self.yV += 0.2  # 小鸟上升速度
        self.y += self.yV  # y轴位置等于原位置加yV振幅

    # 定义小鸟的飞行
    def draw(self):
        pygame.draw.rect(screen, BIRD, (self.x, self.y, 40, 40))  # 参数为（幕布，颜色，坐标，大小）
    # 重置小鸟
    def reset(self):
        self.x = 250
        self.y = 250
        self.yV = 0

bird = Bird()

class Pipe(object):
    def __init__(self):
        self.centerY = random.randint(190, 520)# 管子的y轴中间值范围
        self.x=800
        self.size=150# 管子空隙
    def update(self):
        global pipes
        global bird
        global gameState
        self.x -= 2 # 管子的移动速度，因为小鸟其实没有动x轴的位移，小鸟其实是不前进的，只是上下跳动
        # 管子的初始位置
        if self.x == 300:
            pipes.append(Pipe())  # 显示一个新管子
        if self.x <= -100:
            del pipes[0]  # 删除一个不再显示的管子
        if self.x >= 170 and self.x <= 290 and bird.y <= (self.centerY - self.size) or self.x >= 170 and self.x <= 290 and bird.y>= (self.centerY + self.size-40):
            gameState = 3 # 结束
            # 小鸟飞过管子，游戏继续，两个75等于size的150
        if self.x == 170 and bird.y > (self.centerY - 75) and bird.y < (self.centerY + 75):
            gameState = 2
            # 小鸟撞到地面，游戏结束
        if bird.y >= 610 or bird.y<0:
            gameState = 3

    def draw(self):  # 定义上面管子的显示（幕布，颜色，坐标，宽=80，长）
        # 定义上面管子的显示（幕布，颜色，坐标，宽=80，长）
        pygame.draw.rect(screen, PIPE, (self.x, 0, 80, (self.centerY - self.size)))
        # 定义下面管子的显示
        pygame.draw.rect(screen, PIPE, (self.x, (self.centerY + self.size), 80, (548 - self.centerY)))
        # 实例化管子，显示新管子
pipes.append(Pipe())




while True:

    screen.blit(bk,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # 设置为空格键
                if gameState==1:
                    gameState = 2  # 游戏中状态为2
                elif gameState == 3:  # 游戏结束状态为3
                    bird.reset()  # 小鸟重置
                    pipes=[] # 管子list重置
                    pipes.append(Pipe())
                    gameState = 2
                else:  # 没有管子的时候，小鸟飞行
                    bird.flap()

    if gameState == 1:  # 游戏未开始时
        screen.blit(ready,(300,300))
    if gameState == 2: # 当游戏运行中
        # 小鸟的飞行更新
        bird.update()
        bird.draw()
        # 管子的更新显示
        for pipe in pipes:
            pipe.update()
            pipe.draw()
        # 当游戏结束
    if gameState == 3:
        for pipe in pipes:
            pipe.draw()
            bird.draw()
            screen.blit(gmover,(300,300))



    pygame.display.update()
