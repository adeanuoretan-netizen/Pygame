import pygame as py
py.init()
screen=py.display.set_mode((500,500))
py.display.set_caption("Liverpool and PSG")
psgimage=py.image.load("Paris_saint_german-removebg-preview.png")
psgimage=py.transform.scale(psgimage,(50,50))
psgsprite=psgimage.get_rect()
psgsprite.center=(250,250)
liverpoolimage=py.image.load("Liverpool-Logo-PNG-Pic-removebg-preview.png")
liverpoolimage=py.transform.scale(liverpoolimage,(250,250))
liverpoolsprite=liverpoolimage.get_rect()
liverpoolsprite.center=(250,250)
running=True
while running:
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
    keys=py.key.get_pressed()
    if keys[py.K_LEFT]:
        liverpoolsprite.x=liverpoolsprite.x-1
    if keys[py.K_RIGHT]:
         liverpoolsprite.x=liverpoolsprite.x+1
    if keys[py.K_UP]:
        liverpoolsprite.y=liverpoolsprite.y-1
    if keys[py.K_DOWN]:
        liverpoolsprite.y=liverpoolsprite.y+1


    screen.fill("blue")
    screen.blit(psgimage,psgsprite)
    screen.blit(liverpoolimage,liverpoolsprite)
    py.display.update()
py.quit()