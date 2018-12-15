# -*- coding: UTF-8 -*-
class Point:
    row =0
    col =0
    def __init__(self,row,col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(row=self.row, col=self.col)
#初始框架
import pygame
import random

#初始化
pygame.init()
W = 800
H = 600

ROW=30
COL=40

size = (W,H)
window = pygame.display.set_mode(size)
pygame.display.set_caption('贪吃蛇')

bg_color = (255,255,255)

#生成食物
def gen_food():
    while 1:
        pos = Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))

        is_coll=False
        #是否碰上蛇
        if head.row==pos.row and head.col==pos.col:
            is_coll=True
        for snake in snakes:
            if snake.row==pos.row and snake.col==pos.col:
                is_coll=True
                break
        if not is_coll:
            break
    return pos

#定义坐标
head = Point(row=int(ROW/2),col=int(COL/2))
head_color =(0,128,128)
#food = Point(row=2,col=3)
#随机食物位置
food = Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))
food_color = (255,255,0)

snakes=[
    Point(row=head.row,col=head.col+1),
    Point(row=head.row,col=head.col+2),
    Point(row=head.row,col=head.col+3)
]
snake_color =(128,128,128)
direct="left"

def rect(point,color):
    cell_width=W/COL
    cell_height=H/ROW
    left = point.col*cell_width
    top = point.row*cell_height

    pygame.draw.rect(
        window, color,
        (left,top,cell_width,cell_height)
    )

#游戏循环
quit = True
clock = pygame.time.Clock()
while quit:
    #处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.key==273 or event.key==119:
                if direct=='left' or direct=='right':
                    direct='up'
            elif event.key==274 or event.key==115:
                if direct == 'left' or direct == 'right':
                    direct='down'
            elif event.key==276 or event.key==97:
                if direct == 'up' or direct == 'down':
                    direct='left'
            elif event.key==275 or event.key==100:
                if direct == 'up' or direct == 'down':
                    direct='right'
    #吃东西
    eat =(head.row==food.row and head.col==food.col)
    #重新产生食物
    if eat:
        food = Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))
    #处理身子：
    ## 1.把原来的头插入到snakes的头上；
    snakes.insert(0,head.copy())
    ##2.把snakes的最后一个删掉
    if not eat:
        snakes.pop()
    #移动
    if direct=='left':
        head.col -= 1
    elif direct=='right':
        head.col += 1
    elif direct=='up':
        head.row-=1
    elif direct=='down':
        head.row+=1
    #检测：
    dead = False
    #1.撞墙
    if head.col<0 or head.row<0 or head.col>=COL or head.row>=ROW:
        dead = True
    #2.撞自己
    for snake in snakes:
        if head.col==snake.col and head.row==snake.row:
            dead=True
            break

    if dead:
        print('dead')
        quit=False

    #渲染
    pygame.draw.rect(window,(255,255,255),(0,0,W,H))
    #画蛇头、食物
    rect(head,head_color)
    rect(food,food_color)
    ##画蛇身
    for snake in snakes:
        rect(snake,snake_color)
    #让渡控制权
    pygame.display.flip()

    #设置帧频
    clock.tick(60)
