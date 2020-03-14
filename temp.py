import pygame
import numpy as np
import pygame.surfarray as sfr
import time
import random
import math
from sys import exit



class klocek():
    def __init__(self,actual):
        self.h=10
        self.z=9

        self.ee=np.array([255,255,100])
        self.col=actual
    def left(self):
        self.z=self.z-1
        if self.z<10:
            self.z=19

    def right(self):
        self.z = self.z + 1
        if self.z>19:
            self.z=0
    def lower(self):
        if self.h<89 :
            actual[self.z][self.h]=[0,0,0]
        self.h=self.h+1
        if self.h>89:
            self.h=10
            a.right()
        elif actual[self.z][self.h][2]==100:
            if self.h<30:
                pygame.quit()

            actual[self.z][self.h-1][0]=250
            actual[self.z][self.h - 1][1] = 250
            actual[self.z][self.h - 1][2] = 100
            self.h = 10
            a.right()



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


conv(actual,scr)
sfr.make_surface(scr)


actual = np.zeros((20, 90, 3))
a=klocek(actual)
Running=True
while Running:

    for i in range(len(actual[1])):
        flag=True
        for j in range(len(actual)):
            if actual[j][i][2]!=100:
                flag=False

        if flag == True:
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
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    a.lower()
    if keys[pygame.K_a]:
        a.left()
    if keys[pygame.K_d]:
        a.right()

    #pygame.time.wait(10)


