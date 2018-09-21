#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
 
int 
main()
{
  const int SIZE = 1024;
  const char *id = "BarkCoefficient";

  int shm_fd;
  void *ptr;

  shm_fd = shm_open(id, O_RDONLY, 0600);
  ptr = mmap(0, SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);

  if (ptr)
    printf("%s\n", (char *) ptr);

  shm_unlink(id);

  return 0;
}
