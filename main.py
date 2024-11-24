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
    glTranslate(0, -1, -12)

    # Ativar iluminação
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Habilitar uma fonte de luz
    glEnable(GL_DEPTH_TEST)  # Ativar teste de profundidade
    #glEnable(GL_NORMALIZE)

    # Configuração da luz
    light_position = [5.0, 0.0, 10.0, 1.0]
    light_diffuse = [1.0, 1.0, 1.0, 1.0]
    light_ambient = [0.3, 0.3, 0.3, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)


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
    #glRotatef(2, 3, -10, -0)

    keys = pg.key.get_pressed()
    if keys[K_a]:
        glRotatef(-2, 0, 2, 0)
    if keys[K_d]:
        glRotatef(2, 0, 2, 0)
    if keys[K_w]:
        glRotatef(-2, 2, 0, 0)
    if keys[K_s]:
        glRotatef(2, 2, 0, 0)

    display()
    ChairMesh()
    pg.display.flip()
    pg.time.wait(100)
