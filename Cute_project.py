from pygame import *
from Character import GameSprite

window = display.set_mode((600, 600))
display.set_caption("Catch")
backround = transform.scale(image.load("backround.png"), (800, 800))

window.blit(backround,(10,10))

pig = GameSprite("cute_pig_caracter.png", 100, 100, 2)
