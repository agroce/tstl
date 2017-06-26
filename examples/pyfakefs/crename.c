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
  /* This should fail with EINVAL (22) and do nothing. */
  int res = rename("testingdir","testingdir/a/a/a");
  /* But on OS X 10.12.5 at least, it returns EIO (5) and deletes testingdir/a/a/a! */
  printf("res = %d, ERRNO = %d\n",res,errno);
  printf("AFTER:\n");
  system("ls -lR testingdir");  
}
