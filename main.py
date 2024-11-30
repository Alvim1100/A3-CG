import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from LoadMesh import ChairMesh
import os


os.environ["SDL_VIDEO_CENTERED"]='1'
pg.init()

FPS = 60
clock = pg.time.Clock()
screen = (1600, 900)
display = pg.display.set_mode(screen, DOUBLEBUF|OPENGL)

def initialise():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glMatrixMode(GL_PROJECTION)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluPerspective(60, (screen[0]/screen[1]), 0.1, 100.0)
    glTranslate(0, -1, -12)
    glRotated(90, -1, 0, 0)
    glTranslate(0, 10, 0)

    # Ativar iluminação
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

    # Configuração da luz
    light_position = [5.0, 0.0, 10.0, 1.0]
    light_diffuse = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(0, 0, 0, 0)
    glPushMatrix()
    glPopMatrix()

running = True
initialise()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[K_a]:
        glRotatef(-4, 0, 2, 0)
    if keys[K_d]:
        glRotatef(4, 0, 2, 0)
    if keys[K_w]:
        glRotatef(-4, 2, 0, 0)
    if keys[K_s]:
        glRotatef(4, 2, 0, 0)

    if keys[K_p]:
        glScale(1.5, 1.5, 1.5)
    if keys[K_l]:
        glScale(0.5, 0.5, 0.5)


    if keys[K_LEFT]:
        glTranslate(-2, 0, 0)
    if keys[K_RIGHT]:
        glTranslate(2, 0, 0)
    if keys[K_UP]:
        glTranslate(0, 2, 0)
    if keys[K_DOWN]:
        glTranslate(0, -2, 0)

    display()
    ChairMesh()
    pg.display.flip()
    pg.time.wait(100)
