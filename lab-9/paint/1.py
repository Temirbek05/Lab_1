import pygame, math

#Draws rectangle
def rectangle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    a = abs(x1-x2)
    b = abs(y1-y2)
    pygame.draw.rect(surf, color, (min(x1, x2), min(y1, y2), a, b), d)
    
def square(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    c = min(abs(x2-x1), abs(y2-y1))
    if x2 != x1:
        a1 = int((x2-x1)/abs(x2 - x1))
    else:
        a1 = 0
    if y2 != y1:
        b1 = int((y2-y1)/abs(y2-y1))
    else:
        b1 = 0
    pygame.draw.polygon(surf, color, [(x1, y1), ((x1 + a1 * c), y1), ((x1 + a1 * c), (y1 + b1 * c)), (x1, y1 + b1 * c)], d)


def isosceles_triangle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    a = x1-x2
    pygame.draw.polygon(surf, color, [(x1, y1), (x1 + a, y2), (x2, y2)], d)

def right_triangle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    a = abs(x1-x2)
    b = abs(y1-y2)
    pygame.draw.polygon(surf, color, [(x1, y1), (x1, y2), (x2, y2)], d)

def triangle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    height = y2 - y1
    c = 2 * height / math.tan(math.radians(60))
    point1 = (x1, y1)
    point2 = (x1 + c/2, y1 + height)
    point3 = (x1 - c/2, y1 + height) 
    pygame.draw.polygon(surf, color, [point1, point2, point3], d)


def rhombus(surf, cur, end, d, color): 
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    a = x1-x2
    pygame.draw.polygon(surf, color, [((x1 + x2)/2, y1), (x2, (y1 + y2)/2), ((x1 + x2)/2, y2), (x1, (y1 + y2)/2)], d)

#Pen tool
def pen(surf, cur, end, d, color):
    pygame.draw.line(surf, color, cur, end, d)

#Draws circle     
def circle(surf, cur, end, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1]
    a = abs(x1-x2)
    b = abs(y1-y2)
    pygame.draw.ellipse(surf, color, (min(x1, x2), min(y1, y2), a, b), d)

#Eraser tool
def eraser(surf, cur):
    x1, y1 = cur[0], cur[1]
    pygame.draw.circle(surf, "Black", (x1, y1), 20)

FPS = 60
WIDTH = 640
HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')
baseLayer = pygame.Surface((640, 480))
clock = pygame.time.Clock()

mode = "Rectangle"
color = "Red"
isMouseDown = False
currentX = -1
currentY = -1
prevX = -1
prevY = -1


running = True

while running:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            #Color switches
            if event.key == pygame.K_r:
                color = "Red"
            if event.key == pygame.K_b:
                color = "Blue"
            if event.key == pygame.K_g:
                color = "Green"
            if event.key == pygame.K_w:
                color = "White"
            
            #Tool switches
            if event.key == pygame.K_1:
                mode = "Rectangle"
            if event.key == pygame.K_2:
                mode = "Square"
            if event.key == pygame.K_3:
                mode = "Circle"
            if event.key == pygame.K_4:
                mode = "Equil"
            if event.key == pygame.K_5:
                mode = "Isos"
            if event.key == pygame.K_6:
                mode = "Right"
            if event.key == pygame.K_7:
                mode = "Rhombus"
            if event.key == pygame.K_8:
                mode = "Pen"
            if event.key == pygame.K_9:
                mode = "Eraser"

        #Saves coordinates when we hold LMB
        if event.type == pygame.MOUSEBUTTONDOWN:
            xnow = event.pos[0]
            ynow = event.pos[1]
            last_pos = (xnow, ynow)
            isMouseDown = True
        #Copies screen on canvas when release LMB
        if event.type == pygame.MOUSEBUTTONUP:
            isMouseDown = False
            baseLayer.blit(screen, (0,0))
        #Saves moving position and draws pen when mouse is moved while LMB is pressed 
        if event.type == pygame.MOUSEMOTION:
            if isMouseDown == True:
                if mode == 'Pen':
                    pen(baseLayer, last_pos, (xnow, ynow), 1, color)
                    last_pos = (xnow, ynow)
                xnow = event.pos[0]
                ynow = event.pos[1]

    #Copy canvas on screen and use tools
    if isMouseDown == True and last_pos[0] != -1 and last_pos[1] != -1 and xnow != -1 and ynow != -1:
        screen.blit(baseLayer, (0, 0))
        if mode == 'Rectangle':
            rectangle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == 'Circle':
            circle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == "Eraser":
            eraser(baseLayer, (xnow, ynow))
        elif mode == 'Square':
            square(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == 'Isos':
            isosceles_triangle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == 'Rhombus':
            rhombus(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == 'Right':
            right_triangle(screen, last_pos, (xnow, ynow), 1, color)
        elif mode == 'Equil':
            triangle(screen, last_pos, (xnow, ynow), 1, color)
    pygame.display.update()
    clock.tick(144)