/* cat /proc/asound/card0/stream0 | grep 'Rates:' | awk '{ print $2 }' */

#include <stdio.h>
#include <string.h> 
#include <regex.h>

#define bufSize 1024
 
int
getRates (char *buff) 
{
  regex_t regex;
  short int i = 0;
  int reti = regcomp(&regex, "Rates:", 0);
  if (reti) {
    return -1;      
  }

  reti = regexec(&regex, buff, 0, NULL, 0);
  if (!reti) {
    char *rate;
    rate = strtok(buff, " ");
    while (rate != NULL) {
      if (i % 2)
        printf("%s\n", rate);
      rate = strtok(NULL, " ");
      i++;
    }
  }

  else {
    return -1;
  }

  regfree(&regex);

  return 0;
}

int
openProc(char *filename)
{
  FILE* fp;
  char buf[bufSize];

  fp = fopen(filename, "r"); 
  if (fp == NULL) {
    return -1;
  }
 
  while (fgets(buf, sizeof(buf), fp) != NULL) {
    buf[strlen(buf) - 1] = '\0';
    getRates(buf);
  }

  fclose(fp);

  return 0;
}

int 
main(int argc, char *argv[])
{
  openProc("/proc/asound/card2/stream0");
  return 0;
}
