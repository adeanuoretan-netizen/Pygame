import pygame as py
py.init()
screen=py.display.set_mode((800,800))
py.display.set_caption("Flappy Bird")
running=True
birdimage=py.image.load("flappy-bird-no-background-11549936960agq8fxhfbr-removebg-preview.png")
birdimage=py.transform.scale(birdimage,(70,70))
birdsprite=birdimage.get_rect()
pipe1image=py.image.load("6d2a698f31595a1-removebg-preview.png")
pipe1image=py.transform.scale(pipe1image,(100,400))
pipe1image=py.transform.rotate(pipe1image,180)
pipe1sprite=birdimage.get_rect()
pipe2image=py.image.load("6d2a698f31595a1-removebg-preview.png")
pipe2image=py.transform.scale(pipe2image,(100,400))
pipe2sprite=birdimage.get_rect()
pipe3image=py.image.load("6d2a698f31595a1-removebg-preview.png")
pipe3image=py.transform.scale(pipe3image,(100,400))
pipe3image=py.transform.rotate(pipe3image,180)
pipe3sprite=birdimage.get_rect()
pipe4image=py.image.load("6d2a698f31595a1-removebg-preview.png")
pipe4image=py.transform.scale(pipe4image,(100,400))
pipe4sprite=birdimage.get_rect()

pipe1sprite.center=(250,0)
pipe2sprite.center=(250,600)
pipe3sprite.center=(600,-150)
pipe4sprite.center=(600,500)
by=300
birdsprite.center=(50,by)
velocity=-1
score=0
font1=py.font.SysFont("Arial", 30)
text1= font1.render("Score: " + str(score), True, "black")
gravity=0.5

while running:
    pipe1sprite.x=pipe1sprite.x+velocity
    pipe2sprite.x=pipe2sprite.x+velocity  
    pipe3sprite.x=pipe3sprite.x+velocity 
    pipe4sprite.x=pipe4sprite.x+velocity 
    by=by+gravity 
    if pipe1sprite.x<0:
         pipe1sprite.x=800
         pipe2sprite.x=800
    if pipe3sprite.x<0:
             pipe3sprite.x=800
             pipe4sprite.x=800

      
    for event in py.event.get():
            if event.type==py.QUIT:
                running=False
    screen.fill("light blue")
    screen.blit(birdimage,birdsprite)
    birdsprite.center=(50,by)
    screen.blit(pipe1image,pipe1sprite)
    screen.blit(pipe2image,pipe2sprite)
    screen.blit(pipe3image,pipe3sprite)
    screen.blit(pipe4image,pipe4sprite)
    screen.blit(text1,(300,100))

    py.display.update()
    

py.quit()
    