from sys import stdin

def mst(nm):
    lengst = 0
    for i in prim(nm):
        if lengst < nm[i[0]][i[1]]:
            lengst = nm[i[0]][i[1]]

    return lengst

def prim(nm):
    Inf = float(1e3000)
    tre = []
    ubrukte = range(1, len(nm))
    noder = [[Inf, Inf] for i in xrange(len(nm))]
    forrige = 0

    while (ubrukte != []):
        for i in ubrukte:
            if nm[i][forrige] < noder[i][0]:
                noder[i][0] = nm[i][forrige]
                noder[i][1] = forrige


        kortest = Inf
        for i in ubrukte:
            if noder[i][0] < kortest:
                kortest = noder[i][0]
                kortestkant = noder[i][1]
                fra = i
        ubrukte.remove(fra)
        tre.append((fra, kortestkant))
        forrige = fra
    return tre


def main():
    Inf = float(1e3000)
    linjer = []
    for str in stdin:
        linjer.append(str)
    n = len(linjer)
    nabomatrise = [None] * n
    node = 0
    for linje in linjer:
        nabomatrise[node] = [Inf] * n
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            nabomatrise[node][nabo] = vekt
        node += 1
    print(mst(nabomatrise))


main()
