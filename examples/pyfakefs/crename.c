#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/stat.h>

/* Code to expose the OS X 10.12.5 bug discovered while testing pyfakefs */

int main () {
  system("rm -rf testingdir");
  mkdir("testingdir",S_IRWXU);  
  mkdir("testingdir/a",S_IRWXU);
  mkdir("testingdir/a/a",S_IRWXU);
  mkdir("testingdir/a/a/a",S_IRWXU);
  printf("BEFORE:\n");
  system("ls -lR testingdir");
  int res = rename("testingdir","testingdir/a/a/a");
  printf("res = %d, ERRNO = %d\n",res,errno);
  printf("AFTER:\n");
  system("ls -lR testingdir");  
}
