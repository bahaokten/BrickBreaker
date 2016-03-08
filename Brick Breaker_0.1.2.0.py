from __future__ import print_function, division
import pygame
from math import pi
#brickler icin yeni surface yarat




def test():
    pass
#================================####INTERACTIVE OBJECTS####================================#
class Paddle(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self,x,y,state,size,velX):
        self.state = state
        self.velX = velX
        self.size = size
        self.x = x
        self.y = y
        self.add = 0
        if size == "medium":
            self.add = 0
        elif size == "small":
            self.add = -20
        else:
            self.add = 20
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
    def move(self):
       if data_left:
            self.x -= self.velX
       elif data_right:
            self.x += self.velX

    def create(self):
       self.image = pygame.Surface([self.add+98, 21],pygame.SRCALPHA,32)
       self.image = self.image.convert_alpha()
       pygame.draw.ellipse(self.image,(0,0,0),(0,0,35,20))
       pygame.draw.arc(self.image, (255,255,255), (0,0,35,20), pi/2, 3*pi/2)
       pygame.draw.ellipse(self.image, (0,0,0), (self.add+63,0,35,20))
       pygame.draw.arc(self.image, (255,255,255), (self.add+63,0,35,20), 3*pi/2, 5*pi/2)
       pygame.draw.rect(self.image, (0,0,0), (18,0,self.add+62,20))
       pygame.draw.polygon(self.image, (255,0,0), ((18,20),(28,0),(38,20)))
       pygame.draw.polygon(self.image, (255,0,0), ((self.add+80,20),(self.add+70,0),(self.add+60,20)))
       pygame.draw.line(self.image,(255,255,255), (18,0),(self.add+80,0))
       pygame.draw.line(self.image,(255,255,255), (18,20),(self.add+80,20))

    def draw(self):
        screen.blit(self.image, (self.x,self.y))


       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       #self.rect = self.image.get_rect()
"""
class Paddle(object):
    #Constructor
    def __init__(self,x,y,state,size,velX): #You always call self in python
        print ("OOOOOOOOOO")
        self.state = state
        self.velX = velX
        self.size = size
        self.x = x
        self.y = y
        self.add = 0
        if size == "medium":
            self.add = 0
        elif size == "small":
            self.add = -20
        else:
            self.add = 20

    def move(self):
        #print (data_left)
        if data_left:
            self.x -= self.velX
        elif data_right:
            self.x += self.velX

    def draw(self):
        #print (self.x)
        global data_actionground
        tmp = self.x+self.add
        pygame.draw.ellipse(data_actionground,(0,0,0),(self.x,self.y,35,20))
        pygame.draw.arc(data_actionground, (255,255,255), (self.x,self.y,35,20), pi/2, 3*pi/2)
        pygame.draw.ellipse(data_actionground, (0,0,0), (tmp+63,self.y,35,20))
        pygame.draw.arc(data_actionground, (255,255,255), (tmp+63,self.y,35,20), 3*pi/2, 5*pi/2)
        pygame.draw.rect(data_actionground, (0,0,0), (self.x+18,self.y,self.add+62,20))
        pygame.draw.polygon(data_actionground, (255,0,0), ((self.x+18,self.y+20),(self.x+28,self.y),(self.x+38,self.y+20)))
        pygame.draw.polygon(data_actionground, (255,0,0), ((tmp+80,self.y+20),(tmp+70,self.y),(tmp+60,self.y+20)))
        pygame.draw.line(data_actionground,(255,255,255), (self.x+18,self.y),(tmp+80,self.y))
        pygame.draw.line(data_actionground,(255,255,255), (self.x+18,self.y+20),(tmp+80,self.y+20))

    def __str__(self):
        return "Ball is" + self.color
"""
def test():
    global data_paddle
    data_paddle = Paddle(350,200,"-","medium",15)
#================================####GAME HANDLING####=====================================0##3
def constructor():
    global data_allSprites
    global data_paddle
    paddle = Paddle(350,200,"-","medium",15)
    data_paddle.add(paddle)
    data_allSprites.add(paddle)

#==TXT==#
def createText(f,size,text = "",bold = False,italic = False):
    global data_textSize
    global data_font
    data_font = pygame.font.Font(f,size,bold=bold,italic=italic)
    tmp = pygame.font.Font.size(data_font,text)
    data_textSize =  tmp

def drawText(x,y,text,R,G,B, ycor = 0,xcor = 0):
    global data_foreground
    txt = pygame.font.Font.render(data_font,text,10,(R,G,B))
    data_foreground.blit(txt, (x+xcor,y+ycor))
    print ("drawn")

