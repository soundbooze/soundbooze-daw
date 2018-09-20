#include <stdio.h> 
#include <stdlib.h> 
  
int 
min(int a, int b) {
    if (a > b)
        return b;
    return a;
}

int 
main(int argc, char *argv[]) 
{ 
  int i, j;
  int count;
  int r = 3, c = 4;

  double **array = (double **) malloc(r * sizeof(double *)); 

  for (i = 0; i < r; i++) 
    array[i] = (double *) malloc(c * sizeof(double)); 

  /*
  count = 0; 
  for (i = 0; i <  r; i++) 
    for (j = 0; j < c; j++) 
      arr[i][j] = ++count;

  for (i = 0; i <  r; i++) 
    for (j = 0; j < c; j++) 
      printf("%d ", arr[i][j]); 
  */

  for (i = 0; i < r; i++) 
    free(array[i]);

  free(array);

  return 0; 
} 
