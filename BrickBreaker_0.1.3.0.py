from __future__ import print_function, division
import pygame
from math import pi

RED = (255,0,0)
BLACK = (0,0,0)
LIGHTBLACK = (20,20,20)
WHITE = (255,255,255)
GREEN = (0,155,0)
BLUE = (0,0,155)
LIGHTGRAY = (136,136,136)
ORANGE = (255,102,0)
YELLOW = (255,255,0)
DARKGREEN = (0,80,0)
DARKRED = (139,0,0)
"""
def redrawAll():
      #Redraws all
      print "redrawn"
      canvas.delete(ALL)
      drawGame()
      if canvas.data.takenNum["b"] == 15:
            canvas.data.spriteState = "finished"
            canvas.delete(ALL)
            drawGame()
            drawWinner()
      elif canvas.data.takenNum["w"] == 15:
            canvas.data.spriteState = "finished"
            canvas.delete(ALL)
            drawGame()
            drawWinner()
"""
#================================####INTERACTIVE OBJECTS####================================#

class Paddle(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self,x,y,state,size,velX):
        self.state = state
        self.velX = velX
        self.size = size
        self.rect = [x,y]
        self.add = 0
        if size == "medium":
            self.add = 0
        elif size == "small":
            self.add = -20
        else:
            self.add = 20
        pygame.sprite.Sprite.__init__(self)

    def update(self):
       if data_left:
            self.rect[0] -= self.velX
       elif data_right:
            self.rect[0] += self.velX

    def create(self):
       self.image = pygame.Surface([self.add+98, 21],pygame.SRCALPHA,32)
       self.image = self.image.convert_alpha()
       pygame.draw.ellipse(self.image,BLACK,(0,0,35,20))
       pygame.draw.arc(self.image, (55,55,55), (0,0,35,20), pi/2, 3*pi/2,3)
       pygame.draw.ellipse(self.image, BLACK, (self.add+63,0,35,20))
       pygame.draw.arc(self.image, (55,55,55), (self.add+63,0,35,20), 3*pi/2, 5*pi/2,3)
       pygame.draw.rect(self.image, BLACK, (18,0,self.add+62,20))
       pygame.draw.polygon(self.image, (155,0,0), ((18,20),(28,0),(38,20)))
       pygame.draw.polygon(self.image, (155,0,0), ((self.add+80,20),(self.add+70,0),(self.add+60,20)))
       pygame.draw.line(self.image,(55,55,55), (18,0),(self.add+80,0),5)
       pygame.draw.line(self.image,(55,55,55), (18,20),(self.add+80,20),5)

    def info(self):
        print (self.rect)
    
#================================####GAME HANDLING####=====================================0##3
def constructor(level):
    global data_allSprites
    global data_paddle
    paddle = Paddle(350,200,"-","medium",15)
    data_paddle = paddle
    data_allSprites.add(data_paddle)#,something)


#==TXT==#

#NEEDS font to be created before called
def normTextDraw(font,x,y,size,text,R,G,B,bold = False,italic = False,create = False):
    if create:
        createText(font,size,text = text,bold = bold,italic = italic)
    drawText(x,y,text,R,G,B)

#--FitTextDraw Module--#
    
def fitTextDraw(font,limW,limH,text,X1,Y1,R,G,B,Ycorrection = 0,Xcorrection = 0,bold = False,italic = False,prev = False):
    global data_textSize
    if not prev:
        tmp = 100
        createText(font,tmp,text = text,bold = bold,italic = italic)
        while data_textSize[0] > limW or data_textSize[1] > limH:
            createText(font,tmp,text = text,bold = bold,italic = italic)
            tmp -= 1
    drawText(X1+(limW-data_textSize[0])/2,Y1+(limH-data_textSize[1])/2,text, R,G,B, ycor = Ycorrection,xcor = Xcorrection)

