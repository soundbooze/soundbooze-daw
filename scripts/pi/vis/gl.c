// gcc c.c -o c -lGL -lglut -lGLU

#include <stdlib.h>
#include <GL/glut.h>

#define WIDTH   800
#define HEIGHT  600

pthread_t animate_thread;

void 
init2D(float r, float g, float b)
{
	glClearColor(r,g,b,0.0);  
	glMatrixMode (GL_PROJECTION);
	gluOrtho2D (0.0, 0.0, 0.0, 0.0);
}

void 
display(void)
{

  while (1) {

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glColor3f(1.0, 1.0, 0.0);
    glBegin(GL_POINTS);
      glVertex2f(-0.8, 0.8);
    glEnd();

    glColor3f(1.0, 0.0, 0.0);
    glBegin(GL_LINES);
      glVertex2f(0.0, a);
      glVertex2f(a,1.0);
      glVertex2f(a,0.0);
      glVertex2f(-a,-a);
    glEnd();

	  glFlush();

  }

}

void 
main(int argc,char *argv[])
{
	glutInit(&argc,argv);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize (WIDTH, HEIGHT);
	glutInitWindowPosition (100, 100);
	glutCreateWindow ("points and lines");
	init2D(0.0,0.0,0.0);
	glutDisplayFunc(display);
	glutMainLoop();
}
