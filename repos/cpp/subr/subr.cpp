#include <sys/ioctl.h>
#include <stdio.h>
#include <unistd.h>
#include <iostream>
using namespace std;
int main (int argc, char **argv)
{
	//[screen_size]
    //struct winsize w;
    //ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
    //printf ("lines %d\n", w.ws_row);
    //printf ("columns %d\n", w.ws_col);
	//x = _getch();
	//printf(x)
	while (true)
	{
    	if('n' == getchar())
			printf("work");
			break;
	}
    return 0;  // make sure your main returns int
}

