import pygame as py
import time
py.init()
screen=py.display.set_mode((800,800))
py.display.set_caption("Recycling")
running=True
greenbin=py.image.load("png-green-bin-set-waste-collection_888418-95409-removebg-preview.png")
redbin=py.image.load("red-recycling-bin-photo-removebg-preview.png")
yellowbin=py.image.load("a-recycle-trash-bin-in-yellow-color-isolate-on-transparent-background-png-removebg-preview.png")
greenbin=py.transform.scale(greenbin,(100,100))
redbin=py.transform.scale(redbin,(100,100))
yellowbin=py.transform.scale(yellowbin,(100,100))
greenbinsprite= greenbin.get_rect()
redbinsprite= redbin.get_rect()
yellowbinsprite= yellowbin.get_rect()
greenbinsprite.center=(50,650)
redbinsprite.center=(400,650)
yellowbinsprite.center=(750,650)
plasticbottle=py.image.load("cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDI0LTA4L3N0YXJ0dXBpbWFnZXNfcGhvdG9ncmFwaHlfb2ZfcGxhc3RpY19ib3R0bGVfd2FzdGVfcGlsZV9pc29sYXRlZF82ZWVkZTEwNy1lMDg3LTQ1NTQtYjExNC1lNmQ3ZjEzMDdmOWMucG5n-removebg-previe.png")
plasticbottle=py.transform.scale(plasticbottle,(70,70))
plasticbottlesprite= plasticbottle.get_rect()
plasticbottlesprite.center=(100,70)
paper=py.image.load("pngtree-bunch-of-waste-of-paper-materials-isolated-png-image_15775701-removebg-preview.png")
paper=py.transform.scale(paper,(70,70))
papersprite= paper.get_rect()
papersprite.center=(250,70)
ceramic=py.image.load("pngtree-a-white-ceramic-vase-tipped-over-surrounded-by-numerous-scattered-broken-png-image_16133345-removebg-preview.png")
ceramic=py.transform.scale(ceramic,(70,70))
ceramicsprite= ceramic.get_rect()
ceramicsprite.center=(350,70)
bananapeel=py.image.load("banana-peel-png-favpng-PMLb1xH9qwiRpiHrhVFRjyC3z-removebg-preview.png")
bananapeel=py.transform.scale(bananapeel,(70,70))
bananapeelsprite= bananapeel.get_rect()
bananapeelsprite.center=(450,70)
rottenapple=py.image.load("half-rotten-apple-isolated-transparent-background-realistic-vector-illustration_220739-12566-removebg-preview.png")
rottenapple=py.transform.scale(rottenapple,(70,70))
rottenapplesprite= rottenapple.get_rect()
rottenapplesprite.center=(550,70)
glassbottle=py.image.load("1000_F_659996292_87W8vSjZZt2PHxcm5tGyyftSAMbKNqWB-removebg-preview.png")
glassbottle=py.transform.scale(glassbottle,(70,70))
glassbottlesprite= glassbottle.get_rect()
glassbottlesprite.center=(650,70)

draggingplasticbottle=False
draggingceremic=False
draggingpaper=False
draggingrottenapple=False
draggingglassbottle=False
draggingbananapeel=False
score=0