def fitTextDraw(font,limW,limH,text,X1,Y1,R,G,B,Ycorrection = 0,Xcorrection = 0,bold = False,italic = False,prev = False):
    if not prev:
        f = open(font)
        tmp = 100
        createText(f,tmp,text = text,bold = bold,italic = italic)
        while data_textSize[0] > limW or data_textSize[1] > limH:
            createText(font,tmp,text = text,bold = bold,italic = italic)
            tmp -= 1
    x,y = objMid(X1,Y1,data_textSize[0],data_textSize[1])
    drawText(x,y,text, R,G,B, ycor = Ycorrection,xcor = Xcorrection)

def normTextDraw(font,x,y,size,text,R,G,B,bold = False,italic = False):
    createText(font,size,text = text,bold = bold,italic = italic)
    drawText(x,y,text,R,G,B)


    

#================================####COLLISION DETECTION####================================================================================#

def mouseCollision(X1,Y1,W,H):
    if data_mousePressedPos != ():
        if X1 < data_mousePressedPos[0] < (X1 + W) and Y1 < data_mousePressedPos[1] < (Y1 + H):
            return True
        else:
            return False

def objMid(X1,Y1,W,H):
    return (X1-(W/2),Y1-(H/2))

#================================####DRAWFUNCTIONS####================================================================================#

def drawButton(ground,X1,Y1,W,H,R1,G1,B1,R2,G2,B2,state,newState,depth = 10,middle = True):
    global data_state
    global data_tmp
    if middle:
        x,y = objMid(X1,Y1,W,H)
    else:
        x,y = X1,Y1
    pygame.draw.rect(ground,(R1,G1,B1),(x,y,W,H))
    pygame.draw.rect(ground,(R2*0.3,G2*0.3,B2*0.3),(x+depth,y+depth,W-(depth*2),H-(depth*2)))
    if data_state == state and data_tmp >= 1:
        data_tmp -= 1
        pygame.draw.rect(ground,(R2,G2,B2),(x,y,W,H))
        pygame.draw.rect(ground,(R2*0.6,G2*0.6,B2*0.6),(x+depth,y+depth,W-(depth*2),H-(depth*2)))
    if data_state == state and data_tmp == 0:
        data_tmp = ()
        data_state = newState
        pass
    if mouseCollision(x,y,W,H) and data_tmp == () and data_state != state:
        data_state = state
        data_tmp = 10

def drawMenu():
    global data_foreDraw
    global data_bgDraw
    if data_bgDraw:
        drawBackground()
        test()
        data_bgDraw = False
        fitTextDraw(data_fontFile1,80,30,"START",data_canvasX/2,data_canvasY/2,110,100,100,Ycorrection = 3)
        data_paddle.create()
    elif data_foreDraw != 0:
        data_foreground.fill((0,0,0,0))
        drawButton(data_buttonground,data_canvasX/2,data_canvasY/2,100,50,10,100,10,200,10,10,"transM","menu")
        fitTextDraw(data_fontFile1,80,30,"START",data_canvasX/2,data_canvasY/2,110,100,100,Ycorrection = 3,prev = True)
        data_foreDraw -= 1
    data_paddle.move()
    data_paddle.draw()
    

def drawBackground():
    backColor = [154,52,53]
    curtainColor = [250,0,0]
    for n in xrange(18):
        pygame.draw.rect(data_background, backColor , (n*30,n*20,data_canvasX-(60*n),data_canvasY-(40*n)))
        backColor = [154-(n*2),52+(n*9),53+(n*8)]
    for num in xrange(19):
        pygame.draw.polygon(data_background, curtainColor, (((num*10),0),(10+(num*10),0),(0,450)))
        pygame.draw.polygon(data_background, curtainColor, ((data_canvasX-(num*10),0),(data_canvasX,450),(data_canvasX-10-(num*10),0)))
        pygame.draw.polygon(data_background, curtainColor, (((num*8),data_canvasY),(10+(num*8),data_canvasY),(0,450)))
        pygame.draw.polygon(data_background, curtainColor, ((data_canvasX-(num*8),data_canvasY),(data_canvasX-10-(num*8),data_canvasY),(data_canvasX,450)))
        if not curtainColor[0] < 20+num:
                curtainColor[0] -= 5+(num)
        curtainColor[1] += 20-(num)
        curtainColor[2] += abs(num-5)
    screen.blit(data_background, (0,0))


###############MAIN FUNCTION###############

