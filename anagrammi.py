import copy

from anyio.functools import lru_cache


def anagrammi(parola):
    soluzioni = set()
    ricorsione([], parola, soluzioni)
    return soluzioni

def ricorsione(parziale: list, rimanenti: str, soluzioni:set):
    #terminale

    if len(rimanenti) == 0:
        stringa = "".join(parziale)
        soluzioni.add(copy.deepcopy(stringa))
    #ricorsivo
    else:
        for i in range(len(rimanenti)):
            parziale.append(rimanenti[i])
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione(parziale, nuovi_rimanenti, soluzioni)
            parziale.pop()




if __name__ == "__main__":
    parola = "casa"
    res = list(anagrammi(parola))
    res.sort()
    print(res)
    print(len(res))
