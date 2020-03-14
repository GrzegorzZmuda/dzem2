import pygame
import numpy as np
import pygame.surfarray as sfr
import time
import random
import math
from sys import exit
#autopilot
N=1


class klocek():
    def __init__(self,actual):
        self.h=10
        self.z=9
<<<<<<< Updated upstream
        #self.shape=[[1,1][1,1]]
=======

>>>>>>> Stashed changes
        self.ee=np.array([255,255,100])
        self.col=actual
    def left(self):
        if self.z>0 and actual[self.z-1][self.h][2]!=100:
            self.z=self.z-1
        if self.z==0 and actual[19][self.h][2]!=100:
            self.z=self.z-1
        if self.z<0:
            self.z=19

    def right(self):
        if self.z<19 and actual[self.z+1][self.h][2] != 100:
            self.z = self.z + 1
        elif self.z==19 and actual[0][self.h][2] != 100:
            self.z = self.z + 1
        if self.z>19:
            self.z=0
    def lower(self,wyn):
        if self.h<89 :

            actual[self.z][self.h]=[0,0,0]
        self.h=self.h+1
        if self.h>89:
            self.h=10
            if N==0:
                a.right()
        elif actual[self.z][self.h][2]==100:
            if self.h<30:
                pygame.quit()

            actual[self.z][self.h-1][0]=250
            actual[self.z][self.h - 1][1] = 250
            actual[self.z][self.h - 1][2] = 100
            self.h = 10
            if N==0:
                a.right()
        rand=random.randint(0,100)
        if rand<wyn:

            side = random.randint(1, 2)
            if side==1:
                a.right()
            else:
                a.left()


def checkbounds(a,b):
    if a>0 and a<19 and b>0 and b<89:
        return True
    else:
        return False

def conv(a,b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j][0]=a[int(i//8)][int(j//8)][0]
            b[i][j][1] = a[int(i // 8)][int(j // 8)][1]
            b[i][j][2] = a[int(i // 8)][int(j // 8)][2]

def loweractual(actual,t):
    return np.roll(actual, 1, axis=1)


actual = np.ndarray((20,90,3))
scr =np.ndarray((160,720,3))

pygame.init()
screen = pygame.display.set_mode((160,720))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

score=0
conv(actual,scr)
sfr.make_surface(scr)
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render(str(score), True, (200,200,200), (0,0,0))
textRect = text.get_rect()

textRect.center = (0,0)

actual = np.zeros((20, 90, 3))
a=klocek(actual)
Running=True
while Running:
    text = font.render(str(score), True, (200, 200, 200), (0, 0, 0))
    for i in range(len(actual[1])):
        flag=True
        for j in range(len(actual)):
            if actual[j][i][2]!=100:
                flag=False

        if flag == True:
            score=score+1
            for k in range(len(actual)):

                actual[k][i][0]=0
                actual[k][i][1]=0
                actual[k][i][2]=0
            actual=loweractual(actual,i)

    actual[a.z][a.h][0]=a.ee[0]
    actual[a.z][a.h][1] = a.ee[1]
    actual[a.z][a.h][2] = a.ee[2]
    surf = pygame.surfarray.make_surface(actual)
    screen.blit(pygame.transform.scale(surf, (160, 720)), (0, 0))
    screen.blit(text,(0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    a.lower(score)
    if keys[pygame.K_a]:
        a.left()
    if keys[pygame.K_d]:
        a.right()
    if not keys[pygame.K_s]:
        pygame.time.wait(30)



