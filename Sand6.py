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
fluidParticles2=[]
drawtool=[]
lineW=4
mx2=0
my2=0
def spawnFluid(mx,my):
    global fluidParticles
    #if len(fluidParticles)>1000:
        #fluidParticles=fluidParticles[1:]
    fluidParticles.append([mx,my,0])
def drawFluids(fluids):
    changey=1
    for i in range(0,len(fluidParticles)):
        change=randint(-90,90)
        xOriginal=fluidParticles[i][0]
        yOriginal=fluidParticles[i][1]
        if screen.get_at((xOriginal,yOriginal+1))==(0,0,0,255):
            fluidParticles[i][1]+=2
        else:# screen.get_at((xOriginal,yOriginal+1))!=(0,0,0,255):
            fluidParticles[i][1]-=1
        if change>=1:
            if screen.get_at((xOriginal+2,yOriginal+1))==(0,0,0,255):
                fluidParticles[i][0]+=1
            elif screen.get_at((xOriginal-2,yOriginal+1))==(0,0,0,255):
                fluidParticles[i][0]-=1
        else:
            if screen.get_at((xOriginal-2,yOriginal+1))==(0,0,0,255):
                fluidParticles[i][0]-=1
            elif screen.get_at((xOriginal+2,yOriginal+1))==(0,0,0,255):
                fluidParticles[i][0]+=1
        if screen.get_at((xOriginal,yOriginal-5))==(255,255,255,255):
            fluidParticles[i][1]=yOriginal
        #screen.set_at((fluidParticles[i][0],fluidParticles[i][1]), (70,140,155))
        draw.circle(screen,(70,140,155),(fluidParticles[i][0],fluidParticles[i][1]),1)
screen.fill((0,0,0))
screen2=screen.copy()
while running:
    screen.fill((0,0,0))
    clock=time.Clock()
    clock.tick(100)
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    changeX=(mx-mx2)
    changeY=(my-my2)
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    screen.blit(screen2,(0,0))
    draw.line(screen,(100,100,200),(0,600),(800,600),50)
    if 1==mb[2]:
        for x in range(0,2):
            for i in range(1,int((changeX**2+changeY**2)**.5)):
                xCoords=mx2+(i*(changeX))/int((changeX**2+changeY**2))**.5
                yCoords=my2+(i*(changeY))/int((changeX**2+changeY**2))**.5
                draw.circle(screen,(255,255,255),(int(xCoords),int(yCoords)),int(lineW/2))
    screen2=screen.copy()
    if 1 == mb[0]:
        for i in range(0,1):
            spawnFluid(mx,my)
            spawnFluid(mx+4,my+4)
            spawnFluid(mx-4,my-4)
            spawnFluid(mx-4,my+4)
            spawnFluid(mx+4,my-4)
    if mx2!=mx:
        mx2=mx
    if my2!=my:
        my2=my
    drawFluids(fluidParticles)
    display.flip()
quit()
