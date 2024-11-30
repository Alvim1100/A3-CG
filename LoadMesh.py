from model import *
from OpenGL.GL import *
from numpy import cross
from numpy.linalg import norm


def calculate_normal(v1, v2, v3):
    u = [v2[i] - v1[i] for i in range(3)]
    v = [v3[i] - v1[i] for i in range(3)]
    normal = cross(u, v)
    magnitude = norm(normal)
    if magnitude == 0:
        return [0, 0, 0]
    return [normal[i] / magnitude for i in range(3)]

def ChairMesh():
    material_diffuse = [0.19125, 0.0735, 0.0225, 1.0]
    material_ambient = [0.4, 0.4, 0.4, 1.0]
    material_specular = [1.0, 1.0, 1.0, 1.0]
    material_shininess = 32.0
    material_emission = [0.1, 0.1, 0.1, 1.0]

    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, material_emission)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, material_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, material_shininess)

    # Desenhar as faces com iluminação
    glBegin(GL_QUADS)
    for face in chair_faces_vector4:
        # Calcular a normal da face
        v1 = chair_verticies_vector3[face[0]]
        v2 = chair_verticies_vector3[face[1]]
        v3 = chair_verticies_vector3[face[2]]
        normal = calculate_normal(v1, v2, v3)

        glNormal3fv(normal)  # Define a normal para a face

        x = 0
        for vertex in face:
            x += 1
            glVertex3fv(chair_verticies_vector3[vertex])
    glEnd()
