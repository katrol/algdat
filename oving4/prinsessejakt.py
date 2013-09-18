from sys import *
import traceback

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    visited = ['u' for i in xrange(n)]
    visited[startnode] = 'v'
    stack = [startnode]
    while (stack != []):
        goback = True
        for i in xrange(n):
            if (nabomatrise[stack[len(stack) - 1]][i] and (visited[i] == 'u')):
                goback = False
                stack.append(i)
                visited[i] = 'v'
                break
        
        if (goback):
            visited[stack.pop()] = 'd'

    noder = []
    kanter = 0
    for i in xrange(len(visited) - 1):
        if (visited[i] == 'u'):
            noder.append(i)
        
    for node in noder:
        for i in xrange(n):
            if (nabomatrise[node][i] and (i in noder)):
                kanter += 1
    

    if len(noder) == 0:
        return 0.0
    else:
        return float(kanter) / float((len(noder))**2)


def main():
    n = int(stdin.readline())
    nabomatrise = [None] * n #rader

    for i in xrange(0, n):
        nabomatrise[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in xrange(0, n):
            nabomatrise[i][j] = (linje[j] == '1')

    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)

main()
