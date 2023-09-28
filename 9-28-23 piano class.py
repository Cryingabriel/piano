import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("python piano program")#sets the window title
screen = pygame.display.set_mode((1000, 800))#creates game screen
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
press = False
pressed = False
#audio stuff!
pygame.mixer.init()
mpsomething = "key0X.mp3"
keys = []
for i in range(24):
    if i < 9:
        keys.append(pygame.mixer.Sound(mpsomething.replace("X",str(i+1))))
    else:
        keys.append(pygame.mixer.Sound(mpsomething.replace("0X",str(i+1))))


sharps = (2,4,6,9,11,14,16,18,21,23)
#this holds onto what key the user has pressed
key: int = 0

class pianokeys():
    def __init__(self, xpos, ypos, key):
        global sharps
        self.xpos = xpos
        self.ypos = ypos
        self.key = key
        if self.key in sharps:
            self.sharp = True
            self.xsize = 20
            self.ysize = 150
            self.tone = 25
        else:
            self.sharp = False
            self.xsize = 40
            self.ysize = 200
            self.tone = 255
        
        
        
    
    def draw(self,pixel):
        #key
        pygame.draw.rect(pixel, (self.tone,self.tone,self.tone), (self.xpos,self.ypos,self.xsize,self.ysize))
        #outline
        pygame.draw.rect(pixel, (0, 0, 0), (self.xpos, self.ypos, self.xsize, self.ysize), 2)

    def collide(self,mouse,held,alrkey = 0) -> int:
        if mouse[0] > self.xpos and mouse[0] < self.xpos+self.xsize and mouse[1] >self.ypos and mouse[1] < self.ypos+self.ysize and held:
            return self.key
        else:
            return 0






wheatley = [pianokeys(30,0,2),pianokeys(70,0,4),pianokeys(110,0,6),pianokeys(190,0,9),pianokeys(230,0,11),pianokeys(310,0,14),pianokeys(350,0,16),pianokeys(390,0,18),pianokeys(470,0,21),pianokeys(510,0,23),pianokeys(0,0,1),pianokeys(40,0,3),pianokeys(80,0,5),pianokeys(120,0,7),pianokeys(160,0,8),pianokeys(200,0,10),pianokeys(240,0,12),pianokeys(280,0,13),pianokeys(320,0,15),pianokeys(360,0,17),pianokeys(400,0,19),pianokeys(440,0,20),pianokeys(480,0,22),pianokeys(520,0,24)]
clock = pygame.time.Clock()
pianoing = True







#gameloop###################################################
while pianoing:
    print(mousePos) #this is just for testing so you can see the mouse coordinates on the screen!
    
    clock.tick(1000)


    
    for event in pygame.event.get(): #Input Section
        if event.type == pygame.QUIT: #close game window
            pianoing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            press = True

        if event.type == pygame.MOUSEBUTTONUP:
            press = False
            pressed = False

        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
    
    #update/timer section---------------------------------------    
    for i in range(len(wheatley)):
        key = wheatley[i].collide(mousePos, (press and not pressed), key)
        if key != 0:
            if press:
                pressed = True
            break
    
    #input section----------------------------------------------


    #render section---------------------------------------------
    for i in range(len(wheatley)):
        wheatley[len(wheatley)-(i+1)].draw(screen)
    print(key)
    #if a key is pressed, highlight in grey and play the sound:
    if press == True:
        if key == 0:
            print("no key")
        else:
            pygame.mixer.Sound.play(keys[key-1])
    
    pygame.display.flip() #always needed at the end of every game loop!
    

#end game loop##############################################

pygame.quit()