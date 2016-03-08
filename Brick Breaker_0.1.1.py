# -*- coding: cp1254 -*-
#######################################################################
# name: Baha Okten
# andrewId: bokten
# hours: 30
######################################################################
# project.py

import random
import csv

from Tkinter import *

#Add Gravity
#Add xvelocity depends on where on the player it hits

#==================================####INTERACTIVE OBJECTS####==========================================#

class Balls(object):
    #Constructor
    def __init__(self,x,y,state,velX,velY,radius): #You always call self in python
        self.state = state
        self.velX = velX
        self.velY = velY
        self.r = radius
        self.x = x
        self.y = y

    def changeSpeedX(self,new_speed):
        self.velX = new_speed

    def changeSpeedY(self,new_speed):
        self.velY = new_speed

    def move(self):
        self.x += self.velX
        self.y += self.velY
        
#      Test
    def ola(self,z):
        print z
#     ======

    def __str__(self):
        return "Ball is" + self.x

    def info(self):
        return str(self.x), str(self.y), str(self.velX)

    def __hash__(self):
        return hash((self.col,self.row,self.special,self.color))

def test():
      b = Balls(1,1,"normal",1,1,1)
      b.ola(1)
      
###############-PADDLE-###############

class Paddle(object):
    #Constructor
    def __init__(self,x,y,state,size,velX): #You always call self in python
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

    def move(self,direction):
        if direction == "right":
            self.x += self.velX
        else:
            self.x -= self.velX

    def draw(self):
        tmp = self.x+self.add
        canvas.create_arc(self.x, self.y, self.x+35, self.y+20, outline="black", fill = "black",start = 90)
        canvas.create_arc(self.x, self.y, self.x+35, self.y+20, outline="white", style = "arc",start = 90)
        canvas.create_arc(self.x, self.y, self.x+35, self.y+20, outline="black", fill = "black",start = 180)
        canvas.create_arc(self.x, self.y, self.x+35, self.y+20, outline="white", style = "arc",start = 180)
        canvas.create_rectangle(self.x+18,self.y,tmp+80,self.y+20,fill = "black",width = 0)
        canvas.create_polygon(self.x+18,self.y+20,self.x+28,self.y,self.x+38,self.y+20,fill = "red",outline = "blue")
        canvas.create_polygon(tmp+80,self.y+20,tmp+70,self.y,tmp+60,self.y+20,fill = "red",outline = "blue")
        canvas.create_line(self.x+18,self.y,tmp+80,self.y,fill = "white",width = 2)
        canvas.create_line(self.x+18,self.y+20,tmp+80,self.y+20,fill = "white")
        canvas.create_arc(tmp+63, self.y, tmp+98, self.y+20, outline="black", fill = "black",start = 270)
        canvas.create_arc(tmp+63, self.y, tmp+98, self.y+20, outline="white", style = "arc",start = 270)
        canvas.create_arc(tmp+63, self.y, tmp+98, self.y+20, outline="black", fill = "black")
        canvas.create_arc(tmp+63, self.y, tmp+98, self.y+20, outline="white", style = "arc")
        

    def __str__(self):
        return "Ball is" + self.color

def direction():
    if canvas.data.left:
        canvas.data.paddleMotion = "left"
    if canvas.data.right:
        canvas.data.paddleMotion = "right"
    if not canvas.data.right and not canvas.data.left:
        canvas.data.paddleMotion = "-"

def test():
    canvas.data.paddle = Paddle(350,200,"-","medium",15)

#===================================####DRAW FUNCTIONS####==========================================#

def draw():
      tmp = canvas.data.state
      if tmp == "menu":
            drawMenu()
            direction()
            canvas.data.paddle.draw()
      elif tmp == "transition":
            drawMenu()
            drawTransitionAnimation(canvas.data.stateTemp)
      elif tmp == "levelSelect":
            drawLevelSelect()
            canvas.data.loop = True
            direction()
            canvas.data.paddle.draw()
         

def drawMenu():
      drawBackground()
      button1 = Button(canvas, text = "Start",command = drawTransitionAnimation, anchor = CENTER)
      button1.configure(width = 10, activebackground = "#532525", relief = RAISED,activeforeground = "green",bg = "#67CB74",bd = 5, font='Helvetica 10')
      button1_window = canvas.create_window(canvas.data.canvasWidth/2, canvas.data.canvasHeight/2, anchor=CENTER, window=button1)
      canvas.create_text(canvas.data.canvasWidth/2,50,text = "Bricks",font = "Times 60",anchor = CENTER)

def drawLevelSelect():
    canvas.create_rectangle(0,0,canvas.data.canvasWidth,canvas.data.canvasHeight, fill = "gray", width = 0)
    canvas.create_text(canvas.data.canvasWidth/2,50,text = "Level Select",font = "Times 30",anchor = CENTER, fill = "red")
    canvas.data.currentLevel = canvas.data.level1
    tmp = 50
    canvas.create_rectangle(tmp,tmp,tmp+13*15,tmp+5*26,fill = "#5a7495")
    drawLevel(13,5,False,tmp,tmp,1)
    canvas.create_rectangle(tmp,tmp,tmp+13*15,tmp+5*26)
    drawLevel(64,25)

def drawLevel(width = 0,height = 0,marginY = True,addX = 0,addY = 0,outline = 5):
    if width == 0:
        width = canvas.data.brickSizeX
    if height == 0:
        height = canvas.data.brickSizeY
    if marginY == True:
        marginY = canvas.data.brickYMargin
    else:
        marginY = 0
    level = canvas.data.currentLevel
    rows = len(level)
    cols = len(level[0])
    for row in xrange(rows):
        for col in xrange(cols):
            if len(level[row][col]) != 0:
                drawBrick(col,row,level[row][col][0],width,height,marginY,addX,addY,outline)