def drawText(x,y,text,R,G,B, ycor = 0,xcor = 0):
    global data_font
    txt = data_font.render(text,10,(R,G,B))
    data_textground.blit(txt, (x+xcor,y+ycor))

def createText(f,size,text = "",bold = False,italic = False):
    global data_textSize
    global data_font
    data_font = pygame.font.Font(f,size,bold=bold,italic=italic)
    tmp = pygame.font.Font.size(data_font,text)
    data_textSize =  tmp

#==BUTTONS==#

class Button(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, X, Y, W, H, R1, G1, B1, R2, G2, B2, newState, text, font, R3, G3, B3, depth = 10, middle = False, bold= False, italic = False, usePrevFont = False, Ycor = 0):
        self.X = X
        self.Y = Y
        self.W = W
        self.H = H
        self.R1 = R1
        self.G1 = G1
        self.B1 = B1
        self.R2 = R2
        self.G2 = G2
        self.B2 = B2
        self.R3 = R3
        self.G3 = G3
        self.B3 = B3
        self.bold = bold
        self.italic = italic
        self.prev = usePrevFont
        self.font = font
        self.Ycor = Ycor
        #NEW GAME STATE ISSUED
        self.newState = newState
        self.depth = depth
        self.middle = middle
        self.isPressed = False
        self.text = text
        self.selfState = "u"
        if middle:
            self.X,self.Y = objMid(self.X,self.Y,self.W,self.H)
            self.rect = [self.X,self.Y]
        else:
            self.rect = [X,Y]
        pygame.sprite.Sprite.__init__(self) 
        

    def update(self,state):
        global data_spriteGroup_buttons
        if mouseCollision(self.X,self.Y,self.W,self.H):
            #self.image.fill((0,0,0,0))
            if state == "d":
                self.selfState = "d"
                pygame.draw.rect(self.image,(self.R2,self.G2,self.B2),(0,0,self.W,self.H))
                pygame.draw.rect(self.image,(self.R2*0.6,self.G2*0.6,self.B2*0.6),(self.depth,self.depth,self.W-(self.depth*2),self.H-(self.depth*2)))
                data_buttonground.blit(self.image, (self.X,self.Y))

        if state == "u" and self.selfState == "d":
            self.selfState = "u"
            pygame.draw.rect(self.image,(self.R1,self.G1,self.B1),(0,0,self.W,self.H))
            pygame.draw.rect(self.image,(self.R2*0.3,self.G2*0.3,self.B2*0.3),(self.depth,self.depth,self.W-(self.depth*2),self.H-(self.depth*2)))
            data_buttonground.blit(self.image, (self.X,self.Y))
        
    def create(self):
        self.image = pygame.Surface([screen.get_size()[0],screen.get_size()[1]],pygame.SRCALPHA,32)
        pygame.draw.rect(self.image,(self.R1,self.G1,self.B1),(0,0,self.W,self.H))
        pygame.draw.rect(self.image,(self.R2*0.3,self.G2*0.3,self.B2*0.3),(self.depth,self.depth,self.W-(self.depth*2),self.H-(self.depth*2)))
        self.buttonTextCreate()

    def buttonTextCreate(self):
        fitTextDraw(self.font, self.W-2*self.depth, self.H-2*self.depth, self.text, self.X+self.depth, self.Y+self.depth, self.R3, self.G3, self.B3, bold= self.bold, italic = self.italic\
                    , prev = self.prev, Ycorrection = self.Ycor)

    def kill(self, text):
        if text == self.text or text == "":
            # if "" is entered it means all sprites will be deleted whatsoever
            data_spriteGroup_buttons.remove(self)
            data_textground.fill((0,0,0,0),(self.X,self.Y,self.W,self.H))
            updateButtons(data_buttonground)

def updateButtons(ground):
    data_buttonground.fill((0,0,0,0))
    data_spriteGroup_buttons.draw(ground)

