import pygame as py
py.init()
screen=py.display.set_mode((500,500))
py.display.set_caption("My First Screen")
bgimage=py.image.load("blr isagi.jpg")
bgimage=py.transform.scale(bgimage,(500,500))
running=True
while running:
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
    screen.fill("blue")
    screen.blit(bgimage,(0,0))
    py.display.update()


py.quit()