def drawBrick(col,row,cl,width,height,marginY,addX,addY,outline):
    #Col(x) max = 0-14
    #Row(y) max = 0-25
    if col >= 15 or row >= 26:
        return False
    else:
        canvas.create_rectangle(addX+col*width,addY+marginY+row*height,addX+(col+1)*width,addY+marginY+(row+1)*height,fill = cl,width = outline)

def drawTransitionAnimation(state1 = "levelSelect"):
    if canvas.data.temp == 25:
        canvas.data.state = state1
        canvas.data.loop = False
        canvas.data.temp = 1
        redrawAll()
    else:
        canvas.create_rectangle(0,0,40*canvas.data.temp,canvas.data.canvasHeight,fill= "green",outline = "green")
        canvas.data.state = "transition"
        canvas.data.stateTemp = state1
        canvas.data.temp += 1
        canvas.data.loop = True
      

   
def drawBackground():
      backColor = [154,52,53]
      curtainColor = [250,0,0]
      for n in xrange(18):
            c2 = '#%02x%02x%02x' % tuple(backColor)
            canvas.create_rectangle(n*30,n*20,canvas.data.canvasWidth-n*30,canvas.data.canvasHeight-n*20,fill = c2,outline = c2)
            backColor = [154-(n*2),52+(n*9),53+(n*8)]
      for num in xrange(19):
            c = '#%02x%02x%02x' % tuple(curtainColor)
            canvas.create_polygon((num*10),0,10+(num*10),0,0,450,fill = c)
            canvas.create_polygon(canvas.data.canvasWidth-(num*10),0,canvas.data.canvasWidth,450,canvas.data.canvasWidth-10-(num*10),0,fill = c)
            canvas.create_polygon((num*8),canvas.data.canvasHeight,10+(num*8),canvas.data.canvasHeight,0,450,fill = c)
            canvas.create_polygon(canvas.data.canvasWidth-(num*8),canvas.data.canvasHeight,canvas.data.canvasWidth-10-(num*8),canvas.data.canvasHeight,canvas.data.canvasWidth,450,fill = c)
            if not curtainColor[0] < 20+num:
                  curtainColor[0] -= 5+(num)
            curtainColor[1] += 20-(num)
            curtainColor[2] += abs(num-5)

    
#==================================####INPUTS AND HITBOXES####=========================================================================#

def mousePressed(event):
      mouseX = event.x
      mouseY = event.y

def keyPressed(event):
    if canvas.data.state[0] == "-" or 1 == 1:
        if event.keysym == "Right":
            canvas.data.right = True
        elif event.keysym == "Left":
            canvas.data.left = True

def keyReleased(event):
    if canvas.data.state[0] == "-" or 1 == 1:
        if event.keysym == "Right":
            canvas.data.right = False
        elif event.keysym == "Left":
            canvas.data.left = False

#================================####INITIAL CALLS####================================================================================#

def timerFired():
    if canvas.data.paddle != []:
        if canvas.data.paddleMotion == "right":
            canvas.data.paddle.move("right")
        elif canvas.data.paddleMotion == "left":
            canvas.data.paddle.move("left")
    if canvas.data.loop == True:
        redrawAll()
    canvas.after(canvas.data.delay, timerFired)

def redrawAll():
    canvas.delete(ALL)
    draw()

def init():
      canvas.delete(ALL)
      canvas.data.delay = 12
      canvas.data.state = "menu"
      #---TRANSITION---#
      canvas.data.loop = False
      canvas.data.stateTemp = ""
      canvas.data.temp = 1
      #---BRICKS---#
      canvas.data.brickSizeX = 64
      canvas.data.brickSizeY = 25
      canvas.data.brickSizeXSelect = 13
      canvas.data.brickSizeYSelect = 5
      canvas.data.brickYMargin = 10
      #---PADDLE---#
      canvas.data.paddle = []
      canvas.data.paddleY = 300
      canvas.data.paddleMotion = "-"
      #---INPUT---#
      canvas.data.left = False
      canvas.data.right = False
      #---LEVEL---#
      canvas.data.currentLevel = []
      canvas.data.lvlLayout   =   [[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]], [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                                  [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                                  [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                                  [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                                  [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                                  [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                                  [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] , [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]

      canvas.data.level1      =   [[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],\
                                   [[],[],["orange","-",1],["yellow","-",1],["green","-",1],["darkgreen","-",1],["darkred","-",1],["black","-",1],["darkred","-",1],\
                                    ["darkgreen","-",1],["green","-",1],["yellow","-",1],["orange","-",1],[],[]],\
                                   [[],[],["orange","-",1],["yellow","-",1],["green","-",1],["darkgreen","-",1],["darkred","-",1],["black","-",1],["darkred","-",1],\
                                    ["darkgreen","-",1],["green","-",1],["yellow","-",1],["orange","-",1],[],[]]]

      #color,powerup,lives
      #[["white","-",1]]
      print canvas.data.lvlLayout
      print canvas.data.level1
      test()
      draw()


def run():
    #Issues screen size, layout, and basic information[Only called at the beginning]
    # create the root and the canvas
    global canvas
    root = Tk()
    root.wm_title("Bricks Alpha 0.1")
    canvasWidth = 960
    canvasHeight = 700
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)  # makes window non-resizable
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.canvasWidth = canvasWidth
    canvas.data.canvasHeight = canvasHeight
    root.bind("<Button-1>", mousePressed)
    test()
    init()
    # set up events
    root.bind("<Key>", keyPressed)
    root.bind("<KeyRelease>", keyReleased)
    #root.bind("<Enter>", mouseEntered)
    #root.bind("<Leave>",mouseLeft)
    # and launch the app
    timerFired()
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()


