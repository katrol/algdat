from sys import stdin, stderr

def beste_sti(nm, sans):
    n = len(sans)
    parents = [-30000] * n
    results = [0.0] * n
    results[0] = sans[0]
    done = [False] * n
    neste = 0
    for i in range(n):
        valgt = neste
        done[valgt] = True
        best = -1
        for j in range(n):
            if not done[j]:
                if (nm[valgt][j]):
                    if results[valgt] * sans[j] > results[j]:
                        results[j] = sans[j] * results[valgt]
                        parents[j] = valgt
                if results[j] > best:
                    best = results[j]
                    neste = j

    i = n - 1
    if results[i] == 0.0:
        return "0"
    path = [i]
    while (i != 0):
        i = parents[i]
        path.insert(0,i)
    strpath = '-'.join(str(x) for x in path)
    return strpath

def main():
    n = int(stdin.readline())
    sansynligheter = [float(x) for x in stdin.readline().split()]
    nabomatrise = []
    for linje in stdin:
        naborad = [0] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
    print(beste_sti(nabomatrise, sansynligheter))

main()
