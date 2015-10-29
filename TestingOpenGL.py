from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



window = 0                                             # glut window number
width, height = 500, 400                               # window size
i = 0

X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
 
DIRECTION = 1


def draw_cube(l, width, height):
    global X_AXIS,Y_AXIS,Z_AXIS
    global DIRECTION
    
    glLoadIdentity()
    glTranslatef(0.0,0.0,-6.0)
    
    glRotatef(X_AXIS,1.0,0.0,0.0)
    glRotatef(Y_AXIS,0.0,1.0,0.0)
    glRotatef(Z_AXIS,0.0,0.0,1.0)    
    
    
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,0.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0) 
    
    glColor3f(1.0,0.0,0.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0) 
 
    glColor3f(0.0,1.0,0.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
 
    glColor3f(1.0,1.0,0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)
 
    glColor3f(0.0,0.0,1.0)
    glVertex3f(-1.0, 1.0, 1.0) 
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0) 
    glVertex3f(-1.0,-1.0, 1.0) 
 
    glColor3f(1.0,0.0,1.0)
    glVertex3f( 1.0, 1.0,-1.0) 
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)

    glEnd()    
    
    
    #glBegin(GL_QUADS)                                  # start drawing a rectangle
    #glVertex2f(x, y)                                   # bottom left point
    #glVertex2f(x + width, y)                           # bottom right point
    #glVertex2f(x + width, y + height)                  # top right point
    #glVertex2f(x, y + height)                          # top left point
    #glEnd()                                            # done drawing a rectangle

def mouseClicks(button, state, x, y):
    print (str(x) + " " + str(y) + " " + str(button))

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    global i
    
    #refresh2d(width, height)
    
    glColor3f((1.0 * i/40) % 1.0, (1.0 * i/60) % 1.0, (1.0 * i/100) % 1.0)      
    draw_cube(20, 200, 100)
    i = i + 1
   
    glutSwapBuffers()                                  # important for double buffering
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b"New Things!")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMouseFunc(mouseClicks)                             # set 
glutMainLoop()                                         # start everything