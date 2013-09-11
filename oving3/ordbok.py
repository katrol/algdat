from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    toppnode = Node()
    for entry in ordliste:
        node = toppnode
        word = entry[0]
        for c in word:
            if not (c in node.barn.keys()):
                node.barn[c] = Node()
            node = node.barn[c] 
        node.posi.append(entry[1])
    return toppnode

def posisjoner(ord, indeks, node):
    if (indeks == len(ord)):
        return node.posi
    elif ord[indeks] in node.barn:
        return posisjoner(ord, indeks + 1, node.barn[ord[indeks]])
    elif ord[indeks] == '?':
        poses = []
        for key in node.barn.keys():
            poses += (posisjoner(ord, indeks + 1, node.barn[key]))
        return poses
    else:
        return []

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append( (o,pos) )
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print sokeord + ':',
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print p,
            print
    except:
        traceback.print_exc(file=stderr)

main()
