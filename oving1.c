#include <stdio.h>

int main()
{
    struct kubbe
    {
        int vekt;
        struct kubbe *neste;
    }

    struct kubbe *forste = NULL;
    struct kubbe *siste = NULL;
    struct kubbe *forrige_siste;
    int i;

    while ((i = (int) fgets()) != EOF)
    {
        forrige_siste = siste;
        *siste = (struct kubbe*)malloc(sizeof(struct kubbe));
        siste->vekt = i;
        if (*forste = NULL)
            forste = siste;
        else
            forrige_siste->neste = siste;
    }
    printf("%d", spor(forste));
}


int spor(struct kubbe k)
{
    int tyngst = k->vekt;
    while(kubbe)
    {
        if (k->vekt > tyngst)
            tyngst = k->vekt;
        k = k->next;
    }
    return(tyngst);
}

