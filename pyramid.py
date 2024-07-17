import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),  # 0
    (1, -1, 1),   # 1
    (-1, -1, 1),  # 2
    (-1, -1, -1), # 3
    (0, 1, 0)     # 4 (top point)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4)
)

def draw_pyramid():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Set up perspective projection
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Get mouse movement
        mouse_x, mouse_y = pygame.mouse.get_rel()

        # Rotate the pyramid based on mouse movement
        glRotatef(mouse_y, 1, 0, 0)  # Rotate around x-axis
        glRotatef(mouse_x, 0, 1, 0)  # Rotate around y-axis
       

        # Clear buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the pyramid
        draw_pyramid()

        # Update display
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

