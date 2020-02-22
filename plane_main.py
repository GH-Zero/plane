import pygame
import time
from pygame.locals import *
import random
class BasePlane(object):
    def __init__(self,screen,x,y,image):
        self.x=x
        self.y=y
        self.screen=screen
        self.image=pygame.image.load(image)
        self.bullit_list=[]#子弹收集
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for i in self.bullit_list:
            i.dispaly()
            i.move()
            if i.judge():
                self.bullit_list.remove(i)
class Heroplane(BasePlane):
    def __init__(self,screen):
        BasePlane.__init__(self,screen,160,615,'./peotol/b1.png')
    def move_lift(self):
        self.x-=10
    def move_right(self):
        self.x+=10
    def fire(self):
        self.bullit_list.append(Built(self.screen,self.x,self.y))
class Enpyplane(BasePlane):
    def __init__(self,screen):
        BasePlane.__init__(self, screen, 0, 0, './peotol/u2.jpg')
        self.conton="right"
    def move(self):
        if self.conton=='right':
            self.x+=1
        elif self.conton=='left':
            self.x-=1
        if self.x>350:
            self.conton='left'
        elif self.x<0:
            self.conton='right'
    def fire(self):
        random_num=random.randint(1,200)
        if random_num ==10 or random_num==50:
            self.bullit_list.append(EnemyBuilt(self.screen,self.x,self.y))

class BaseBuilt(object):
    def __init__(self, screen, x, y,image):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image)
    def dispaly(self):
        self.screen.blit(self.image,(self.x,self.y))
class Built(BaseBuilt):
    def __init__(self,screen,x,y):
        BaseBuilt.__init__(self,screen,x+22,y-20,'./peotol/z2.png')
    def move(self):
        self.y-=10
    def judge(self):
        if self.y<0:
            return True
        else:
            return False
class EnemyBuilt(BaseBuilt):
    def __init__(self,screen,x,y):
        BaseBuilt.__init__(self,screen,x+20,y+40,'./peotol/z1.png')
    def move(self):
        self.y+=2
    def judge(self):
        if self.y>680:
            return True
        else:
            return False
def Coon(hero_n):
    for i in pygame.event.get():
        if i.type == QUIT:
            print('exit')
            exit()
        elif i.type == KEYDOWN:
            if i.key == K_a or i.key == K_LEFT:
                print('lift')
                hero_n.move_lift()
            elif i.key == K_d or i.key == K_RIGHT:
                print('right')
                hero_n.move_right()
            elif i.key == K_SPACE:
                print('space')
                hero_n.fire()
def main():
    #创建窗口
    screen=pygame.display.set_mode((394,700),0,32)
    #创建背景
    background=pygame.image.load('./peotol/u.jpg')
    #创建飞机对象
    hero=Heroplane(screen)
    #创建敌机
    enpy=Enpyplane(screen)
    while True:
        #背景、飞机坐标
        screen.blit(background,(0,0))
        hero.display()
        enpy.display()
        enpy.move()
        enpy.fire()
        #刷新
        pygame.display.update()
        time.sleep(0.01)
        Coon(hero)

if __name__ == '__main__':
    main()