#dependencies
import pygame
import os #used to find paths to static assests

#all constants are in ALL CAPS
#define the screen and the width and height of screen
WIDTH,HEIGHT=900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#define the window's name
pygame.display.set_caption("Joe's GUI")
#define the fps constant
FPS=60
#define a velocity that all rectangles move at
VEL=5
#bullet velocity
BULLET_VEL=7
#max number of bullets
MAX_RENDERED_BULLETS=3
#define border in the middle of the screen
BORDER=pygame.Rect(445,0,10,HEIGHT)#445 becuase it draws from top right so we compensate so it looks like it drew from the middle
#all used rgb colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)
#all static assets (resized and rotated)
SPACESHIP_WIDTH,SPACESHIP_HEIGHT=55,40
YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","spaceship_yellow.png"))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","spaceship_red.png"))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

#all events
YELLOW_HIT=pygame.USEREVENT+1 #we plus one here to make this events int-id uniqe
RED_HIT=pygame.USEREVENT+2 #we plus two here to make this events int-id uniqe

#draw function
def draw_window(red,yellow,red_bullets,yellow_bullets):
    """change the background"""
    WIN.fill(WHITE)# set b.g. color r,g,b
    pygame.draw.rect(WIN,BLACK,BORDER)#params: (where draw to?,color,rectangle drawn)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))#blit used for writing text or images to screen
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
    pygame.display.update()
def yellow_handle_movement(keys_pressed,yellow_rec):
    """all of the movement for the yellow ship"""
    if keys_pressed[pygame.K_a] and yellow_rec.x-VEL>0:#left
        yellow_rec.x-=VEL
    if keys_pressed[pygame.K_d] and yellow_rec.x+yellow_rec.width+VEL<BORDER.x:#right
        yellow_rec.x+=VEL
    if keys_pressed[pygame.K_w] and yellow_rec.y-VEL>0:#up
        yellow_rec.y-=VEL
    if keys_pressed[pygame.K_s] and yellow_rec.y+yellow_rec.height+VEL<HEIGHT:#down
        yellow_rec.y+=VEL
def red_handle_movement(keys_pressed,red_rec):
    """all of the movement for the red ship"""
    if keys_pressed[pygame.K_LEFT] and red_rec.x-VEL>BORDER.x+BORDER.width:#left
        red_rec.x-=VEL
    if keys_pressed[pygame.K_RIGHT] and red_rec.x+red_rec.width+VEL<WIDTH:#right
        red_rec.x+=VEL
    if keys_pressed[pygame.K_UP] and red_rec.y-VEL>0:#up
        red_rec.y-=VEL
    if keys_pressed[pygame.K_DOWN] and red_rec.y+red_rec.height+VEL<HEIGHT:#down
        red_rec.y+=VEL
def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    """handle all bullets and their movement,collsion,etc"""
    # yellow bullets
    for bullet in yellow_bullets:
        bullet.x+=BULLET_VEL
        #check for collisions
        if red.colliderect(bullet):
            #post event so we can interact with the list in the main function
            pygame.event.post(pygame.event.Event(RED_HIT))
            #remove the bullet
            yellow_bullets.remove(bullet)
    # red bullets
    for bullet in red_bullets:
        bullet.x-=BULLET_VEL
        #check for collisions
        if yellow.colliderect(bullet):
            #post event so we can interact with the list in the main function
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            #remove the bullet
            red_bullets.remove(bullet)
#main game loop function
def main():
    """game loop, as well as collision detectors etc"""
    #hit boxes for spaceships
    red_rec=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)#args are "x,y,width,height"
    yellow_rec=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)#^
    
    #list of all bullets
    red_bullets=[]
    yellow_bullets=[]
    
    clock=pygame.time.Clock()#define clock object
    #flag and game loop
    running=True
    while running:
        #hard limit the fps
        clock.tick(FPS)#limit this while loop to 60 runs per second
        #loop through all of the events. So we can bind to them if needed
        for event in pygame.event.get():
            #bind to quit event
            if event.type==pygame.QUIT:
                running=False
            #bind to keyDown event
            if event.type==pygame.KEYDOWN:
                # left ctrl
                if event.key==pygame.K_LCTRL and len(yellow_bullets)<MAX_RENDERED_BULLETS:
                    bullet=pygame.Rect(yellow_rec.x+yellow_rec.width,yellow_rec.y+int(yellow_rec.height/2)-2,10,5)
                    yellow_bullets.append(bullet)
                # right ctrl
                if event.key==pygame.K_RCTRL and len(red_bullets)<MAX_RENDERED_BULLETS:
                    bullet=pygame.Rect(red_rec.x,red_rec.y+int(red_rec.height/2)-2,10,5)
                    red_bullets.append(bullet)
        #if something isn't event based it goes here
        keys_pressed=pygame.key.get_pressed()#returns all keys pressed down during this frame
        #move yellow and redif needed
        yellow_handle_movement(keys_pressed,yellow_rec)
        red_handle_movement(keys_pressed,red_rec)
        #bullets move
        handle_bullets(yellow_bullets,red_bullets,yellow_rec,red_rec)
        draw_window(red_rec,yellow_rec,red_bullets,yellow_bullets)
    #when game loop ends, close the window
    pygame.quit()

#only run main() if this file was run directly and not imported
if __name__=="__main__":
    main()

#1:12:21 on https://www.youtube.com/watch?v=jO6qQDNa2UY