import pygame as py
import time
py.init()
py.mixer.init()
screen=py.display.set_mode((800,800))
py.display.set_caption("Flappy Bird")
running=True
birdimage=py.image.load("flappy-bird-no-background-11549936960agq8fxhfbr-removebg-preview.png")
birdimage=py.transform.scale(birdimage,(40,40))
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
p1x=250
p2x=250
p3x=600
p4x=600
pipe1sprite.center=(p1x,0)
pipe2sprite.center=(p2x,600)
pipe3sprite.center=(p3x,-150)
pipe4sprite.center=(p4x,500)
by=300
birdsprite.center=(50,by)
velocity=-1
score=0
font1=py.font.SysFont("Arial", 30)
text1= font1.render("Score: " + str(score), True, "black")
gravity=0.2

while running:
    p1x=p1x+velocity
    p2x=p2x+velocity
    p3x=p3x+velocity
    p4x=p4x+velocity
    by=by+gravity 
    if p1x<0:
         score=score+1
         p1x=800
         p2x=800
    if p3x<0:
             score=score+1                                                                      
             p3x=800
             p4x=800
    if birdsprite.colliderect(pipe1sprite):
          velocity=0
          gravity=0
          bgmusic=py.mixer.music.load("ejah_music-game-over-retro-video-game-1-422479.mp3")
          font1=py.font.SysFont("Arial",20)
          py.mixer.music.play()
          
      
    if birdsprite.colliderect(pipe2sprite):
          velocity=0
          gravity=0
          bgmusic=py.mixer.music.load("ejah_music-game-over-retro-video-game-1-422479.mp3")
          font1=py.font.SysFont("Arial",20)
          py.mixer.music.play()
          
          
    if birdsprite.colliderect(pipe3sprite):
          velocity=0
          gravity=0
          bgmusic=py.mixer.music.load("ejah_music-game-over-retro-video-game-1-422479.mp3")
          font1=py.font.SysFont("Arial",20)
          py.mixer.music.play()
          
          
    if birdsprite.colliderect(pipe4sprite)  :
          velocity=0
          gravity=0
          bgmusic=py.mixer.music.load("ejah_music-game-over-retro-video-game-1-422479.mp3")
          font1=py.font.SysFont("Arial",20)       
          py.mixer.music.play()

    keys= py.key.get_pressed()
    if keys[py.K_SPACE]:
          by=by-2 
          
          
    
      
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
    text1= font1.render("Score: " + str(score), True, "black")
    screen.blit(text1,(300,100))
    pipe1sprite.center=(p1x,0)
    pipe2sprite.center=(p2x,600)
    pipe3sprite.center=(p3x,-150)
    pipe4sprite.center=(p4x,500)

    py.display.update()
    

py.quit()