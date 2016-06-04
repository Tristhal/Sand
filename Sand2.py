from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((800,600))  #
running=True                        #
cx,cy=400,300                       #
#####################################
screen.fill((250,245,250))
fluidParticles=[]
fuildParticles2=[]
drawtool=[]
def spawnFluid(mx,my):
    global fluidParticles
    fluidParticles.append([mx,my,randint(-1,1)])
def drawFluids(fluids):
    changey=1
    for i in range(0,len(fluidParticles)):
        changex=randint(-1,1)
        if screen.get_at((fluidParticles[i][0]+changex,fluidParticles[i][1]+changey))==(0,0,0,255):
            fluidParticles[i][1]+=changey
            fluidParticles[i][0]+=changex
        elif screen.get_at((fluidParticles[i][0]+changex,fluidParticles[i][1]))==(0,0,0,255):
            fluidParticles[i][0]+=changex
        draw.circle(screen,(255,255,255),(fluidParticles[i][0],fluidParticles[i][1]),2)
while running:
    screen.fill((0,0,0))
    clock=time.Clock()
    clock.tick(1000)
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    draw.line(screen,(100,100,200),(0,600),(800,600),50)
    for i in range(0,len(drawtool)):
        draw.circle(screen,(200,100,100),(drawtool[i][0],drawtool[i][1]),10)
    if 1 == mb[0]:
        for i in range(0,1):
            spawnFluid(mx,my)
    if 1==mb[2]:
        drawtool.append([mx,my])

    drawFluids(fluidParticles)
    display.flip()
quit()
