import pygame as py
py.init()
screen=py.display.set_mode((800,800))
DesireDoueimage=py.image.load("Desire_Duoe-removebg-preview.png")
DesireDoueimage=py.transform.scale(DesireDoueimage,(100,100))
DesireDouesprite=DesireDoueimage.get_rect()
DesireDouesprite.center=(100,100)

LJimage=py.image.load("LJ-removebg-preview.png")
LJimage=py.transform.scale(LJimage,(100,100))
LJsprite=LJimage.get_rect()
LJsprite.center=(100,300)

Tennisimage=py.image.load("Tennis-removebg-preview.png")
Tennisimage=py.transform.scale(Tennisimage,(100,100))
Tennissprite=Tennisimage.get_rect()
Tennissprite.center=(100,500)

BALLimage=py.image.load("BALL-removebg-preview.png")
BALLimage=py.transform.scale(BALLimage,(100,100))
BALLsprite=BALLimage.get_rect()
BALLsprite.center=(550,100)

BASKETBALLimage=py.image.load("BASKETBALL-removebg-preview.png")
BASKETBALLimage=py.transform.scale(BASKETBALLimage,(100,100))
BASKETBALLsprite=BASKETBALLimage.get_rect()
BASKETBALLsprite.center=(550,300)

TENNISBALLimage=py.image.load("TENNISBALL-removebg-preview.png")
TENNISBALLimage=py.transform.scale(TENNISBALLimage,(100,100))
TENNISBALLsprite=TENNISBALLimage.get_rect()
TENNISBALLsprite.center=(550,500)
running=True
while running:
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
        screen.fill("navyblue")
        screen.blit(DesireDoueimage,DesireDouesprite)
        screen.blit(LJimage,LJsprite)
        screen.blit(Tennisimage,Tennissprite)
        screen.blit(BALLimage,BALLsprite)
        screen.blit(BASKETBALLimage,BASKETBALLsprite)
        screen.blit(TENNISBALLimage,TENNISBALLsprite)
        py.display.update()
        
py.QUIT()