#dependencies
import pygame

#all constants are in ALL CAPS
#define the screen and the width and height of screen
WIDTH,HEIGHT=900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#define the window's name
pygame.display.set_caption("Joe's GUI")


#main game loop function
def main():
    """game loop, as well as collision detectors etc"""
    #flag and game loop
    running=True
    while running:
        #loop through all of the events. So we can bind to them if needed
        for event in pygame.event.get():
            #bind to quit event
            if event.type==pygame.QUIT:
                running=False
    #when game loop ends, close the window
    pygame.quit()

#only run main() if this file was run directly and not imported
if __name__=="__main__":
    main()

#13:22 on https://www.youtube.com/watch?v=jO6qQDNa2UY