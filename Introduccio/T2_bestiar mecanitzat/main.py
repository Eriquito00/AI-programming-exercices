import random as rd

from classes.tanks.chimpanzini_bananini import ChimpanziniBananini
from classes.tanks.lirili_larila import LiriliLarila
from classes.tanks.tralalero_tralala import TralaleroTralala

def main():
    tancsChimpanzini = [ChimpanziniBananini(f"Tank {i+1}") for i in range(2)]
    tancsLirili = [LiriliLarila(f"Tank {i+1}") for i in range(2)]
    tancsTralalero = [TralaleroTralala(f"Tank {i+1}") for i in range(2)]

    pass

if __name__ == "__main__":
  main()