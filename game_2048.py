import os
import sys
import numpy
import random
import pygame
"""
Form(): window settings
Action(): action: keyboard/mouse
InitGame(): initializatin
CreatNum(): generate a number 
GetEmpty(): get empty block
MoveUp(): move up 
MoveDown(): move down
MoveLeft(): move left
MoveRight(): move right
JudgeGameOver(): whether game ends
JudgeGameSuccess(): whether game success
Paint(): plot 
"""

class game_2048(object):
    def __init__(self,screen_width,screen_height,block_gap,block_size,block_arc):
        self.screen_width=screen_height
        self.screen_height=screen_height
        self.block_gap=block_gap
        self.block_size=block_size
        self.block_arc=block_arc
        self.size=4
        self.matrix=[]
        self.form=''
        self.is_over=False
        self.is_success=False
        self.score=0
        self.isadd=True
        self.block_color={
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46)
        }
        self.nums_color={
            0: (205, 193, 180),
            2: (0, 0, 0),
            4: (0, 0, 0),
            8: (255, 255, 255),
            16: (255, 255, 255),
            32: (255, 255, 255),
            64: (255, 255, 255),
            128: (255, 255, 255),
            256: (255, 255, 255),
            512: (255, 255, 255),
            1024: (255, 255, 255),
            2048: (255, 255, 255)
        }
        self.title_font=''
        self.score_font=''
        self.tips_font=''
        self.font=''

    def Form(self):
        pygame.init()
        pygame.display.set_caption("2048")
        os.environ['SDL_VIDEO_CENTERED']='1'
        self.form=pygame.display.set_mode([self.screen_width,self.screen_height],0,0)
        self.InitGame()
        while True:
            self.Action()
            self.Paint()
            pygame.display.update()

    def Action(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    self.InitGame()
                if event.key==pygame.K_UP and self.is_over==False:
                    self.MoveUp()
                if event.key==pygame.K_DOWN and self.is_over==False:
                    self.MoveDown()
                if event.key==pygame.K_LEFT and self.is_over==False:
                    self.MoveLeft()
                if event.key==pygame.K_RIGHT and self.is_over==False:
                    self.MoveRight()

    def InitGame(self):
        self.score=0
        self.is_over=False
        self.is_success=False
        self.matrix=numpy.zeros([self.size,self.size])
        for i in range(2):
            self.isadd=True
            self.CreateNum()

    def CreateNum(self):
        list=self.GetEmpty()
        if list and self.isadd:
            value=4 if random.randint(0,3)%3==0 else 2
            x,y=random.sample(list,1)[0]
            self.matrix[x][y]=value
            self.isadd=False

    def GetEmpty(self):
        list=[]
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j]==0:
                    list.append([i,j])
        return list

    def MoveUp(self):
        for j in range(4):
            index=0
            for i in range(1,4):
                if self.matrix[i][j]>0:
                    if self.matrix[i][j]==self.matrix[index][j]:
                        self.score=self.score+self.matrix[i][j]+self.matrix[index][j]
                        self.matrix[index][j]=self.matrix[i][j]+self.matrix[index][j]
                        self.matrix[i][j]=0
                        index+=1
                        self.isadd=True
                    elif self.matrix[index][j]==0:
                        self.matrix[index][j]=self.matrix[i][j]
                        self.matrix[i][j]=0
                        self.isadd=True
                    else:
                        index+=1
                        if self.matrix[index][j]==0:
                            self.matrix[index][j]=self.matrix[i][j]
                            self.matrix[i][j]=0
                            self.isadd=True

    def MoveDown(self):
        for j in range(4):
            index=3
            for i in range(2,-1,-1):
                if self.matrix[i][j]>0:
                    if self.matrix[i][j]==self.matrix[index][j]:
                        self.score=self.score+self.matrix[i][j]+self.matrix[index][j]
                        self.matrix[index][j]=self.matrix[i][j]+self.matrix[index][j]
                        self.matrix[i][j]=0
                        index-=1
                        self.isadd=True
                    elif self.matrix[index][j]==0:
                        self.matrix[index][j]=self.matrix[i][j]
                        self.matrix[i][j]=0
                        self.isadd=True
                    else:
                        index-=1
                        if self.matrix[index][j]==0:
                            self.matrix[index][j]=self.matrix[i][j]
                            self.matrix[i][j]=0
                            self.isadd=True

    def MoveLeft(self):
        for i in range(4):
            index=0
            for j in range(1,4):
                if self.matrix[i][j]>0:
                    if self.matrix[i][j]==self.matrix[i][index]:
                        self.score+=self.matrix[i][j]+self.matrix[index][j]
                        self.matrix[i][index]=self.matrix[i][j]+self.matrix[i][index]
                        self.matrix[i][j]=0
                        index+=1
                        self.isadd=True
                    elif self.matrix[i][index]==0:
                        self.matrix[i][index]=self.matrix[i][j]
                        self.matrix[i][j]=0
                        self.isadd=True
                    else:
                        index+=1
                        if self.matrix[i][index]==0:
                            self.matrix[i][index]=self.matrix[i][j]
                            self.matrix[i][j]=0
                            self.isadd=True

    def MoveRight(self):
        for i in range(4):
            index=3
            for j in range(2,-1,-1):
                if self.matrix[i][j]>0:
                    if self.matrix[i][j]==self.matrix[i][index]:
                        self.score+=self.matrix[i][j]+self.matrix[index][j]
                        self.matrix[i][index]=self.matrix[i][j]+self.matrix[i][index]
                        self.matrix[i][j]=0
                        index-=1
                        self.isadd=True
                    elif self.matrix[i][index]==0:
                        self.matrix[i][index]=self.matrix[i][j]
                        self.matrix[i][j]=0
                        self.isadd=True
                    else:
                        index-=1
                        if self.matrix[i][index]==0:
                            self.matrix[i][index]=self.matrix[i][j]
                            self.matrix[i][j]=0
                            self.isadd=True

    def JudgeGameOver(self):
        zerolist=self.GetEmpty()
        if zerolist:
            return False
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j]==self.matrix[i][j+1]:
                    return False
                if self.matrix[i][j]==self.matrix[i+1][j]:
                    return False
        return True

    def JudgeGameSuccess(self):
        if self.matrix.max()==2e16:
            return True

    def Paint(self):
        self.form.fill((220,220,220))
        pygame.font.init()
        #title
        self.title_font=pygame.font.SysFont('幼圆',50,True)
        title_text=self.title_font.render('2048',True,(0,0,0))
        self.form.blit(title_text,(50,10))
        #add score
        pygame.draw.rect(self.form,(128,128,128),(250,0,120,60))
        self.score_font=pygame.font.SysFont('幼圆',28,True)
        score_text=self.score_font.render('Score:',True,(0,0,0))
        self.form.blit(score_text,(275,0))
        digital_score=self.score_font.render(str(int(self.score)),True,(255,250,250))
        self.form.blit(digital_score,(280,30))
        #game explanation
        self.tips_font=pygame.font.SysFont('simsunnsimsun',20)
        tips_next=self.tips_font.render('Game Control:up,down,left,right,press esc to restart',True,(0,0,0))
        self.form.blit(tips_next,(25,70))
        for i in range(4):
            for j in range(4):
                x=j*self.block_size+(j+1)*self.block_gap
                y=i*self.block_size+(i+1)*self.block_gap
                value=int(self.matrix[i][j])
                pygame.draw.rect(self.form,self.block_color[value],(x+5,y+100,self.block_size,self.block_size),border_radius=self.block_arc)
                #number font(size)
                if value<10:
                    self.font=pygame.font.SysFont('simsunnsimsun',46,True)
                    value_text=self.font.render(str(value),True,self.nums_color[value])
                    self.form.blit(value_text,(x+35,y+120))
                elif value<100:
                    self.font = pygame.font.SysFont('simsunnsimsun', 40, True)
                    value_text = self.font.render(str(value), True, self.nums_color[value])
                    self.form.blit(value_text, (x + 25, y + 120))
                elif value<1000:
                    self.font = pygame.font.SysFont('simsunnsimsun', 34, True)
                    value_text = self.font.render(str(value), True, self.nums_color[value])
                    self.form.blit(value_text, (x + 15, y + 120))
                else:
                    self.font = pygame.font.SysFont('simsunnsimsun', 28, True)
                    value_text = self.font.render(str(value), True, self.nums_color[value])
                    self.form.blit(value_text, (x + 5, y + 120))
        self.CreateNum()
        #gameover
        self.is_over=self.JudgeGameOver()
        if self.is_over:
            over_font=pygame.font.SysFont("simsunnsimsun",60,True)
            str_text=over_font.render('GAME OVER!',True,(178,34,34))
            self.form.blit(str_text,(30,220))
        self.is_success=self.JudgeGameSuccess()
        if self.is_success:
            success_font=pygame.font.SysFont("simsunnsimsun",60,True)
            str_text=success_font.render("YOU SUCCEED!",True,(178,34,34))
            self.form.blit(str_text,(10,220))
