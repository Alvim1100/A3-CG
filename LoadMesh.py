from model import *
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy import cross
from numpy.linalg import norm

# Função para calcular normais de uma face
def calculate_normal(v1, v2, v3):
    u = [v2[i] - v1[i] for i in range(3)]
    v = [v3[i] - v1[i] for i in range(3)]
    normal = cross(u, v)
    magnitude = norm(normal)
    if magnitude == 0:
        return [0, 0, 0]
    return [normal[i] / magnitude for i in range(3)]

def ChairMesh():
    material_diffuse = [0.3, 0.3, 0.3, 1.0]  # Cor difusa (cinza escuro)
    material_ambient = [0.4, 0.4, 0.4, 1.0]  # Cor ambiente mais forte
    material_specular = [1.0, 1.0, 1.0, 1.0]  # Reflexo especular
    material_shininess = 32.0  # Brilho moderado

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
            glColor3fv(colors[x])  # Define a cor do vértice
            glVertex3fv(chair_verticies_vector3[vertex])
    glEnd()


#comentei as linhas para tentar deixar o modelo mais bonito
    # Desenhar as arestas (wireframe)
    #glBegin(GL_LINES)
    #for edge in chair_edges_vector2:
        #for vertex in edge:
            #glVertex3fv(chair_verticies_vector3[vertex])
    #glEnd()
