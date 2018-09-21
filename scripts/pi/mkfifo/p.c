#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
 
int main()
{
  const int SIZE = sizeof(double) * 26;
  const char *id = "BarkCoefficient";

  double bc[26] = {0};

  int i = 0;
  for (i = 0; i < 26; i++)
    bc[i] = i * 0.39;

  int shm_fd;
  void *ptr;

  shm_fd = shm_open(id, O_CREAT | O_RDWR, 0600);
  ftruncate(shm_fd, SIZE);
  ptr = mmap(0, SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);

  sprintf(ptr, "%.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f", bc[0], bc[1], bc[2], bc[3], bc[4], bc[5], bc[6], bc[7], bc[8], bc[9], bc[10], bc[10], bc[11], bc[12], bc[13], bc[14], bc[15], bc[16], bc[17], bc[18], bc[19], bc[20], bc[21], bc[22], bc[23], bc[24], bc[25], bc[26]);

  return 0;
}
