#include <stdio.h>
#include <string.h>

int main()
{
    char line[1000];
    int nodes[10000];
    int start_node, node, n, i;
    char num[10], parent[10];
    scanf("%s", &line);
    scanf("%s", &line);
    scanf("%d", &start_node);
    scanf("%d", &node);
    while ((fgets(line, 100, stdin)) != NULL)
    {
        n = 0;
        while(line[n] != ' ' && line[n] != '\0')
        {
            parent[n] = line[n];
            n++;
        }
        parent[++n] = '\0';
        n--;
        while (line[n] != '\0')
        {
            i = 0;
            while (line[n] != ' ' && line[n] != '\0')
            {
                num[i] = line[n];
                i++;
                n++;
            }
            nodes[atoi(num)] = atoi(parent);
            n++;
        }
    }

    int d = 0;
    while (node != start_node)
    {
        node = nodes[node];
        d++;
    }
    printf("%d\n", d);
}