def drawGame():
    if data_state == "menu" or data_state == "transM":
        drawMenu()
    else:
        data_background.fill((255, 255, 255))
        

#================================####INITIAL CALLS####================================================================================#

def init():
    global data_state
    data_state = "menu"
    #---GENERAL---#
    global data_canvasX
    data_canvasX = 960
    global data_canvasY
    data_canvasY = 700
    global data_tmp
    data_tmp = ()
    global data_foreDraw
    data_foreDraw = 2
    global data_bgDraw
    data_bgDraw = True
    #---PADDLE---#
    global data_paddle
    data_paddle = ()
    #---FONTS&TEXTS---#
    global data_textSize
    data_textSize = 0
    global data_fontFile1
    #data_fontFile1 = "Mona Shark.otf"
    data_fontFile1 = "Font_1.ttf"
    global data_font
    data_font = ()
    #---BRICKS---#
    global data_brickSizeX
    data_brickSizeX = 64
    global data_brickSizeY
    data_brickSizeY = 3
    global data_brickSizeXSelect
    data_brickSizeXSelect = 13
    global data_brickSizeYSelect
    data_brickSizeYSelect = 5
    global data_brickYMargin
    data_brickYMargin = 10
    #---Sprites---#
    global data_allSprites
    data_allSprites = pygame.sprite.Group()
    #Paddle#
    global data_paddle
    data_paddle = pygame.sprite.Group()
    global data_paddleY
    data_paddleY = 300
    #---INPUT---#
    global data_left
    data_left = False
    global data_right
    data_right = False
    #---LEVEL---#
    global data_currentLevel
    data_currentLevel = []
    global data_lvlLayout
    data_lvlLayout   =   [[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
    global data_level1
    data_level1      =   [[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                          [[],[],["orange","-",1],["yellow","-",1],["green","-",1],["darkgreen","-",1],["darkred","-",1],["black","-",1],["darkred","-",1],\
                            ["darkgreen","-",1],["green","-",1],["yellow","-",1],["orange","-",1],[],[]],\
                          [[],[],["orange","-",1],["yellow","-",1],["green","-",1],["darkgreen","-",1],["darkred","-",1],["black","-",1],["darkred","-",1],\
                            ["darkgreen","-",1],["green","-",1],["yellow","-",1],["orange","-",1],[],[]]]
    #color,powerup,lives
    #[["white","-",1]]
    print (data_lvlLayout)
    print ("\nLevel 1")
    print (data_level1)

def main():
    global data_foreDraw
    pygame.init()
    global screen
    screen=pygame.display.set_mode((960,700))
    global data_background
    data_background = pygame.Surface(screen.get_size())
    data_background.fill((255, 255, 255))
    global data_actionground
    data_actionground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_actionground = data_actionground.convert_alpha()
    global data_buttonground
    data_buttonground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_buttonground = data_buttonground.convert_alpha()
    global data_foreground
    data_foreground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_foreground = data_foreground.convert_alpha()
# Convert Surface object to make blitting faster.
    data_background = data_background.convert()
# Copy background to screen (position (0, 0) is upper left corner).
# Create Pygame clock object.  
    clock = pygame.time.Clock()
    mainloop = True         
    FPS = 30
    init()
    ###INTERACTIVES###
    global data_left
    data_left = False
    global data_right
    data_right = False
    global data_mousePressedPos
    data_mousePressedPos = ()
    ###-----------###
    playtime = 0.0
    while mainloop:
    # Do not go faster than this framerate.
        milliseconds = clock.tick(FPS) 
        playtime += milliseconds / 1000.0 
        for event in pygame.event.get():
        # User presses QUIT-button.
            if event.type == pygame.QUIT:
                mainloop = False 
            elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
                elif event.key == pygame.K_RIGHT:
                    data_right = True
                elif event.key == pygame.K_LEFT:
                    data_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    data_right = False
                elif event.key == pygame.K_LEFT:
                    data_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                data_foreDraw = 20
                data_mousePressedPos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                data_mousePressedPos = ()
        text = "Bricks Alpha 0.2 {" + "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime) + "}"
        pygame.display.set_caption(text)
        data_actionground.fill((255,255,255,0)) 
        drawGame()
    #hersey burada olmali
        screen.blit(data_actionground, (0,0))
        if data_foreDraw != 0:
            screen.blit(data_buttonground, (0,0))
            screen.blit(data_foreground,(0,0))
        pygame.display.flip()

# Finish Pygame.  
    pygame.quit()
    
main()
