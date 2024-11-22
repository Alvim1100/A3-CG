import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import *
from model import *
from LoadMesh import ChairMesh
import random
import os


os.environ["SDL_VIDEO_CENTERED"]='1'
pg.init()

FPS = 60
clock = pg.time.Clock()
screen = (1600, 900)
display = pg.display.set_mode(screen, DOUBLEBUF|OPENGL)

def initialise():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    # projection
    glMatrixMode(GL_PROJECTION)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluPerspective(60, (screen[0]/screen[1]), 0.1, 100.0)
    glTranslate(0, 5, -12)



def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(0, 0, 0, 0)
    glPushMatrix()
    glPopMatrix()

def random_color():
    x = random.randint(0, 255) / 255
    y = random.randint(0, 255) / 255
    z = random.randint(0, 255) / 255
    color = (x, y, z)
    return color

colors_list= []

for n in range(len(chair_faces_vector4)):
    colors_list.append(random_color())

running = True
initialise()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    display()
    ChairMesh()
    pg.display.flip()
    pg.time.wait(100)
