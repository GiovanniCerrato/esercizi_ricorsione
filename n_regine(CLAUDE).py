from time import time


class NRegine():
    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0

    # ===================================APPROCCIO 2 (ORIGINALE) ===========================================
    def solve2(self, N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self._ricorsione2([], N)

    def _ricorsione2(self, parziale, N):
        self.n_chiamate += 1

        if len(parziale) == N:
            self.n_soluzioni += 1
            print(parziale)
        else:
            for row in range(1, N + 1):
                for col in range(1, N + 1):
                    nuova_regina = [row, col]
                    if self._step_is_valid(nuova_regina, parziale):
                        parziale.append(nuova_regina)
                        self._ricorsione2(parziale, N)
                        parziale.pop()

    def _step_is_valid(self, nuova_regina, parziale):
        for regina in parziale:
            if not self._is_pair_admissible(nuova_regina, regina):
                return False
        return True

    def _is_pair_admissible(self, regina1, regina2):
        if regina1[0] == regina2[0]:
            return False
        if regina1[1] == regina2[1]:
            return False
        if regina1[1] - regina1[0] == regina2[1] - regina2[0]:
            return False
        if regina1[0] + regina1[1] == regina2[0] + regina2[1]:
            return False
        return True

    # ===================================APPROCCIO 3 (OTTIMIZZATO) ===========================================
    def solve3(self, N):
        """Versione ottimizzata: una regina per colonna"""
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self._ricorsione3([], N)

    def _ricorsione3(self, parziale, N):
        """parziale[i] = riga della regina nella colonna i+1"""
        self.n_chiamate += 1

        col_corrente = len(parziale) + 1  # prossima colonna da riempire

        if len(parziale) == N:
            self.n_soluzioni += 1
            # Converti in formato [riga, col] per visualizzazione
            soluzione = [[parziale[i], i + 1] for i in range(N)]
            print(soluzione)
        else:
            # Prova ogni riga nella colonna corrente
            for row in range(1, N + 1):
                if self._step_is_valid3(row, col_corrente, parziale):
                    parziale.append(row)
                    self._ricorsione3(parziale, N)
                    parziale.pop()

    def _step_is_valid3(self, row, col, parziale):
        """Controlla se piazzare una regina a (row, col) è valido"""
        for prev_col_idx in range(len(parziale)):
            prev_row = parziale[prev_col_idx]
            prev_col = prev_col_idx + 1

            # Stessa riga
            if row == prev_row:
                return False

            # Diagonale
            if abs(row - prev_row) == abs(col - prev_col):
                return False

        return True


if __name__ == "__main__":
    N = 7 # Cambia questo per testare dimensioni diverse

    print(f"{'=' * 60}")
    print(f"CONFRONTO TRA APPROCCI PER N = {N}")
    print(f"{'=' * 60}\n")

    # Test Approccio 2 (originale)
    print(">>> APPROCCIO 2 (ORIGINALE) <<<")
    nreg2 = NRegine()
    start_time = time()
    nreg2.solve2(N)
    end_time = time()
    tempo2 = end_time - start_time
    print(f"\n⏱️  Tempo: {tempo2:.6f} secondi")
    print(f"✓  Soluzioni trovate: {nreg2.n_soluzioni}")
    print(f"📞 Chiamate ricorsive: {nreg2.n_chiamate:,}")

    print(f"\n{'-' * 60}\n")

    # Test Approccio 3 (ottimizzato)
    print(">>> APPROCCIO 3 (OTTIMIZZATO) <<<")
    nreg3 = NRegine()
    start_time = time()
    nreg3.solve3(N)
    end_time = time()
    tempo3 = end_time - start_time
    print(f"\n⏱️  Tempo: {tempo3:.6f} secondi")
    print(f"✓  Soluzioni trovate: {nreg3.n_soluzioni}")
    print(f"📞 Chiamate ricorsive: {nreg3.n_chiamate:,}")

    # Confronto finale
    print(f"\n{'=' * 60}")
    print("RISULTATI CONFRONTO:")
    print(f"{'=' * 60}")
    if tempo2 > 0:
        if tempo3 == 0:
            speedup = tempo2 / (tempo3+ 0.000001)
        else:
            speedup = tempo2 / tempo3
        print(f"🚀 Speedup: {speedup:.2f}x più veloce")
    if nreg2.n_chiamate > 0:
        riduzione = (1 - nreg3.n_chiamate / nreg2.n_chiamate) * 100
        print(f"📉 Riduzione chiamate: {riduzione:.1f}%")
    print(f"{'=' * 60}")