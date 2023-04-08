from pygame import*
window = display.set_mode((700, 500))
display.set_caption("You know who else...")

height = 60
width = 40
x = 5
y = 500 - heigh - 5
draw.rect(window, (0,0,255), (x, y, width, height))
display.update()

time.delay(5000)
