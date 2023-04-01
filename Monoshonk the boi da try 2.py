from pygame import*
window = display.set_mode((700, 500))
display.set_caption("MY MOM!")

height = 60
width = 40
x = 5
y = 500 - height - 5
draw.rect(window, (0,0,255), (x, y, width, height))
display.update()



run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                print("left")
            elif e.key == K_RIGHT:
                print("right")
            elif e.key == K_UP:
                print("up")
            elif e.key == K_DOWN:
                print("down")
        elif e.type == QUIT:
            quit()



time.delay(5000)