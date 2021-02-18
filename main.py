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
#all used rgb colors
WHITE=(255,255,255)
#all static assets (resized and rotated)
SPACESHIP_WIDTH,SPACESHIP_HEIGHT=55,40
YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","spaceship_yellow.png"))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","spaceship_red.png"))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

#draw function
def draw_window(red,yellow):
    """change the background"""
    WIN.fill(WHITE)# set b.g. color r,g,b
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))#blit used for writing text or images to screen
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()
#main game loop function
def main():
    """game loop, as well as collision detectors etc"""
    #hit boxes for spaceships
    red_rec=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)#args are "x,y,width,height"
    yellow_rec=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)#^
    clock=pygame.time.Clock()#define clock object
    #flag and game loopmmmmmmmmmmmmm
        #hard limit the fps
        clock.tick(FPS)#limit this while loop to 60 runs per second
        #loop through all of the events. So we can bind to them if needed
        for event in pygame.event.get():
            #bind to quit event
            if event.type==pygame.QUIT:
                running=False
        #if something isn't event based it goes here
        keys_pressed=pygame.key.get_pressed()#returns all keys pressed down during this frame
        if keys_pressed[pygame.K_a]:#left ##working here##
        draw_window(red_rec,yellow_rec)
    #when game loop ends, close the window
    pygame.quit()

#only run main() if this file was run directly and not imported
if __name__=="__main__":
    main()

#34:48 on https://www.youtube.com/watch?v=jO6qQDNa2UY