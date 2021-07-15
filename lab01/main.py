import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

ranXarr = []
ranYarr = []
for i in range(50):
    ranXarr.append(random.randrange(0,600,1))
    ranYarr.append(random.randrange(0,600,1))


def draw_points(x, y):
    glPointSize(1) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def drawPixels50Random():
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(50):
        x =  ranXarr[i]
        y =  ranYarr[i]
        glVertex2f(x,y)
    glEnd()



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    for i in range(50):
        x = random.randint(10,400)
        y = random.randint(10,400)
        #print(i)
        #draw_points(x,y)
        drawPixels50Random()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()

