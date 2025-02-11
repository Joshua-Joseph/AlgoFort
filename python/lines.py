import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)


def plot_line():
    print(' What do you want to do? ')
    print('1. Draw a horizontal line')
    print('2. Draw a vertical line')
    print('3. Draw a diagonal line')
    ch = int(input('Enter your choice: '))
    if (ch==1):
        x1 = int(input('Enter the initial x coordinate: '))
        x2 = int(input('Enter the final x coordinate: '))
        y1 = int(input('Enter the y coordinate: '))
        y2 = y1
        x1 = x1/100
        x2 = x2/100
        y1 = y1/100
        y2 = y2/100

    elif (ch==2):
        x1 = int(input('Enter the x coordinate: '))
        x2 = x1
        y1 = int(input('Enter the initial y coordinate: '))
        y2 = int(input('Enter the final y coordinate: '))
        x1 = x1/100
        x2 = x2/100
        y1 = y1/100
        y2 = y2/100

    elif (ch==3):
        x1 = int(input('Enter the initial x coordinate: '))
        x2 = int(input('Enter the final x coordinate: '))
        y1 = x1
        y2 = x2
        x1 = x1/100
        x2 = x2/100
        y1 = y1/100
        y2 = y2/100
    
    else:
        print('Invalid Choice')

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glPointSize(5.0)

    glBegin(GL_LINES)
    # Y_Axis
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    # X_Axis
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glEnd()
    # line
    glColor3f(1.0,0.0,0.0)

    glBegin(GL_LINES)        

    glVertex2f(x1, y1)
    glVertex2f(x2, y2)         
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("Line")
glutInitWindowSize(100, 100)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot_line)
clearScreen()
glutMainLoop()