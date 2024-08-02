import pygame as pg
from random import randint
from sys import exit

pg.init()

"""
the coordinate are store in the top left 
"""

# insertin the images of character and backgroung 

walkRight = [pg.image.load( 'R1.png' ) ,pg. image . load ( 'R2.png' ) ,pg.image.load( 'R3.png' ) ,pg.image.load( 'R4.png' ),pg.image.load( 'R5.png' ),pg.image.load( 'R6.png' ),pg.image.load( 'R7.png' ),pg.image.load( 'R8.png' ),pg.image.load( 'R9.png' ) ]
walkLeft =  [pg.image.load('L1.png') ,pg. image . load ( 'L2.png' ) ,pg.image.load( 'L3.png' ) ,pg.image.load( 'L4.png' ),pg.image.load( 'L5.png' ),pg.image.load( 'L6.png' ),pg.image.load( 'L7.png' ),pg.image.load( 'L8.png' ),pg.image.load( 'L9.png' ) ]
bg = pg.image.load('BG.jpg') # background image 
flame = [ pg.image.load("R_blast.png") ,pg.image.load('L_blast.png') ,pg.image.load("R_cosmicblast.png") ,pg.image.load("L_cosmicblast.png") ] # images of fire blast 
flame_sound = [pg.mixer.Sound('flame.mp3') ,pg.mixer.Sound('cosmic_flame.mp3')]
hitsound = [pg.mixer.Sound('pain.mp3'), pg.mixer.Sound('moye.mp3')]
bg_music = pg.mixer.Sound('music.mp3')
bg_music.play(-1)
life = [pg.image.load('life.png'), pg.image.load('life_x.png')]

WINDO_HEIGHT : int = 500 # height of window
WINDO_WIDTH : int = 800 # height of window

Score : int = 0

# begin 

