from sys import stdin

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def posisjoner(ord, indeks, node):
    poses = []
    while (ord[indeks] != '?'):
        if (ord[indeks] in node.barn):
            node = node.barn[ord[indeks]]
            indeks += 1
            if (indeks == len(ord)):
                return node.posi
        else:
            return []

    if (indeks + 1 == len(ord)):
        for letter in node.barn.keys():
            poses += node.barn[letter].posi
    else:
        for letter in node.barn.keys():
            poses += posisjoner(ord, indeks + 1, node.barn[letter])
    
    return poses

def main():
    built = False
    ord = stdin.readline().split()
    words = {}
    pos = 0
    for o in ord:
        if (o in words):
            words[o].append(pos)
        else:
            words[o] = [pos]
        pos += len(o) + 1

    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ':',
        if (sokeord in words):
            posi = words[sokeord]
        else:
            if not built:
                built = True
                toppnode = Node()
                for word in words.keys():
                    node = toppnode
                    for c in word:
                        if not (c in node.barn.keys()):
                            node.barn[c] = Node()
                        node = node.barn[c]
                    node.posi += words[word]
            posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print

main()
