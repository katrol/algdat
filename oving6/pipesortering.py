from sys import stdin
from random import randint

def sorter(A):
    rand_quicksort(A, 0, len(A) - 1)
    return A

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def rand_quicksort(A, p, r):
    if p < r:
        q = rand_partition(A, p, r)
        rand_quicksort(A, p, q - 1)
        rand_quicksort(A, q + 1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[r] = A[r], A[i + 1]
    
    return i + 1

def rand_partition(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def finn(A, nedre, ovre):
    inedre = binarysearch(A, nedre, 0, len(A) - 1)
    if A[inedre] > nedre and inedre != 0:
        inedre -= 1

    iovre = binarysearch(A, ovre, 0, len(A) - 1)
    if A[iovre] < ovre and iovre != (len(A) - 1):
        iovre += 1

    return(A[inedre], A[iovre])

def binarysearch(A, target, mini, maxi):
    while (maxi >= mini):
        mid = (mini + maxi) / 2
        if (A[mid] < target):
            mini = mid + 1
        elif (A[mid] > target):
            maxi = mid - 1
        else:
            return mid

    return mid


def main():

    liste = []

    for x in stdin.readline().split():
        liste.append(int(x))

    sortert = sorter(liste)

    for linje in stdin:
        ord = linje.split()
        minst = int(ord[0])
        maks = int(ord[1])
        resultat = finn(sortert, minst, maks)
        print str(resultat[0]) + " " + str(resultat[1])

main()
