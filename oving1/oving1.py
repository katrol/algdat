from sys import stdin

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None

def spor(kubbe):
    tyngst = kubbe.vekt
    while (kubbe):
        if kubbe.vekt > tyngst:
            tyngst = kubbe.vekt
        kubbe = kubbe.neste
    return tyngst

# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

print spor(forste)
