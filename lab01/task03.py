from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def drawPixels(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def DDA(x0, y0, x1, y1):
    x = x0
    y = y0

    if abs(x1 - x0) > abs(y1 - y0):
        len = abs((x1 - x0))
    else:
        len = abs((y1 - y0))

    dx = ((x1 - x0) / float(len))
    dy = ((y1 - y0) / float(len))
    for iterator in range(int(len)):
        x += dx
        y += dy
        drawPixels(x, y)


def DDADot(x0, y0, x1, y1):
    x = x0
    y = y0

    if abs(x1 - x0) > abs(y1 - y0):
        len = abs((x1 - x0))
    else:
        len = abs((y1 - y0))

    dx = ((x1 - x0) / float(len))
    dy = ((y1 - y0) / float(len))
    for p in range(int(len)):
        x += dx + 5
        # for creating Gap within the pixels along Y axis
        y += dy
        drawPixels(x, y)


def drawLetter():
    DDADot(100, 400, 400, 400)
    DDA(300, 400, 300, 100)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    # call the draw methods
    ##Task3--------------------

    drawLetter()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

