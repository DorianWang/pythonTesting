from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import os
import threading
import math
 
ESCAPE = b'\x1b'
 
window = 0
 
#rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

x = 0

DIRECTION = 1


 
def InitGL(Width, Height): 
 
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0) 
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)   
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width)/float(Height), 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)

def keyPressed(*args):
        print (args[0])
        if args[0] == ESCAPE:
                sys.exit()

 
def DrawGLScene():
        global X_AXIS,Y_AXIS,Z_AXIS
        global x
        global DIRECTION
 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
        glLoadIdentity()
        glTranslatef(X_AXIS,0.0,Z_AXIS-6.0)
 
        glRotatef(X_AXIS,0.1,0.0,0.0)
        #glRotatef(Y_AXIS,0.0,0.01,0.0)
        #glRotatef(Z_AXIS,0.0,0.0,0.01)
 
        # Attempt a square based pyramid
        glBegin(GL_TRIANGLES)
        
        glColor3f(0.1, 0.2, 0.3)
        glVertex3f(0, 0, 2)
        glVertex3f(1, 0, 0)
        glVertex3f(0, 1, 0)
        
        
        
        
        glEnd()
        
        glBegin(GL_TRIANGLE_STRIP);	
        
        glColor3f(0.1, 0.6, 0.2)
        
        glVertex3f( 0.0, 0.0, 0.0 ); #vertex 1
        glVertex3f( 0.0, 1.0, 0.0 ); #vertex 2
        glVertex3f( 1.0, 0.0, 0.0 ); #vertex 3
        glVertex3f( 1.5, 1.0, 0.0 ); #vertex 4
        
        glColor3f(0.1, 0.2, 0.7)
        
        glVertex3f( 2.0, 0.0, 0.0 ); #vertex 5
        glVertex3f( 2.0, 1.0, 0.0 ); #vertex 6
        
        glColor3f(0.9, 0.3, 0.1)
        
        glVertex3f( 2.5, 0.0, 0.0 ); #vertex 7
        glVertex3f( 2.5, 1.0, 4.0 ); #vertex 8
        
        glEnd();        
 
        # Draw Cube (multiple quads)
        #glBegin(GL_QUADS)
 
        #glColor3f(0.0,1.0,0.0)
        #glVertex3f( 1.0, 1.0,-1.0)
        #glVertex3f(-1.0, 1.0,-1.0)
        #glVertex3f(-1.0, 1.0, 1.0)
        #glVertex3f( 1.0, 1.0, 1.0) 
 
        #glColor3f(1.0,0.0,0.0)
        #glVertex3f( 1.0,-1.0, 1.0)
        #glVertex3f(-1.0,-1.0, 1.0)
        #glVertex3f(-1.0,-1.0,-1.0)
        #glVertex3f( 1.0,-1.0,-1.0) 
 
        #glColor3f(0.0,1.0,0.0)
        #glVertex3f( 1.0, 1.0, 1.0)
        #glVertex3f(-1.0, 1.0, 1.0)
        #glVertex3f(-1.0,-1.0, 1.0)
        #glVertex3f( 1.0,-1.0, 1.0)
 
        #glColor3f(1.0,1.0,0.0)
        #glVertex3f( 1.0,-1.0,-1.0)
        #glVertex3f(-1.0,-1.0,-1.0)
        #glVertex3f(-1.0, 1.0,-1.0)
        #glVertex3f( 1.0, 1.0,-1.0)
 
        #glColor3f(0.0,0.0,1.0)
        #glVertex3f(-1.0, 1.0, 1.0) 
        #glVertex3f(-1.0, 1.0,-1.0)
        #glVertex3f(-1.0,-1.0,-1.0) 
        #glVertex3f(-1.0,-1.0, 1.0) 
 
        #glColor3f(1.0,0.0,1.0)
        #glVertex3f( 1.0, 1.0,-1.0) 
        #glVertex3f( 1.0, 1.0, 1.0)
        #glVertex3f( 1.0,-1.0, 1.0)
        #glVertex3f( 1.0,-1.0,-1.0)

        #glEnd()
 
 
        X_AXIS = X_AXIS - 0.002
        Z_AXIS = math.sin(x) #Z_AXIS - 0.04
        
        x = x + 0.001
        
        if (x > 40 * 3.1415):
                x = 0
        
        glutSwapBuffers()




 
def main():
 
        global window
 
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640,480)
        glutInitWindowPosition(200,200)
        
        window = glutCreateWindow(b'OpenGL Python Cube')
 
        glutDisplayFunc(DrawGLScene)
        glutIdleFunc(DrawGLScene)
        glutKeyboardFunc(keyPressed)
        InitGL(640, 480)
        glutMainLoop()
 
if __name__ == "__main__":
        main() 












