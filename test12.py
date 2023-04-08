from pygame import *
from sys import *


window = display.set_mode((700, 500))
display.set_caption("First application")
window.fill((255, 100, 50))
background = transform.scale(image.load("fail_1.jpg"), (700,500))
window.blit(background,(0,0))


draw.rect(window, (0,0,0), (100,  40,  40, 60))

merlin = transform.scale(image.load('shutterstock_783589810_frame-32.png'), (100, 100))
window.blit(merlin, (100, 100))

display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

