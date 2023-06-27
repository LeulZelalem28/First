import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0.0
angle2 = 0.0
angle3 = 0.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

def display():
    global angle, angle2, angle3
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)
    glColor3f(1.0, 1.0, 0.0)
    glutSolidSphere(1.0, 30, 30)
    glRotatef(angle, 0.0, 15, 0.0)
    glTranslatef(4, 0.0, 0.0)
    glColor3f(0, 0, 1)
    glutSolidSphere(0.5, 20, 20)
    glRotatef(angle2, 0.0, 1.0, 0.0)
    glTranslatef(0.7, 0.0, 0.0)
    glColor3f(1, 1, 1)
    glutSolidSphere(0.2, 10, 10)
    glLoadIdentity()
    angle += 0.05
    angle2 += 1
    angle3 += 0.3
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow("Solar System")
glutDisplayFunc(display)
glutIdleFunc(display)
init()
glutMainLoop()