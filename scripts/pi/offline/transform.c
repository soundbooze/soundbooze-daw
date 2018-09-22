#include <stdio.h>

#define BAR 8 


/*
int []
tsToBar(void buff) {

  // durasi /   
  // tempo
  // ppq


}
*/

int
main (int argc, char *argv[])
{

  char scale[7] = {'c', 'd', 'e', 'f', 'g', 'a', 'b'};

  int  t1[BAR] = {1, 0, 0, 1, 0, 0, 1, 0};
  char m1[BAR] = {'a', ' ', ' ', 'c', ' ', ' ', 'b', ' '};
  char n1[BAR] = {'b', ' ', ' ', 'e', ' ', ' ', 'a', ' '};

  int  t2[BAR] = {1, 1, 0, 1, 0, 1, 1, 1};
  char m2[BAR] = {'e', 'c', ' ', 'a', ' ', 'f', 'b', 'f'};
  char n2[BAR] = {'d', 'd', ' ', 'e', ' ', 'g', 'b', 'e'};

  int i = 0;

  printf("\n");

  for (i = 0; i < BAR; i++) {
    printf("%c ", scale[i]);
  }

  printf("\n");
  printf("---------------------\n");

  for (i = 0; i < BAR; i++) {
    printf("%c %c %d\n", m1[i], n1[i], t1[i]);
  }

  printf("\n");

  for (i = 0; i < BAR; i++) {
    printf("%c %c %d\n", m2[i], n2[i], t2[i]);
  }

  printf("\n");
  printf("-- Transformed 1 --\n");

  for (i = 0; i < BAR; i++) {
    printf("%d %d %d\n", t1[i] && t2[i], t1[i] || t2[i], t1[i] ^ t2[i]);
  }

  printf("\n");
  printf("-- Transformed 2 --\n");

  for (i = 0; i < BAR; i++) {
    int and = t1[i] && t2[i];
    int or = t1[i] || t2[i];
    int xor = t1[i] ^ t2[i];
    printf("%d %d %d %d %d %d\n", t1[i] * and, t2[i] * and, t1[i] * or, t2[i] * or, t1[i] * xor, t2[i] * xor);
  }

  // reverse, split, shuffle /etc

  return 0;
}
