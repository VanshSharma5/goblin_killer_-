import pygame as pg


"""
the coordinate are store in the top left 
"""


# begin 
pg.init()

# parameter of the program 
WINDO_HEIGHT : int = 500 # height of window
WINDO_WIDTH : int = 800 # height of window
x : int = 50 # position in x
y : int = 358-80 # position in y
wid : int = 110 # width of character 
hei : int = 120 # height if character 
vel : int = 5 # velocity of character 
delay : int = 50 # refresh rate of window screen 
jumpCount : int = 10 # hight parameter of jump 
neg : int = 1 # use to control up and down in jump
frame : int = 27 # frame per second deliver
walkCount : int = 0 # count for the frame for animation
morph : int = 80 # tells what power is activate
isJump : bool = False
left : bool = False 
right : bool = False 
power : bool = False

# create a object 
win = pg.display.set_mode((WINDO_WIDTH ,WINDO_HEIGHT))
# set the window size 
pg.display.set_caption("bla bla")

# time clock 
clock = pg.time.Clock()

# insertin the images of character and backgroung 

walkRight = [pg.image.load( 'R1.png' ) ,pg. image . load ( 'R2.png' ) ,pg.image.load( 'R3.png' ) ,pg.image.load( 'R4.png' ),pg.image.load( 'R5.png' ),pg.image.load( 'R6.png' ),pg.image.load( 'R7.png' ),pg.image.load( 'R8.png' ),pg.image.load( 'R9.png' ) ]

lionRight = [pg.image.load( 'lion1.gif' ) ,pg. image . load ( 'lion2.gif' ) ,pg.image.load( 'lion3.gif' ) ,pg.image.load( 'lion4.gif' ),pg.image.load( 'lion5.gif' ),pg.image.load( 'lion6.gif' ),pg.image.load( 'lion7.gif' ),pg.image.load( 'lion8.gif' ),pg.image.load( 'lion9.gif' ),pg.image.load('lion10.gif') ]

walkLeft =  [pg.image.load( 'L1.png' ) ,pg. image . load ( 'L2.png' ) ,pg.image.load( 'L3.png' ) ,pg.image.load( 'L4.png' ),pg.image.load( 'L5.png' ),pg.image.load( 'L6.png' ),pg.image.load( 'L7.png' ),pg.image.load( 'L8.png' ),pg.image.load( 'L9.png' ) ]
char = pg.image.load( 'ben.png' )
bg = pg.image.load('BG.jpg')

# defining a function to draw 
def re_draw( ):
    global walkCount,x
    win.blit(bg ,(0 ,0))
    if walkCount + 1 >= frame:
        walkCount = 0
    if left :
        win.blit(walkLeft[walkCount//3] , ( x , y + morph ))
        walkCount += 1
    elif right :
        win.blit(lionRight[walkCount//3] , ( x, y ))
        walkCount += 1
    else :
        win.blit(char,(x,y))  


    '''pg.draw.rect(win ,(255 ,0,0 ) ,(x, y, wid, hei ))'''
    pg.display.update()





# main game starts 
run = True 
# loop begins 
while run :
    clock.tick(frame)
    # set wait time for response from user
    pg.time.delay(delay)
    # check the event and checks for logic 
    for event in pg.event.get():
        # for exit the game 
        if event.type == pg.QUIT :
            run = False
    
    # take the input from the player/user
    keys = pg.key.get_pressed()

    # if left key is pressed then move left (decrease x) and bound in box 
    if keys[pg.K_LEFT] and x > vel :
        x -= vel
        left = True 
        right = False
        power = False
    # if right key is pressed then move right (increase x) and bound in box 
    elif keys[pg.K_RIGHT] and x < WINDO_WIDTH - wid - vel :
        x += vel
        right = True
        left = False
        power = False
    # if up key is press
    elif keys[pg.K_t]:
        right = False
        left = False
        power = True
        morph = 'lion'

    # character at stationary position 
    else :
        right = False
        left = False
        power = False
        walkCount = 0 
    # checks for yhe character command to not jump
    if not(isJump) :
        # if space bar is pressed then character jumps 
        if keys[pg.K_SPACE]:
            isJump = True
        
        '''            
        # if up key is pressed then move up (increase y) and bound in box 
        if keys[pg.K_UP] and y > vel:
            y -= vel
        # if down key is pressed then move down (decrease y) and bound in box 
        if keys[pg.K_DOWN] and  y < 500 - hei - vel:
            y += vel
        # to give the ability to jump 
        '''
    # if the character has to be jump then
    else :
        # select the jump len from 10 to -10 
        if jumpCount >= -10 :
            # for going upward in jump 
            neg = 1
            if jumpCount < 0 :
                # going downward in jump
                neg = -1
                # quadratic equn. for jump animation (gives an acceleration effet )
            y -= (jumpCount ** 2) * 0.5 * neg
            # change the value for frame
            jumpCount -= 1
            # when one jump is occured then 
        else :
            # reset to initial default values for jump
            isJump = False 
            jumpCount = 10

    # redraw the background of window
    re_draw()
    '''
    # fill the background before drawing the new rectangle character over the other
    win.fill((0,0,0))
        
    # drawing of character or avatar 
    pg.draw.rect(win ,(255,0,255) ,(x,y,wid ,hei))
    # to update display each time the loop runs
    pg.display.update()
    '''


# end or terminate
pg.quit()