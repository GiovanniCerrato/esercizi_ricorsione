import copy


class XExpansion:
    def __init__(self):
        self.soluzioni = []
        self.soluzioni_list = []

    def calcola_list(self, input):
        self.soluzioni_list = []
        self._ricorsione_list([], input)

    # parziale è la ricorsione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione_list(self, parziale: list, rimanenti: str):
        # caso terminale
        if len(rimanenti) == 0:

            self.soluzioni_list.append(copy.deepcopy(parziale))
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                for c in ["0","1"]:
                    parziale.append(c)
                    self._ricorsione_list(parziale, rimanenti[1:])
                    parziale.pop()
            else:
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])
                parziale.pop()  # <-- AGGIUNGI QUESTO!

    def calcola(self, input):
        self.soluzioni = []
        self._ricorsione("", input)


    #parziale è la ricorsione parziale
    #rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione(self, parziale: str, rimanenti: str):
        #caso terminale
        if len(rimanenti) == 0:
            self.soluzioni.append(parziale)
        #caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                self._ricorsione(parziale+'0', rimanenti[1:])
                self._ricorsione(parziale+'1', rimanenti[1:])
            else:
                self._ricorsione(parziale + rimanenti[0], rimanenti[1:])

def x_expansion2(input):
    soluzioni = []

    #parziale è la ricorsione parziale
    #rimanenti sono il resto dei caratteri da esaminare
    def ricorsione(parziale: str, rimanenti: str):
        #caso terminale
        if len(rimanenti) == 0:
            soluzioni.append(parziale)
        #caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                ricorsione(parziale+'0', rimanenti[1:])
                ricorsione(parziale+'1', rimanenti[1:])
            else:
                ricorsione(parziale + rimanenti[0], rimanenti[1:])
    ricorsione("", input)

    return soluzioni
if __name__ == "__main__":
    sequenza = "01X0X"
    xexp = XExpansion()
    xexp.calcola(sequenza)
    print(xexp.soluzioni)

    xexp.calcola_list(sequenza)
    print(xexp.soluzioni_list)

