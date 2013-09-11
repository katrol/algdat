from sys import stdin
from collections import deque

class Node:
    barn = None
    ratatosk = None
    nesteBarn = None
    level = None

    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0
        self.level = 0

def dfs(rot):
    stack = [rot]
    d = 0
    node = rot
    while (stack != []):
        node = stack[len(stack) - 1]
        if (node.ratatosk == True): 
            return d
        if (len(node.barn) != node.nesteBarn):
            stack.append(node.barn[node.nesteBarn])
            node.nesteBarn += 1
            d += 1
        else:
            stack.pop()
            d -= 1
        

def bfs(rot):
    queue = deque()
    append(rot)
    node = rot
    while not(node.ratatosk):
        node = queue.popleft()
        for b in node.barn:
            b.level = node.level + 1
            queue.append(b)
    
    return node.level
        
def main():
    funksjon = stdin.readline().strip()
    antall_noder = int(stdin.readline())
    noder = []
    for i in xrange(antall_noder):
         noder.append(Node())
    start_node = noder[int(stdin.readline())]
    ratatosk_node = noder[int(stdin.readline())]
    ratatosk_node.ratatosk = True
    for linje in stdin:
        tall = linje.split()
        temp_node = noder[int(tall.pop(0))]
        for barn_nr in tall:
            temp_node.barn.append(noder[int(barn_nr)])

    if funksjon == 'velg':
        print bfs(start_node)
    elif funksjon == 'bfs':
        print bfs(start_node)
    elif funksjon == 'dfs':
        print dfs(start_node)

main()
