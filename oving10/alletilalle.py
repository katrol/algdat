from sys import stdin, maxint

def korteste_rute(rekkefolge, nabomatrise, byer):
    for k in xrange(byer):
        for j in xrange(byer):
            for i in xrange(byer):
               nabomatrise[i][j] = min(nabomatrise[i][j], nabomatrise[i][k] + nabomatrise[k][j])

    n = 0
    for city in xrange(len(rekkefolge)):
        n += nabomatrise[rekkefolge[city]][rekkefolge[(city + 1) % byer]]
    if (n >= maxint / 3):
        return "umulig"
    else:
        return n

def main():
    testcases = int(stdin.readline())
    for test in xrange(testcases):
        byer = int(stdin.readline())
        rekkefolge = [int(by) for by in stdin.readline().split()]
        nabomatrise = []
        for by in xrange(byer):
            naborad = []
            for d in stdin.readline().split():
                d = int(d)
                if d == -1 : d = maxint / 3
                naborad.append(d)
            nabomatrise.append(naborad)
        print korteste_rute(rekkefolge, nabomatrise, byer)

main()