class player(object):
    def __init__(self ,x ,y ,wid ,hei): 
        self.x : int = x # position in x = 50
        self.y : int = y # position in y =358
        self.wid : int = wid # width of character 110
        self.hei : int = hei # height if character 120
        self.vel : int = 7 # velocity of character 
        self.delay : int = 50 # refresh rate of window screen 
        self.jumpCount : int = 10 # hight parameter of jump 
        self.neg : int = 1 # use to control up and down in jump
        self.frame : int = 27 # frame per second deliver
        self.walkCount : int = 0 # count for the frame for animation
        self.blastCount : int = 10 # no. of blast launch
        self.cosmic_blastcount : int = 1 # no. of super blast
        self.lifeCount : int = 3
        self.hitbox = (self.x + 20 ,self.y , 28 ,60 )
        self.isJump : bool = False
        self.left : bool = False 
        self.right : bool = False 
        self.standing : bool = True
        
    # defining a function to draw 
    def draw(self ,win ):
        if self.walkCount + 1 >= self.frame:
            self.walkCount = 0

        if not(self.standing):
            if self.left :
                win.blit(walkLeft[self.walkCount//3] , ( self.x , self.y))
                self.walkCount += 1
            elif self.right :
                win.blit(walkRight[self.walkCount//3] , ( self.x, self.y ))
                self.walkCount += 1
        else :
            if self.left:
                win.blit(walkLeft[0] ,(self.x ,self.y))
            else :
                win.blit(walkRight[0],(self.x ,self.y ))

        self.hitbox = (self.x + 18 ,self.y + 12 , 26 ,50 )
        #pg.draw.rect(win ,(255 ,0, 0 ), self.hitbox ,2)

    def hit(self):
        if self.lifeCount > 1 :
            self.lifeCount -= 1
            #self.y = 358
            self.x = 60 if gob.x > WINDO_WIDTH//2 else (WINDO_WIDTH -60)  
            self.walkCount = 0        
            win.blit(life[1],( 150,0))
            pg.display.update()
            i = 0
            while i < 50 :
                pg.time.delay(self.delay)
                i += 1
                for event in pg.event.get() :
                    if event.type == pg.QUIT :
                        i = 301
        else :
            font1 = pg.font.SysFont('comicscans' ,120 ,True ,False )
            text = font1.render("GAME OVER",1 ,(235,51,36))
            win.blit(text,(WINDO_WIDTH//2 -240 ,WINDO_HEIGHT//2 - 100))
            pg.display.update()
            pg.time.delay(5000)
            pg.quit()
            exit(0)
            

class projectile(object):
    def __init__(self ,x ,y,facing ):
        self.x : int  = x
        self.y : int = y 
        self.radius : int = 8
        self.iscosmic : bool
        if facing in [-1,1]:
            self.facing : int = facing 
            self.vel = 8 * self.facing 
            self.iscosmic = False
        else :
            self.facing : int = -facing
            self.vel = 8 * self.facing//2
            self.iscosmic = True
        self.hitbox = (self.x ,self.y )


    def draw(self ,win):
        if self.facing == -1:
            win.blit(flame[1] ,(self.x - 55 ,self.y - 15 ))
            self.hitbox = (self.x -35 ,self.y )
            self.radius : int = 8
        elif self.facing == +1 :
            win.blit(flame[0] ,(self.x +5 ,self.y - 15 ))
            self.hitbox = (self.x + 35 ,self.y )
            self.radius : int = 8
        elif self.facing == 2 :
            win.blit(flame[2] , (self.x + 5  ,self.y -48))
            self.hitbox = (self.x + 85 ,self.y )
            self.radius : int = 35
        else :
            win.blit(flame[3] , (self.x - 128 ,self.y - 48 ))
            self.hitbox = (self.x -90 ,self.y )
            self.radius : int = 35
        #pg.draw.circle(win ,(255,0,0) ,self.hitbox, self.radius ,2 )


class enemy(object):
    walkRight =  [pg.image.load( 'R1E.png' ) ,pg. image . load ( 'R2E.png' ) ,pg.image.load( 'R3E.png' ) ,pg.image.load( 'R4E.png' ),pg.image.load( 'R5E.png' ),pg.image.load( 'R6E.png' ),pg.image.load( 'R7E.png' ),pg.image.load( 'R8E.png' ),pg.image.load( 'R9E.png' ) ]
    walkLeft =  [pg.image.load( 'L1E.png' ) ,pg. image . load ( 'L2E.png' ) ,pg.image.load( 'L3E.png' ) ,pg.image.load( 'L4E.png' ),pg.image.load( 'L5E.png' ),pg.image.load( 'L6E.png' ),pg.image.load( 'L7E.png' ),pg.image.load( 'L8E.png' ),pg.image.load( 'L9E.png' ) ]
    def __init__(self ,x ,y ,wid ,hei ,end ): 
        self.x : int = x # position in x = 50
        self.y : int = y # position in y =358
        self.wid : int = wid # width of character 110
        self.hei : int = hei # type: ignore # height if character 120
        self.vel : int = 6 # velocity of character 
        self.walkCount : int = 0  # count for the frame for animation
        self.frame : int = 27 # frame per second deliver
        self.jumpCount : int = 7
        self.temp : int = y
        self.isJump : bool = False
        self.maxhealth : int = randint(2,10) 
        self.health : int = self.maxhealth
        self.visible : bool = True
        self.end : int = end 
        self.path = [50 ,self.end]
        self.hitbox = ( self.x + 20 ,self.y ,28 ,60)

    def draw(self ,win):
        self.move()    
        if self.walkCount + 1 >= self.frame :
            self.walkCount = 0
        elif self.vel > 0 :
            win.blit(self.walkRight[self.walkCount//3] ,(self.x ,self.y))
            self.hitbox = ( self.x + 18 ,self.y ,26 ,58)
            self.walkCount += 1
        else :
            win.blit(self.walkLeft[self.walkCount//3] ,(self.x ,self.y))
            self.hitbox = ( self.x + 24 ,self.y ,26 ,58)
            self.walkCount += 1 
        pg.draw.rect(win,(255,0,0) ,(self.hitbox[0] - 10  ,self.hitbox[1] - 10,50 ,10 ) )
        pg.draw.rect(win,(0,255,0) ,(self.hitbox[0] - 10  ,self.hitbox[1] - 10,50 - (50//self.maxhealth)*(self.maxhealth - self.health ) ,10 ) )
        #pg.draw.rect(win ,(255,0,0) ,self.hitbox , 2 )
        
    def move(self): 
        if self.vel > 0 :
            if self.x + self.vel < self.path[1] :
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
            self.y = self.temp
        else :
            if self.x - self.vel > self.path[0] :
                self.x += self.vel
            else:
                self.vel *= -1 
                self.walkCount = 0
            self.y = self.temp - 120
    def hit(self ):
        if self.health >1 :
            self.health -= 1
        else :
            if man.x > WINDO_WIDTH*2/3 :    
                self.x = man.x - WINDO_WIDTH//3
            
            elif man.x < WINDO_WIDTH/3:
                    self.x = man.x + WINDO_WIDTH//3

            else :
                if man.right :
                    self.x = man.x + 200 
                else :
                    self.x = man.x - 200
            self.vel = randint(4,8)
            self.maxhealth = randint(2,self.maxhealth + 3) 
            self.health = self.maxhealth

# create a object 
win = pg.display.set_mode((WINDO_WIDTH ,WINDO_HEIGHT))
# set the window size 
pg.display.set_caption("bla bla")

# time clock 
clock = pg.time.Clock()

def re_draw():
    win.blit(bg , (0 ,0))
    text = font.render(f'Score : {Score}' ,0 ,(150,16,8) )
    win.blit(text ,(50 ,20))
    for i in range(man.lifeCount):
        win.blit(life[0],(WINDO_WIDTH//2-120+i*70,0))
    man.draw(win)
    gob.draw(win)
    for blast in blasts :
        blast.draw(win)
    pg.display.update()

font = pg.font.SysFont('comicscans' ,30 ,True ,False )
man = player(50 ,358 ,64 ,64)
gob = enemy(150 ,362 ,64 ,64 , WINDO_WIDTH - 100 )
blasts = []
shootLoop : int = 0
# main game starts 
run = True 
# loop begins 
while run :
    clock.tick(man.frame)

    if man.hitbox[0] > gob.hitbox[0]  and  man.hitbox[0] < gob.hitbox[0] + gob.hitbox[2] :
            if man.hitbox[1] > gob.hitbox[1]  and man.hitbox[1] < gob.hitbox[1] + gob.hitbox[3]:
                man.hit()
                Score -= 5
    '''if man.hitbox[0] in  range(gob.hitbox[0],gob.hitbox[0]+gob.hitbox[2])  and  man.hitbox[1] in range(gob.hitbox[1],gob.hitbox[1]+gob.hitbox[3]) :
            man.hit()
            Score -= 5'''
    

    if shootLoop > 0 :
        shootLoop += 1
    if shootLoop > 5 :
        shootLoop = 0
    # check the event and checks for logic 
    for event in pg.event.get():
        # for exit the game 
        if event.type == pg.QUIT :
            run = False
    for blast in blasts :
        if blast.hitbox[0] + blast.radius > gob.hitbox[0]  and  blast.hitbox[0] - blast.radius < gob.hitbox[0] + gob.hitbox[2] :
            if blast.hitbox[1] + blast.radius > gob.hitbox[1]  and blast.hitbox[1] - blast.radius < gob.hitbox[1] + gob.hitbox[3]:
        #if (blast.hitbox[0] + blast.radius) in  range(gob.hitbox[0],gob.hitbox[0]+gob.hitbox[2])  and  (blast.hitbox[1] + blast.radius) in range(gob.hitbox[1],gob.hitbox[1]+gob.hitbox[3]) :
                hitsound[0].play() if gob.health > 1 else hitsound[1].play()        
                Score += 1 if not(blast.iscosmic) else 5
                if blast.iscosmic :
                    gob.health = 0 
                gob.hit()
                blasts.pop(blasts.index(blast))


        if blast.x < WINDO_WIDTH and blast.x > 0 :
            blast.x += blast.vel
        else :
            blasts.pop(blasts.index(blast))
    # take the input from the player/user
    keys = pg.key.get_pressed()

    if keys[pg.K_x]:
        break
    if keys[pg.K_SPACE] and shootLoop == 0 :
        flame_sound[0].play()
        if man.left:
            facing = -1
        else :
            facing = 1
    
        if len(blasts) < man.blastCount :
            blasts.append(projectile(round(man.x + man.wid//2),round(man.y + man.hei//2) ,facing))
        shootLoop = 1

    if keys[pg.K_TAB]:
        flame_sound[1].play()
        if man.left:
            facing = -2
        else :
            facing = 2
    
        if len(blasts) < man.cosmic_blastcount :
            blasts.append(projectile(round(man.x + man.wid//2),round(man.y + man.hei//2) ,facing))

    # if left key is pressed then move left (decrease x) and bound in box 
    if keys[pg.K_LEFT] and man.x > man.vel :
        man.x -= man.vel
        man.left = True 
        man.right = False
        man.standing = False
    # if right key is pressed then move right (increase x) and bound in box 
    elif keys[pg.K_RIGHT] and man.x < WINDO_WIDTH - man.wid - man.vel :
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    # character at stationary position 
    else :
        man.standing = True        
        man.walkCount = 0 


    # checks for yhe character command to not jump
    if not(man.isJump) :
        # if space bar is pressed then character jumps 
        if keys[pg.K_UP]:
            man.isJump = True

    # if the character has to be jump then
    else :
        # select the jump len from 10 to -10 
        if man.jumpCount >= -10 :
            # for going upward in jump 
            man.neg = 1
            if man.jumpCount < 0 :
                # going downward in jump
                man.neg = -1
                # quadratic equn. for jump animation (gives an acceleration effet )
            man.y -= (man.jumpCount ** 2) * 0.5 * man.neg
            # change the value for frame
            man.jumpCount -= 1
            # when one jump is occured then 
        else :
            # reset to initial default values for jump
            man.isJump = False 
            man.jumpCount = 10

    # redraw the background of window
    re_draw()
# end or terminate
pg.quit()