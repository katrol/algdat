from sys import stdin

def main():
    tull = stdin.readline()
    tull = stdin.readline()
    nodes = {}
    start_node = int(stdin.readline())
    node = int(stdin.readline())
    d = 0
    for linje in stdin:
        if (node == start_node):
            break
        tall = linje.split()
        if (node in tall[1:]):
            node = tall[0]
            d += 1
        else:
            for barn_nr in tall[1:]:
                nodes[int(barn_nr)] = int(tall[0])
    while (node != start_node):
        node = nodes[node]
        d += 1

    print(d)

main()
