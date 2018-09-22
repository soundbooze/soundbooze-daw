import time
import numpy as np
import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

WIDTH = 800
HEIGHT = 600

def init2D(r,g,b):
    glClearColor(r,g,b,0.0)    
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0.0, WIDTH, 0.0, HEIGHT)

def display():

    #bark_coeff = np.fromstring(file.read(), dtype=float, sep=' ')

    glColor3f(0.9, 0.0, 0.0 )
    glBegin(GL_LINES)
    glVertex2i(WIDTH/2,HEIGHT/2)   
    glVertex2i(WIDTH/2,HEIGHT)
    glEnd()

    glFlush()
    glClear(GL_COLOR_BUFFER_BIT)

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (WIDTH, HEIGHT)
glutInitWindowPosition (100, 100)
glutCreateWindow ('debaptism')

init2D(0.0,0.0,0.0)
glutDisplayFunc(display)
glutMainLoop()
