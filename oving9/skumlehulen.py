from sys import stdin, stderr

# kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder nxn elementer
# (hvor n er antall noder)
# startrom er en liste med indeksene til nodene som tilsvarer startrommene.
# utganger er en liste med indeksene til nodene som tilsvarer utgangene.

def antallIsolerteStier(kapasiteter, startrom, utganger):
    kap = kapasitet(kapasiteter, startrom, utganger)
    n = len(kap)
    flow = [[0 for i in xrange(n)] for j in xrange(n)]
    
    numPaths = 0
    sti = finnFlytsti(0, n-1, flow, kap)
    while (sti != None):
        numPaths += 1
        for i in xrange(len(sti) - 1):
            flow[sti[i+1]][sti[i]] -= 1
            flow[sti[i]][sti[i+1]] += 1
        sti = finnFlytsti(0, n-1, flow, kap)
    
    return numPaths



def kapasitet(kapasiteter, startrom, utganger):
    n = 2 * len(kapasiteter) + 2
    nykapasitet = [[0 for i in xrange(n)] for j in xrange(n)]
    n = len(kapasiteter)
    
    for i in startrom:
        nykapasitet[0][i * 2 + 1] = 1

    for i in xrange(n):
        nykapasitet[2 * i + 1][2 * i + 2] = 1

    for i in xrange(n):
        for j in xrange(n):
            nykapasitet[2 * i + 2][2 * j + 1] = kapasiteter[i][j]

    n = 2 * len(kapasiteter) + 2
    for i in utganger:
        nykapasitet[2 * i + 2][n - 1] = 1

    return nykapasitet

    
    



# Finner en sti fra noden med indeks 'kilde' til noden med indeks 'sluk'
# med ledig kapasitet i et flytnettverk med flyt F og kapasitet C.
# Returnerer en liste hvor foerste element er indeksen til en av startnodene,
# siste element er indeksen til en av utgangene, og elementene imellom er
# indeksene til de andre nodene paa veien som ble funnet, i riktig rekkefoelge.
# Eksempel: en sti fra startnoden 4 til node 3, node 9, node 7 og til slutt til
# utgangen 12 vil representeres som [4, 3, 9, 7, 12].

def finnFlytsti(kilde, sluk, F, C):
    n = len(F)
    oppdaget = [False] * n
    forelder = [None] * len(F)
    koe = [kilde]
    while koe:
        node = koe.pop()
        if node == sluk:
            # Har funnet sluken, lager en array med passerte noder
            sti = []
            i = node
            while True:
                sti.append(i)
                if i == kilde:
                    break
                i = forelder[i]
            sti.reverse()
            return sti
        for nabo in range(n):
            if not oppdaget[nabo] and F[node][nabo] < C[node][nabo]:
                koe.append(nabo)
                oppdaget[nabo] = True
                forelder[nabo] = node
    return None


def main():
    noder, _, _ = [int(x) for x in stdin.readline().split()]
    startrom = [int(x) for x in stdin.readline().split()]
    utganger = [int(x) for x in stdin.readline().split()]
    nabomatrise = []
    for linje in stdin:
        naborad = [int(nabo) for nabo in linje.split()]
        nabomatrise.append(naborad)

    print(antallIsolerteStier(nabomatrise, startrom, utganger))

main()
