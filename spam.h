#include <stdio.h>

static void order_spam(void)
{
    int tons = 1111;
    {
        printf("Ordered %i tons of spam! ", tons);
        printf("Ordered %i Kilos of spam!\n", tons);
    }
}