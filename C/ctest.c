#include <stdio.h>

#define  message_for(a, b)  \
   printf(#a " and " #b ": We love you!\n")

#define one 2


int main(void) {
   message_for(Carole, Debra);
   // int one = 0;
   printf("%d\n", one);
   #ifdef one
       // message_for(one, one);
       printf("one is defined ");
   #endif

   return 0;
}