def buttonCreator(X,Y,W,H,R1,G1,B1,R2,G2,B2,newState,text, font, R3, G3, B3,depth = 10,mid = False,bold = False, italic= False, usePrevFont = False,Ycor = 0):
    global data_spriteGroup_buttons
    button = Button(X,Y,W,H,R1,G1,B1,R2,G2,B2,newState,text,font, R3, G3, B3, depth = depth,middle = mid, bold = bold, italic = italic, usePrevFont = usePrevFont,Ycor = Ycor)
    data_spriteGroup_buttons.add(button)#,something)

def spawnCreatedButtons(ground):
    for i in xrange(len(data_spriteGroup_buttons.sprites())):
        data_spriteGroup_buttons.sprites()[i].create()
    data_spriteGroup_buttons.draw(ground)
    
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

#listeden okumak yerine spritedan okumaya cevir
def drawLevelSelect():
    #pygame.draw.rect(data_buttonground, LIGHTGRAY , (0,0,data_canvasX,data_canvasY),0)
    #canvas.create_text(canvas.data.canvasWidth/2,50,text = "Level Select",font = "Times 30",anchor = CENTER, fill = "red")
    tmp = 50
    pygame.draw.rect(data_buttonground, (90,116,149),(tmp,tmp,13*15,5*26))
    drawLevel(data_level1,data_buttonground,13,5,False,tmp,tmp,1)
    pygame.draw.rect(data_buttonground, BLACK, (tmp,tmp,13*15,5*26),5) 
    #drawLevel(data_level1,data_buttonground,64,25)

