#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <openssl/rand.h>

#define ARR_SIZE(arr) ( sizeof((arr)) / sizeof((arr[0])) )

int isNumeric (const char * s)
{
    if (s == NULL || *s == '\0' || isspace(*s))
      return 0;
    char * p;
    strtod (s, &p);
    return *p == '\0';
}

unsigned int rand_range(unsigned int max)
{
    unsigned int rand_index;
    RAND_bytes((unsigned char *)&rand_index, sizeof(rand_index));
    return rand_index % max;
}


int main(int argc, char** argv)
{   
    int num_words = 4;
    
    if(argc>2)
    {
        printf("Too many arguments");
        return 0;
    }
    if(argc == 2)
    {
        if(isNumeric(argv[1]))
        {
            num_words = atoi(argv[1]);
            if(num_words<1)
            {
                printf("Argument must be greater than or equal to 1");
            }
        }
        else
        {
            printf("Argument is not a integer");
            return 0;
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
        printf("%s.", words[rand_range(ARR_SIZE(words)-1)]);
    }
    printf("%s%c%c\n", words[rand_range(ARR_SIZE(words)-1)], upper[rand_range(ARR_SIZE(upper)-1)], digits[rand_range(ARR_SIZE(digits)-1)]);
    return 0;
}
