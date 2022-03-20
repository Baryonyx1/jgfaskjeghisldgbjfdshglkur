#Создай собственный Шутер!

from pygame import *
from pygame import *
from random import randint
font.init()
zad_bullet = 0
zad_max_bullet = 15
killingenemy = 0
class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,scale_x,scale_y):
        super().__init__()
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = transform.scale(image.load(player_image), (self.scale_x, self.scale_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(Gamesprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s]and self.rect.y < win_width - 80:
            self.rect.y += self.speed
        if keys_pressed[K_a]and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d]and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys_pressed[K_UP]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]and self.rect.y < win_width - 80:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT]and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT]and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def shot(self):
        keys_pressed = key.get_pressed()
        global zad_bullet
        if zad_bullet == zad_max_bullet :
            if keys_pressed[K_SPACE]:
                bullet =  Bullet('bullet.png',player.rect.x + 18,player.rect.y -10,6,20,40)
                bullets.add(bullet)
                
                zad_bullet = 0
        else:
            zad_bullet +=1
       
lost =1
class Enemy(Gamesprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(100,win_width-100)
            self.rect.y = 0
            lost = lost + 1
       
score = 0
class Bullet(Gamesprite):
    def update(self):
        if self.rect.y != -150:
            self.rect.y -= self.speed
        if self.rect.y <0:
            self.kill()


win_width = 1000
win_height = 750
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))
player = Player('rocket.png',5, win_height - 80, 4,100,100)
bullets = sprite.Group()

monsters = sprite.Group()
for i in range(1,6):
    enemy = Enemy('ufo.png',randint(80,win_width-80),-40,randint(1,3),70,40)
    monsters.add(enemy)
game = True
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('f.mp3')
mixer.music.play()

h = False
l = 0
font1 = font.Font(None,100)
font2 = font.Font(None,35)
text1 = font1.render('GAme Over',True ,(255,255,255))
text1_2 = font1.render('НИГЕРС',True ,(255,255,255))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if h != True:
        window.blit(background,(0,0))
        text = font2.render('счет:' + str(score),1,(255,255,255))
        window.blit(text,(10,20))
        text_lose = font2.render('Пропущено:' + str(lost),1,(233,255,255))
        if lost >= 10:
            window.blit(text1,(100,200))
            h = True
        elif score == 15:
            window.blit(text1_2,(100,200))
            h = True
        if sprite.groupcollide(monsters,bullets,True,True):
            score += 1
            enemy = Enemy('ufo.png',randint(100,win_width-100),-20,randint(2,6),65,65)
            monsters.add(enemy)
        if sprite.spritecollide(player,monsters,False):
            h = True
            window.blit(text1,(10,20))
            mixer.music.stop()
        


        window.blit(text_lose,(10,50))

        player.update()
        player.shot() 
        player.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        display.update()
        clock.tick(FPS)                                                                                                                                                                                                                                                                                                                                                                                                                                             