def drawLevel(level,ground,width = 0,height = 0,marginY = True,addX = 0,addY = 0,outline = 5):
    if width == 0:
        width = data_brickSizeX
    if height == 0:
        height = data_brickSizeY
    if marginY == True:
        marginY = data_brickYMargin
    else:
        marginY = 0
    rows = len(level)
    cols = len(level[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if len(level[row][col]) != 0:
                drawBrick(col,row,level[row][col][0],width,height,marginY,addX,addY,outline,ground = ground)

def drawBrick(col,row,cl,width,height,marginY,addX,addY,outline,ground = ()):
    if ground == ():
        ground = data_actionground
    #Col(x) max = 0-14
    #Row(y) max = 0-25
    #global data_actionground
    if col >= 15 or row >= 26:
        return False
    else:
        pygame.draw.rect(ground, cl,(addX+col*width,addY+marginY+row*height,width,height))
        pygame.draw.rect(ground, BLACK,(addX+col*width,addY+marginY+row*height,width,height),outline)
"""
def drawMenu():
    global data_foreDraw
    global data_bgDraw
    if data_bgDraw:
        drawMenuBackground()
        constructor("o")
        data_bgDraw = False
        fitTextDraw(data_fontFile1,80,30,"START",data_canvasX/2,data_canvasY/2,110,100,100,Ycorrection = 3)
        #normTextDraw(data_fontFile1,data_canvasX/2,50,12,"Brick Breaker",0,0,0,bold = False,italic = False)
        ##TEMP##
        data_paddle.create()
    elif data_foreDraw != 0:
        data_foreground.fill((0,0,0,0))
        drawLevelSelect()
        normTextDraw(data_fontFile1,data_canvasX/2,50,12,"Brick Breaker",0,0,0,bold = False,italic = False)
        data_foreDraw -= 1
    data_allSprites.update()
    data_allSprites.draw(data_actionground)
"""

def drawMenu():
    global data_tick1
    if not data_tick1:
        drawMenuBackground()
        constructor("0")
        data_paddle.create()
        #self, X, Y, W, H, R1, G1, B1, R2, G2, B2, newState, text, font, R3, G3, B3, depth = 10, middle = True, bold= False, italic = False, usePrevFont = False)
        buttonCreator(480,350,100,50,105,250,250,50,150,150,"Menu","START", data_fontFile1,100,50,50, mid= True, Ycor = 4)
        spawnCreatedButtons(data_buttonground)
        normTextDraw(data_fontFile1,data_canvasX/2,50,12,"Brick Breaker",0,0,0,bold = False,italic = False)
        data_tick1 = True
        print ("done!")
    data_allSprites.update()
    data_allSprites.draw(data_actionground)
    

def drawMenuBackground():
    global data_background
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


###############MAIN FUNCTION###############

def drawGame():
    if data_state == "menu":
        drawMenu()
    else:
        data_background.fill((100, 255, 255))
        

#================================####INITIAL CALLS####================================================================================#

def temp(): 
    global data_tick1
    if not data_tick1:
        data_tick1 = True
        #self, X, Y, W, H, R1, G1, B1, R2, G2, B2, newState, text, font, R3, G3, B3, depth = 10, middle = True, bold= False, italic = False, usePrevFont = False)
        buttonCreator(480,350,100,50,105,250,250,50,150,150,"Menu","START", data_fontFile1,100,50,50, mid= True, Ycor = 4)
        spawnCreatedButtons(data_buttonground)
  
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
    global data_bgDraw
    data_bgDraw = True
    global data_tick1
    data_tick1 = False
    #--BUTTON--#
    global data_spriteGroup_buttons
    data_spriteGroup_buttons = pygame.sprite.Group()
    #---PADDLE---#
    global data_paddle
    data_paddle = ()
    #---FONTS&TEXTS---#
    global data_textSize
    data_textSize = 0
    global data_fontFile1
    #data_fontFile1 = "Mona Shark.otf"
    data_fontFile1 = "Font_1.ttf"
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
    #global data_paddle
    data_paddle = ()
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
                          [[],[],[ORANGE,"-",1],[YELLOW,"-",1],[GREEN,"-",1],[DARKGREEN,"-",1],[DARKRED,"-",1],[LIGHTBLACK,"-",1],[DARKRED,"-",1],\
                            [DARKGREEN,"-",1],[GREEN,"-",1],[YELLOW,"-",1],[ORANGE,"-",1],[],[]],\
                          [[],[],[ORANGE,"-",1],[YELLOW,"-",1],[GREEN,"-",1],[DARKGREEN,"-",1],[DARKRED,"-",1],[LIGHTBLACK,"-",1],[DARKRED,"-",1],\
                            [DARKGREEN,"-",1],[GREEN,"-",1],[YELLOW,"-",1],[ORANGE,"-",1],[],[]]]
    #color,powerup,lives
    #[["white","-",1]]
    print (data_lvlLayout)
    print ("\nLevel 1")
    print (data_level1)
    global screen
    screen=pygame.display.set_mode((960,700))
    global data_background
    data_background = pygame.Surface(screen.get_size())
    global data_actionground
    data_actionground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_actionground = data_actionground.convert_alpha()
    global data_foreground
    data_foreground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_foreground = data_foreground.convert_alpha()
    global data_buttonground
    data_buttonground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_buttonground = data_buttonground.convert_alpha()
    global data_textground
    data_textground = pygame.Surface(screen.get_size(),pygame.SRCALPHA,32)
    data_textground = data_textground.convert_alpha()
    data_background = data_background.convert()
    
def main():
    pygame.init()
    
# Convert Surface object to make blitting faster.
    
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
                data_mousePressedPos = pygame.mouse.get_pos()
                data_spriteGroup_buttons.update("d")
            elif event.type == pygame.MOUSEBUTTONUP:
                data_mousePressedPos = ()
                data_spriteGroup_buttons.update("u")
        text = "Bricks Alpha 0.2 {" + "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime) + "}"
        pygame.display.set_caption(text)
        data_actionground.fill((0,0,0,0))
        drawGame()
    #hersey burada olmali
        screen.blit(data_background,(0,0))
        screen.blit(data_actionground, (0,0))
        screen.blit(data_foreground,(0,0))
        screen.blit(data_buttonground, (0,0))
        screen.blit(data_textground, (0,0))
        pygame.display.flip()

# Finish Pygame.  
    pygame.quit()
    
main()
