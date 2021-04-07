#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#define ARR_SIZE(arr) ( sizeof((arr)) / sizeof((arr[0])) )

int isNumeric (const char * s)
{
    if (s == NULL || *s == '\0' || isspace(*s))
      return 0;
    char * p;
    strtod (s, &p);
    return *p == '\0';
}


int main(int argc, char** argv)
{   
    int num_words = 3;
    
    if(argc>2)
    {
        printf("Too many arguments");
    }
    if(argc == 2)
    {
        if(isNumeric(argv[1]))
        {
            num_words = atoi(argv[1]);
        }
        else
        {
            printf("Invalid argument");
        }
    }
    struct timespec tstart={0,0};
	clock_gettime(CLOCK_MONOTONIC, &tstart);
	
    srand(tstart.tv_nsec);
    char upper[] = "ABCDEFGHIJKLMNPQRSTUVWXYZ";
    char digits[] = "0123456789";
    char words[$num_words][$max_len] = {$words};
    for (int i =0;i<num_words-1;i++)
    {
        printf("%s.", words[rand() % ARR_SIZE(words)]);
    }
    printf("%s%c%c", words[rand() % ARR_SIZE(words)], upper[rand() % (ARR_SIZE(upper)-1)], digits[rand() % (ARR_SIZE(digits)-1)]);
    return 0;
}
