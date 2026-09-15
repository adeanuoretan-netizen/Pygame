import pygame as py
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
plasticbootle=py.image.load("cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDI0LTA4L3N0YXJ0dXBpbWFnZXNfcGhvdG9ncmFwaHlfb2ZfcGxhc3RpY19ib3R0bGVfd2FzdGVfcGlsZV9pc29sYXRlZF82ZWVkZTEwNy1lMDg3LTQ1NTQtYjExNC1lNmQ3ZjEzMDdmOWMucG5n-removebg-previe.png")
glassbottle=py.image.load("1000_F_659996292_87W8vSjZZt2PHxcm5tGyyftSAMbKNqWB-removebg-preview.png")
paper=py.image.load("pngtree-bunch-of-waste-of-paper-materials-isolated-png-image_15775701-removebg-preview.png")
ceramic=py.image.load("pngtree-a-white-ceramic-vase-tipped-over-surrounded-by-numerous-scattered-broken-png-image_16133345-removebg-preview.png")
bananapeel=py.image.load("banana-peel-png-favpng-PMLb1xH9qwiRpiHrhVFRjyC3z-removebg-preview.png")
rottenapple=py.image.load("half-rotten-apple-isolated-transparent-background-realistic-vector-illustration_220739-12566-removebg-preview.png")
while running:
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
    screen.fill("grey")
    screen.blit(greenbin,greenbinsprite)
    screen.blit(redbin,redbinsprite)
    screen.blit(yellowbin,yellowbinsprite)
    py.display.update()
    
py.quit()