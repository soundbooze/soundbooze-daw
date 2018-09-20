#include <stdio.h>
#include <stdlib.h>

int
main(int argc, char *argv[])

  double *buffer_tmp;
  double **buffer_tmp2;

  buffer_tmp = (double *) malloc(sizeof(double));
  if (buffer_tmp == NULL) {
    perror("malloc():");
  }

  free(buffer_tmp);

  return 0;
}
