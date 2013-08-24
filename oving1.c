#include <stdio.h>


struct kubbe
{
    int vekt;
    struct kubbe *neste;
};

int main()
{
    struct kubbe *forste;
    struct kubbe *siste;
    struct kubbe *forrige_siste;
    int i;

    while ((scanf("%d", &i)) != EOF)
    {
        forrige_siste = siste;
        siste = (struct kubbe*)malloc(sizeof(struct kubbe));
        siste->vekt = i;
        if (forste == NULL)
            forste = siste;
        else
            forrige_siste->neste = siste;
    }
    printf("%d\n", spor(forste));
}

int spor(struct kubbe *k)
{
    int tyngst = k->vekt;
    while(k->neste != NULL)
    {
        if (k->vekt > tyngst)
            tyngst = k->vekt;
        k = k->neste;
    }
    // funky and unneceseary code because the server insist the program
    // is a failure if the condition in the while loop is changed to
    // k != 0
    if (k->vekt > tyngst)
        tyngst = k->vekt;
    return(tyngst);
}
