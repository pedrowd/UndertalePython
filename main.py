import pygame
import os
pygame.init()


win = pygame.display.set_mode((800,800))
bulletSound = pygame.mixer.Sound(os.path.join('music','Yellow SOUL shoot.wav'))

pygame.display.set_caption("Undertale Python")

clock = pygame.time.Clock()
font1 = pygame.font.Font('MonsterFriendFore.otf',42)
font2 = pygame.font.Font('MonsterFriendBack.otf',42)
font3 = pygame.font.Font('DTM-Sans.otf',36)
font4 = pygame.font.Font('MonsterFriendFore.otf',25)
title = font1.render('undertAle python',1,(255,255,255))
title2 = font2.render('undertAle python',1,(128,128,128))
subtitle = font4.render('by pAtrick',1,(255,255,255))
options = font3.render('[1]-Normal        [2]-Papyrus       [3]-Mettaton',1,(255,255,255))
options2 =font3.render('[4]-Muffet      [5]-Undyne',1,(255,255,255))
class red:
    def __init__(self,width,height):
        self.x = 375
        self.y = 375
        self.width = width
        self.height = height
        self.vel = 6
        self.heart = pygame.image.load(os.path.join('images','heart.png'))
        self.music = pygame.mixer.music.load(os.path.join('music','enemy-approaching.mp3'))
    def draw(self,win):
        win.blit(self.heart,(self.x,self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 200 + self.vel:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < 600 - self.width - self.vel:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y > 200 + self.vel:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < 600 - self.height - self.vel:
            self.y += self.vel

class blue:
    def __init__(self,width,height):
        self.x = 375
        self.y = 550
        self.width = width
        self.height = height
        self.isJump = False
        self.jumpCount = 10
        self.vel = 6
        self.heart = pygame.image.load(os.path.join('images','blue.png'))
        self.music = pygame.mixer.music.load(os.path.join('music','bonetrousle.mp3'))
    def draw(self,win):
        win.blit(self.heart,(self.x,self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 200 + self.vel:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < 600 - self.width - self.vel:
            self.x += self.vel
        if not (self.isJump):

            if keys[pygame.K_UP]:
                self.isJump = True

        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

class projectile(object):
    def __init__(self,x,y,color,vel):
        self.x = x
        self.y = y
        self.color = color
        self.vel = vel

    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x - 3,self.y,5,10),0)

class yellow:
    def __init__(self,width,height):
        self.x = 375
        self.y = 375
        self.width = width
        self.height = height
        self.vel = 6
        self.heart = pygame.image.load(os.path.join('images','yellow.png'))
        self.music = pygame.mixer.music.load(os.path.join('music','DeathByGlamour.mp3'))
    def draw(self,win):
        win.blit(self.heart,(self.x,self.y))

    def move(self):
        global shootloop,bullets
        for bullet in bullets:
            if bullet.y > 0 and bullet.y < 800:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 200 + self.vel:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < 600 - self.width - self.vel:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y > 200 + self.vel:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < 600 - self.height - self.vel:
            self.y += self.vel
        if shootloop > 0:
            shootloop += 1
        if shootloop > 5:
            shootloop = 0
        if keys[pygame.K_z] and shootloop == 0:
            if len(bullets) < 5:
                bulletSound.play()
                bullets.append(
                    projectile(round(self.x + self.width // 2), round(self.y + self.height // 2),(255, 255, 0),10))
            shootloop = 1

class purple:
    def __init__(self,width,height):
        self.x = 375
        self.y = 375
        self.width = width
        self.height = height
        self.vel = 6
        self.heart = pygame.image.load(os.path.join('images','purple.png'))
        self.music = pygame.mixer.music.load(os.path.join('music','SpiderDance.mp3'))
    def draw(self,win):
        win.blit(self.heart,(self.x,self.y))

    def move(self):
        global flag,shootloop
        for bullet in bullets:
            if bullet.y > 0 and bullet.y < 800:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
                flag = 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 200 + self.vel:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < 600 - self.width - self.vel:
            self.x += self.vel
        if shootloop > 0:
            shootloop += 1
        if shootloop > 5:
            shootloop = 0
        if keys[pygame.K_UP] and self.y > 300 + self.vel and flag == 1 and shootloop == 0:
            if len(bullets) < 1:
                bullets.append(
                    projectile(round(self.x + self.width // 2), round(self.y + self.height // 2), (255, 255, 0), 75))
            shootloop = 1
            self.y -= 100
            flag = -1
        if keys[pygame.K_DOWN] and self.y < 450 - self.height - self.vel and flag == 1 and shootloop == 0:
            self.y += 100
            if len(bullets) < 1:
                bullets.append(
                    projectile(round(self.x + self.width // 2), round(self.y + self.height // 2), (255, 255, 0), 75))
            shootloop = 1


class green:
    def __init__(self,width,height):
        self.x = 375
        self.y = 375
        self.width = width
        self.height = height
        self.vel = 6
        self.protection = pygame.image.load(os.path.join('images','tree.png'))
        self.heart = pygame.image.load(os.path.join('images','green.png'))
        self.music = pygame.mixer.music.load(os.path.join('music','spear_of_justice.mp3'))
    def draw(self,win):
        win.blit(self.heart,(375,375))
        win.blit(self.protection,(self.x,self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x = 300
            self.y = 375
        if keys[pygame.K_RIGHT] and self.x < 600 - self.width - self.vel:
            self.x = 450
            self.y = 375
        if keys[pygame.K_UP] and self.y > 200 + self.vel:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < 600 - self.height - self.vel:
            self.y += self.vel


class tree:
    def __init__(self,width,height):
        self.x = 375
        self.y = 375
        self.width = width
        self.height = height
        self.vel = 6
        self.heart = pygame.image.load(os.path.join('images','tree.png'))
        self.music = pygame.mixer.music.load(os.path.join('music','bone-trouble.mp3'))
    def draw(self,win):
        win.blit(self.heart,(self.x,self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 200 + self.vel:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < 600 - self.width - self.vel:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y > 200 + self.vel:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < 600 - self.height - self.vel:
            self.y += self.vel

def redrawGameWindow():
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (343, 108, 15, 15), 0)
    if muffet:
        pygame.draw.rect(win,(128,0,128),(200,400,400,5))
        pygame.draw.rect(win, (128, 0, 128), (200, 300, 400, 5))
        pygame.draw.rect(win, (128, 0, 128), (200, 500, 400, 5))
    win.blit(title2, (400 - (title.get_width() / 2), 100))
    win.blit(title,(400 - (title.get_width() / 2),100))
    win.blit(subtitle,(400 -(subtitle.get_width() / 2),75 + title.get_height() + subtitle.get_height()))
    win.blit(options,(400 - (options.get_width() / 2),650))
    win.blit(options2, (400 - (options2.get_width() / 2), 700))
    pygame.draw.rect(win,(255,255,255),(200,600,400,-400),1)
    frisk.draw(win)
    if mettaton:
        for bullet in bullets:
            bullet.draw(win)
    pygame.display.update()

frisk = red(50,50)
bullets = []
shootloop = 0
updownloop = 0
run = True
flagM = 1
flag = 1
muffet = False
mettaton = False
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        pygame.mixer.stop()
        bullets = []
        flagM = 1
        muffet= False
        mettaton = False
        frisk = red(50,50)
    if keys[pygame.K_2]:
        pygame.mixer.stop()
        bullets = []
        flagM = 1
        muffet = False
        mettaton = False
        frisk = blue(50,50)
    if keys[pygame.K_3]:
        pygame.mixer.stop()
        flagM = 1
        muffet = False
        mettaton = True
        frisk = yellow(50, 50)
    if keys[pygame.K_4]:
        pygame.mixer.stop()
        flagM = 1
        bullets = []
        muffet = True
        mettaton = False
        frisk = purple(50, 50)
    if keys[pygame.K_5]:
        pygame.mixer.stop()
        flagM = 1
        bullets = []
        muffet = False
        mettaton = True
        frisk = green(50, 50)
    if flagM == 1:
        music = frisk.music
        pygame.mixer.music.play(-1)
        flagM = -1
    frisk.move()
    redrawGameWindow()
pygame.quit()
