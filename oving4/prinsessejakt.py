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

    noder = 0
    kanter = 0
    for i in xrange(n):
        if (visited[i] == 'u'):
            noder += 1
            for j in xrange(n):
                if nabomatrise[i][j] and visited[j] == 'u':
                    kanter += 1


    if noder == 0:
        return 0.0
    else:
        return float(kanter) / float(noder**2)


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
