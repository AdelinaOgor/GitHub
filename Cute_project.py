from pygame import *
from Character import GameSprite

#marimea ecranului
window = display.set_mode((600, 600))

#denuimirea jocului
display.set_caption("Cute World")

#fundalul jocului
backround = transform.scale(image.load("c:\\Users\\cheptine\\Desktop\\my game\\fundal_iepuras.PNG"), (800, 800))

#"lipim" fundalul de ecran
window.blit(backround,(10,10))

#sprite-ul meu principal
bob = GameSprite("c:\\Users\\cheptine\\Desktop\\Pygame\\cute_caracter2.png", 100, 100, 2)
block1 = GameSprite("c:\\Users\\cheptine\\Desktop\\Pygame\\block.PNG", 400, 80, 10)
block2 = GameSprite("c:\\Users\\cheptine\\Desktop\\Pygame\\block.PNG", 200, 80, 10)
block3 = GameSprite("c:\\Users\\cheptine\\Desktop\\Pygame\\block.PNG", 200, 90, 10)
block4 = GameSprite("c:\\Users\\cheptine\\Desktop\\Pygame\\block.PNG", 300, 80, 10)

game = True
while game:
    window.blit(backround,(600, 600))
    display.update()
    bob.reset(window)
    bob.handle_events()
    bob.update(window)
    window.blit(backround,(600, 600))
    block1.reset(window)
    block1.handle_events()
    block2.reset(window)
    block2.handle_events()
    block3.reset(window)
    block3.handle_events()
    block4.reset(window)
    block4.handle_events()
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False
