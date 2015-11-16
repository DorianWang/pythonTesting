from OpenGL.GL import *
from OpenGL.GLU import *


import os
import threading
import math





def main():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0) 
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)   
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)    









































