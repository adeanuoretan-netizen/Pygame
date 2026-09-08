import pygame as py
py.init()
screen=py.display.set_mode((800,800))
py.display.set_caption("birthday card")
running=True
while running:
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
    screen.fill("blue")
    py.display.update()
py.quit()