while running:
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
        if event.type==py.MOUSEBUTTONDOWN:
            if plasticbottlesprite.collidepoint(event.pos):
                draggingplasticbottle=True
            if glassbottlesprite.collidepoint(event.pos):
                draggingglassbottle=True
            if papersprite.collidepoint(event.pos):
                draggingpaper=True
            if ceramicsprite.collidepoint(event.pos):
                draggingceremic=True
            if bananapeelsprite.collidepoint(event.pos):
                draggingbananapeel=True
            if rottenapplesprite.collidepoint(event.pos):
                draggingrottenapple=True

        if event.type==py.MOUSEMOTION:
            if draggingplasticbottle==True:
                plasticbottlesprite.center= event.pos
            if draggingglassbottle==True:
                glassbottlesprite.center= event.pos
            if draggingpaper==True:
                papersprite.center= event.pos
            if draggingceremic==True:
                ceramicsprite.center= event.pos
            if draggingbananapeel==True:
                 bananapeelsprite.center= event.pos
            if draggingrottenapple==True:
                 rottenapplesprite.center= event.pos

        if event.type==py.MOUSEBUTTONUP:
            draggingbananapeel=False
            draggingglassbottle=False
            draggingrottenapple=False
            draggingceremic=False
            draggingpaper=False
            draggingplasticbottle=False

    if plasticbottlesprite.colliderect(greenbinsprite):
        time.sleep(2)
        draggingplasticbottle=False
        
        plasticbottlesprite.center=(2000,2000)
        score=score+1

    if papersprite.colliderect(greenbinsprite):
            papersprite.center=(2000,2000)
            draggingpaper=False
            time.sleep(1)
            score=score+1
    if ceramicsprite.colliderect(redbinsprite):
            ceramicsprite.center=(2000,2000)
            draggingceremic=False
            time.sleep(1)
            score=score+1
    if glassbottlesprite.colliderect(redbinsprite):
            glassbottlesprite.center=(2000,2000)
            draggingglassbottle=False
            time.sleep(1)
            score=score+1
    if bananapeelsprite.colliderect(yellowbinsprite):
            bananapeelsprite.center=(2000,2000)
            draggingbananapeel=False
            time.sleep(1)
            score=score+1
    if rottenapplesprite.colliderect(yellowbinsprite):
            rottenapplesprite.center=(2000,2000)
            draggingrottenapple=False
            time.sleep(1)
            score=score+1

    if plasticbottlesprite.colliderect(yellowbinsprite):
        plasticbottlesprite.center=(2000,2000)
        draggingplasticbottle=False
        time.sleep(1)
        score=score-1
    if plasticbottlesprite.colliderect(redbinsprite):
            plasticbottlesprite.center=(2000,2000)
            draggingplasticbottle=False
            time.sleep(1)
            score=score-1
    if papersprite.colliderect(yellowbinsprite):
            papersprite.center=(2000,2000)
            draggingpaper=False
            time.sleep(1)
            score=score-1
    if papersprite.colliderect(redbinsprite):
                papersprite.center=(2000,2000)
                draggingpaper=False
                time.sleep(1)
                score=score-1
    if ceramicsprite.colliderect(greenbinsprite):
                ceramicsprite.center=(2000,2000)
                draggingceramic=False
                time.sleep(1)
                score=score-1
    if ceramicsprite.colliderect(yellowbinsprite):
                    ceramicsprite.center=(2000,2000)
                    draggingceramic=False
                    time.sleep(1)
                    score=score-1
    if glassbottlesprite.colliderect(greenbinsprite):
                glassbottlesprite.center=(2000,2000)
                draggingglassbottle=False
                time.sleep(1)
                score=score-1
    if glassbottlesprite.colliderect(yellowbinsprite):
                    glassbottlesprite.center=(2000,2000)
                    draggingglassbottle=False
                    time.sleep(1)
                    score=score-1
    if bananapeelsprite.colliderect(greenbinsprite):
                bananapeelsprite.center=(2000,2000)
                draggingbananapeel=False
                time.sleep(1)
                score=score-1
    if bananapeelsprite.colliderect(redbinsprite):
                    bananapeelsprite.center=(2000,2000)
                    draggingbananapeel=False
                    time.sleep(1)
                    score=score-1
    if rottenapplesprite.colliderect(greenbinsprite):
                rottenapplesprite.center=(2000,2000)
                draggingrottenapple=False
                time.sleep(1)
                score=score-1

    if rottenapplesprite.colliderect(redbinsprite):
                rottenapplesprite.center=(2000,2000)
                draggingrottenapple=False
                time.sleep(1)
                score=score-1 
    print(score)
        

    
    

    
    

                                
                                
                                
                                    
                                    
                    
    screen.fill("grey")
    screen.blit(greenbin,greenbinsprite)
    screen.blit(redbin,redbinsprite)
    screen.blit(yellowbin,yellowbinsprite)
    screen.blit(plasticbottle,plasticbottlesprite)
    screen.blit(paper,papersprite)
    screen.blit(ceramic,ceramicsprite)
    screen.blit(bananapeel,bananapeelsprite)
    screen.blit(rottenapple,rottenapplesprite)
    screen.blit(glassbottle,glassbottlesprite)
    if score==6:
        font1=py.font.SysFont("Arial",20)
        text1=font1.render("Great you completed the activity", "blue", True)
        screen.blit(text1,(300,300))

    py.display.update()
    
py.quit()