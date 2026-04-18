class XExpansion:
    def __init__(self):
        self.soluzioni = []

    def calcola(self, input):
        self._ricorsione("", input)
        print(*(soluzione for soluzione in self.soluzioni))


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


if __name__ == "__main__":
    sequenza = "X01X0X01"
    xexp = XExpansion()
    xexp.calcola(sequenza)
