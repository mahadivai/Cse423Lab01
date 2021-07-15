import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *




def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_home():
    glBegin(GL_LINE_LOOP)
    glVertex2f(200,300)
    glVertex2f(300,400)
    glVertex2f(400,300)
    glVertex2f(400,100)
    glVertex2f(200,100)
    glEnd()

def draw_roof():
    glBegin(GL_LINES)
    glVertex2f(200,300)
    glVertex2f(400,300)
    glEnd()

def draw_window():
    glBegin(GL_LINE_LOOP)
    glVertex2f(240,260)
    glVertex2f(280,260)
    glVertex2f(280,220)
    glVertex2f(240,220)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(320,260)
    glVertex2f(360,260)
    glVertex2f(360,220)
    glVertex2f(320,220)
    glEnd()


def draw_door():
    glBegin(GL_LINE_LOOP)
    glVertex2f(280,180)
    glVertex2f(320,180)
    glVertex2f(320,100)
    glVertex2f(280,100)
    glEnd()

def draw_lock():
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(310,140)
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_home()
    draw_roof()
    draw_window()
    draw_door()
    draw_lock()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()

