from time import time

class NRegine():

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
    #===================================APPROCCIO 2 ===========================================
    #rappresentiamo soluzione come un vettore di N regine,
    #ognuno rappresentante una regina come riga e colonna
    def solve2(self, N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self._ricorsione2([], N)

    #parziale è un vettore di coppie (riga, colonna)
    def _ricorsione2(self, parziale, N):
        self.n_chiamate += 1

        #caso terminale: ho messo N regine
        if len(parziale) == N:
        #   if self._is_soluzione(parziale):
        #       print(parziale)
        #      self.n_soluzioni += 1
            self.n_soluzioni += 1
            print(parziale)

        #caso ricorsivo: ho messo < N regine
        else:
            for row in range(1,N+1):
                for col in range(1,N+1):
                    nuova_regina = [row,col]
                    #verifico che la nuova regina sia ammissibile
                    if self._step_is_valid(nuova_regina, parziale):
                        #aggiungi pezzetto di soluzione in parziale
                        parziale.append(nuova_regina)
                        #andare avanti con la ricorsione
                        self._ricorsione2(parziale, N)
                        #backtracking
                        parziale.pop()
    # Funzione che controlla se la nuova regina da inserire sia ammissibile rispetto alla soluzione parziale costruita finora.
    def _step_is_valid(self, nuova_regina, parziale) -> bool:
        for regina in parziale:
            if not self._is_pair_admissible(nuova_regina, regina):
                return False
        return True

    def _is_pair_admissible(self, regina1, regina2) -> bool:
        #1) verifico la riga. Se non va bene, return False
        if regina1[0] == regina2[0]:
            return False
        #2) verifico la colonna. Se non va bene, return False
        if regina1[1] == regina2[1]:
            return False
        #3) verifico la diagonale 1 (da alto a basso: col-row = cost). Se non va bene, return False
        if regina1[1]-regina1[0] == regina2[1]-regina2[0]:
            return False
        #4) verifico la diagonale 2 (da basso verso alto: col+row= const). Se non va bene, return False
        if regina1[0]+regina1[1] == regina2[0]+regina2[1]:
            return False
        #5) Ho passato tutti i controlli, return True
        return True


    def _is_soluzione(self, soluzione_possibile) -> bool:
        for i in range(len(soluzione_possibile)):
            for j in range(i+1, len(soluzione_possibile)):
                if not self._is_pair_admissible(soluzione_possibile[i], soluzione_possibile[j]):
                    return False
        return True




if __name__ == "__main__":
    nreg = NRegine()
    start_time = time()
    nreg.solve2(6)
    end_time = time()

    print(f"Elapsed time = {end_time - start_time}")
    print(f"Ho trovato {nreg.n_soluzioni} soluzioni ammisibili")
    print(f"Chiamate effettuate: {nreg.n_chiamate}")