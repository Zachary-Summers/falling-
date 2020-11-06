#initializing and importing
import time, pygame, sys, random, pyautogui
from pygame.locals import *
pygame.init()
#variables
screen = pygame.display.set_mode((800,600))
run = True
main_radius = 20
radius = 10
COLOR = (122, 255, 242)
BLACK = (0,0,0)
PINK = (255, 0, 119)
RED = (255,0,0)
MAROON = (117, 22, 76)
BLUE = (0,0,255)
GREEN = (0,255,0)
PURPLE = (255,0,255)
x = 400
y = 500
pyautogui.alert(text="For help type \'h\'.", title='Alert')
font = pygame.font.SysFont("comicsansms", 50)
text = font.render('Falling', True, PINK, BLACK) 
textRect = text.get_rect()  
textRect.center = (700, 35) 
bx = random.randint(0,800)
pygame.display.set_caption('Falling')
by = random.randint(0,600)
gx = random.randint(0,800)
gy = random.randint(0,600)
gy_change = 1
bx2 = random.randint(0,800)
by2 = random.randint(0,600)
by2_change = 1
bx3 = random.randint(0,800)
by3 = random.randint(0,600)
by3_change = 1
bx4 = random.randint(0,800)
by4 = random.randint(0,600)
by4_change = 1
bx5 = random.randint(0,800)
by5 = random.randint(0,600)
by5_change = 1
px = random.randint(0,800)
py = random.randint(0,600)
by_change = 1
py_change = 1
py2 = random.randint(0,600)
px2 = random.randint(0,800)
py2_change = 1
py5 = random.randint(0,600)
px5 = random.randint(0,800)
py5_change = 1
py6 = random.randint(0,600)
px6 = random.randint(0,800)
py6_change = 1
py7 = random.randint(0,600)
px7 = random.randint(0,800)
py7_change = 1
py8 = random.randint(0,600)
px8 = random.randint(0,800)
py8_change = 1
bby = random.randint(0,600)
bbx = random.randint(0,800)
bby_change = 1
py9 = random.randint(0,600)
px9 = random.randint(0,800)
py9_change = 1
py10 = random.randint(0,600)
px10 = random.randint(0,800)
py10_change = 1
py3 = random.randint(0,600)
px3 = random.randint(0,800)
py3_change = 1
py4 = random.randint(0,600)
px4 = random.randint(0,800)
py4_change = 1
x_change = 0
mx = random.randint(0,800)
my = random.randint(0,600)
my_change = 1
mx2 = random.randint(0,800)
my2 = random.randint(0,600)
my2_change = 1
lx =  random.randint(0,800)
ly = random.randint(0,600)
ly_change = 1
lx2 =  random.randint(0,800)
ly2 = random.randint(0,600)
ly2_change = 1
clock = 0.001
score = 0
health = 5
level = 0
high = 0
#main loop
while run:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2
            elif event.key == pygame.K_RIGHT:
                x_change = 2
            elif event.key == pygame.K_h:
                help = pyautogui.prompt(text='What would you like help with?(Help commands are \'colors\', \'level\', \'controls\', and \'game\'.', title='help')
                if help == 'colors':
                    pyautogui.alert(text='You are the big blue ball, the pink balls will give you one point, the red balls will take away a point, the purple balls will take away five points, the green balls will give you 5 points, the blue balls will give you one more life, the maroon balls will take away a life, the white balls are your score, the light pink balls are your health, and the small blue balls are your level.', title='Colors')
                elif help == 'level':
                    pyautogui.alert(text='To go up a level get a score of 30 or 30 lives, to go to level 0 you get -1 score or 0 health.', title='Level')
                elif help == 'controls':
                    pyautogui.alert(text='Left arrow key moves you left, right arrow key moves you right, the h key goes to help, the l key lets you switch modes, the f key will turn of the taskbar, the d key will turn on the taskbar, and the m key lets you play music.', title='Controls')
                elif help == 'game':
                    pyautogui.alert(text='The game Falling is by Zachary Summers and is a game where balls are falling at you and you have to hit specific ones to go up a level.', title='Game')
            elif event.key == pygame.K_m:
                music = pyautogui.prompt(text='What music?', title='Music')
                if music != 'stop':
                    pygame.mixer.music.load(music)
                    pygame.mixer.music.play(-1)
                elif music == 'stop':
                    pygame.mixer.music.stop()
            elif event.key == pygame.K_l:
                mode = pyautogui.confirm(text='What mode?', title='Mode', buttons=('Easy','Medium','Hard'))
                if mode == 'Easy':
                    clock = 0.005
                elif mode == 'Hard':
                    clock = 0
                else:
                    clock = 0.001
            elif event.key == pygame.K_f:
                pygame.display.set_mode((800,600),pygame.NOFRAME)
            elif event.key == pygame.K_d:
                pygame.display.set_mode((800,600))
            elif event.key == pygame.K_a:
                speed = float(pyautogui.prompt(text='What speed?',title='Speed'))
                clock = speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    #colision detection and wall detection
    if x >= 800:
        x_change = -2
    elif x <= 0:
        x_change = 2
    if x + main_radius >= px - radius and y + main_radius >= py - radius and x - main_radius <= px + radius and y - main_radius <= py + radius:
        score += 1
        py = 0
        px = random.randint(0,800)
    if x + main_radius >= gx - radius and y + main_radius >= gy - radius and x - main_radius <= gx + radius and y - main_radius <= gy + radius:
        score += 5
        gy = 0
        gx = random.randint(0,800)
    if x + main_radius >= px5 - radius and y + main_radius >= py5 - radius and x - main_radius <= px5 + radius and y - main_radius <= py5 + radius:
        score += 1
        py5 = 0
        px5 = random.randint(0,800)
    if x + main_radius >= px6 - radius and y + main_radius >= py6 - radius and x - main_radius <= px6 + radius and y - main_radius <= py6 + radius:
        score += 1
        py6 = 0
        px6 = random.randint(0,800)
    if x + main_radius >= px7 - radius and y + main_radius >= py7 - radius and x - main_radius <= px7 + radius and y - main_radius <= py7 + radius:
        score += 1
        py7 = 0
        px7 = random.randint(0,800)
    if x + main_radius >= px8 - radius and y + main_radius >= py8 - radius and x - main_radius <= px8 + radius and y - main_radius <= py8 + radius:
        score += 1
        py8 = 0
        px8 = random.randint(0,800)
    if x + main_radius >= px9 - radius and y + main_radius >= py9 - radius and x - main_radius <= px9 + radius and y - main_radius <= py9 + radius:
        score += 1
        py9 = 0
        px9 = random.randint(0,800)
    if x + main_radius >= px10 - radius and y + main_radius >= py10 - radius and x - main_radius <= px10 + radius and y - main_radius <= py10 + radius:
        score += 1
        py10 = 0
        px10 = random.randint(0,800)
    if x + main_radius >= px4 - radius and y + main_radius >= py4 - radius and x - main_radius <= px4 + radius and y - main_radius <= py4 + radius:
        score += 1
        py4 = 0
        px4 = random.randint(0,800)
    if x + main_radius >= px3 - radius and y + main_radius >= py3- radius and x - main_radius <= px3 + radius and y - main_radius <= py3 + radius:
        score += 1
        py3 = 0
        px3 = random.randint(0,800)
    if x + main_radius >= px2 - radius and y + main_radius >= py2 - radius and x - main_radius <= px2 + radius and y - main_radius <= py2 + radius:
        score += 1
        py2 = 0
        px2 = random.randint(0,800)
    if x + main_radius >= bx - radius and y + main_radius >= by - radius and x - main_radius <= bx + radius and y - main_radius <= by + radius:
        score += -1
        by = 0
        bx = random.randint(0,800)
    if x + main_radius >= bx4 - radius and y + main_radius >= by4 - radius and x - main_radius <= bx4 + radius and y - main_radius <= by4 + radius:
        score += -1
        by4 = 0
        bx4 = random.randint(0,800)
    if x + main_radius >= bx5 - radius and y + main_radius >= by5 - radius and x - main_radius <= bx5 + radius and y - main_radius <= by5 + radius:
        score += -1
        by5 = 0
        bx5 = random.randint(0,800)
    if x + main_radius >= bx3 - radius and y + main_radius >= by3 - radius and x - main_radius <= bx3 + radius and y - main_radius <= by3 + radius:
        score += -1
        by3 = 0
        bx3 = random.randint(0,800)
    if x + main_radius >= bx2 - radius and y + main_radius >= by2 - radius and x - main_radius <= bx2 + radius and y - main_radius <= by2 + radius:
        score += -1
        by2 = 0
        bx2 = random.randint(0,800)
    if x + main_radius >= mx - radius and y + main_radius >= my - radius and x - main_radius <= mx + radius and y - main_radius <= my + radius:
        health += -1
        my = 0
        mx = random.randint(0,800)
    if x + main_radius >= mx2 - radius and y + main_radius >= my2 - radius and x - main_radius <= mx2 + radius and y - main_radius <= my2 + radius:
        health += -1
        my2 = 0
        mx2 = random.randint(0,800)
    if x + main_radius >= lx - radius and y + main_radius >= ly - radius and x - main_radius <= lx + radius and y - main_radius <= ly + radius:
        health += 1
        ly = 0
        lx = random.randint(0,800)
    if x + main_radius >= lx2 - radius and y + main_radius >= ly2 - radius and x - main_radius <= lx2 + radius and y - main_radius <= ly2 + radius:
        health += 1
        ly2 = 0
        lx2 = random.randint(0,800)
    if x + main_radius >= bbx - radius and y + main_radius >= bby - radius and x - main_radius <= bbx + radius and y - main_radius <= bby + radius:
        score += -5
        bby = 0
        bbx = random.randint(0,800)
    if bby >= 600:
        bby = 0
        bbx = random.randint(0,800)
    if ly >= 600:
        ly = 0
        lx = random.randint(0,800)
    if ly2 >= 600:
        ly2 = 0
        lx2 = random.randint(0,800)
    if gy >= 600:
        gy = 0
        gx = random.randint(0,800)
    if py >= 600:
        py = 0
        px = random.randint(0,800)
    if py5 >= 600:
        py5 = 0
        px5 = random.randint(0,800)
    if py6 >= 600:
        py6 = 0
        px6 = random.randint(0,800)
    if py7 >= 600:
        py7 = 0
        px7 = random.randint(0,800)
    if py8 >= 600:
        py8 = 0
        px8 = random.randint(0,800)
    if py9 >= 600:
        py9 = 0
        px9 = random.randint(0,800)
    if py10 >= 600:
        py10 = 0
        px10 = random.randint(0,800)
    if py4 >= 600:
        py4 = 0
        px4 = random.randint(0,800)
    if bby >= 600:
        bby = 0
        bby = random.randint(0,800)
    if py3 >= 600:
        py3 = 0
        px3 = random.randint(0,800)
    if py2 >= 600:
        py2 = 0
        px2 = random.randint(0,800)
    if my >= 600:
        my = 0
        mx = random.randint(0,800)
    if my2 >= 600:
        my2 = 0
        mx2 = random.randint(0,800)
    if by >= 600:
        by = 0
        bx = random.randint(0,800)
    if by4 >= 600:
        by4 = 0
        bx4 = random.randint(0,800)
    if by5 >= 600:
        by5 = 0
        bx5 = random.randint(0,800)
    if by2 >= 600:
        by2 = 0
        bx2 = random.randint(0,800)
    if by3 >= 600:
        by3 = 0
        bx3 = random.randint(0,800)
    #score, health, and level circles
    def scoreCircles(repCircles):
      for i in range (repCircles):
        pygame.draw.circle(screen, (255,255,255),((i*20+10), 50), radius)
    def healthCircles(repCircles):
      for i in range (repCircles):
        pygame.draw.circle(screen, (255, 166, 237),((i*20+10), 100), radius)
    def levelCircles(repCircles):
      for i in range (repCircles):
        pygame.draw.circle(screen, (0, 255, 255),((i*20+10), 150), radius)
    def highCircles(repCircles):
      for i in range (repCircles):
        pygame.draw.circle(screen, (255,255,0),((i*20+10), 200), radius)
    #winning and losing
    if health <= 0:
        health = 5
        score = 0
        level = 0
    if score >= 30:
        health = 5
        score = 0
        level += 1
    if score <= -1:
        health = 5
        score = 0
        level = 0
    if health >= 30:
        health = 5
        score = 0
        level += 1
    if level > high:
        high = level
    #ticking clock and adding to y/x value the y/x_change
    time.sleep(clock)
    ly += ly_change
    py += py_change
    py5 += py5_change
    py6 += py6_change
    py7 += py7_change
    py8 += py8_change
    py9 += py9_change
    py10 += py10_change
    py2 += py2_change
    py3 += py3_change
    py4 += py4_change
    by += by_change
    bby += bby_change
    by4 += by4_change
    by5 += by5_change
    my += my_change
    by3 += by3_change
    gy += gy_change
    x += x_change
    by2 += by2_change
    my2 += my2_change
    ly2 += ly2_change
    #drawing to screen and updating the screen
    screen.fill(BLACK)
    pygame.draw.circle(screen, BLUE, (lx,ly), radius)
    pygame.draw.circle(screen, BLUE, (lx2,ly2), radius)
    pygame.draw.circle(screen, MAROON, (mx,my), radius)
    pygame.draw.circle(screen, MAROON, (mx2,my2), radius)
    pygame.draw.circle(screen, RED, (bx,by), radius)
    pygame.draw.circle(screen, GREEN, (gx,gy), radius)
    pygame.draw.circle(screen, RED, (bx4,by4), radius)
    pygame.draw.circle(screen, RED, (bx5,by5), radius)
    pygame.draw.circle(screen, RED, (bx3,by3), radius)
    pygame.draw.circle(screen, RED, (bx2,by2), radius)
    pygame.draw.circle(screen, PINK, (px,py), radius)
    pygame.draw.circle(screen, PINK, (px5,py5), radius)
    pygame.draw.circle(screen, PINK, (px6,py6), radius)
    pygame.draw.circle(screen, PINK, (px7,py7), radius)
    pygame.draw.circle(screen, PINK, (px8,py8), radius)
    pygame.draw.circle(screen, PINK, (px9,py9), radius)
    pygame.draw.circle(screen, PINK, (px10,py10), radius)
    pygame.draw.circle(screen, PINK, (px4,py4), radius)
    pygame.draw.circle(screen, PINK, (px3,py3), radius)
    pygame.draw.circle(screen, PINK, (px2,py2), radius)
    pygame.draw.circle(screen, PURPLE, (bbx,bby), radius)
    pygame.draw.circle(screen, COLOR, (x,y), main_radius)
    screen.blit(text, textRect)
    scoreCircles(score)
    healthCircles(health)
    levelCircles(level)
    highCircles(high)
    pygame.display.update()

