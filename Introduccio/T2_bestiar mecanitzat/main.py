import random as rd

from classes.tanks.tank import Tank
from classes.tanks.chimpanzini_bananini import ChimpanziniBananini
from classes.tanks.lirili_larila import LiriliLarila
from classes.tanks.tralalero_tralala import TralaleroTralala
from classes.projectils.projectil import Projectil


def obtenir_tancs_vius(tots_els_tancs: list[Tank]) -> list[Tank]:
    """Retorna els tancs vius

    Args:
        tots_els_tancs (list[Tank]): llista de tots els tancs

    Returns:
        list[Tank]: llista amb els tancs vius
    """
    return [t for t in tots_els_tancs if t.esta_viu()]


def obtenir_faccions_vives(tots_els_tancs: list[Tank]) -> set[str]:
    """Retorna les faccions vives

    Args:
        tots_els_tancs (list[Tank]): llista de tots els tancs

    Returns:
        set[str]: noms de les faccions vives
    """
    return set(t.faction for t in tots_els_tancs if t.esta_viu())

def creacio_tancs() -> list[Tank]:
    """Creacio de X tancs per cada faccio ordenats per ordre d'atac

    Returns:
        list[Tank]: llista amb els tancs ordenats per ordre d'atac
    """
    TANCS_PER_FACCIO = 2
    
    tancsChimpanzini = [ChimpanziniBananini(f"Chimpanzini {i+1}") for i in range(TANCS_PER_FACCIO)]
    tancsLirili = [LiriliLarila(f"Lirili {i+1}") for i in range(TANCS_PER_FACCIO)]
    tancsTralalero = [TralaleroTralala(f"Tralalero {i+1}") for i in range(TANCS_PER_FACCIO)]

    faccions = [tancsChimpanzini, tancsLirili, tancsTralalero]

    ordre_atacs = []
    for i in range(TANCS_PER_FACCIO):
        for faccio in faccions:
            ordre_atacs.append(faccio[i])

    return ordre_atacs

def main():
    ordre_atacs = creacio_tancs()
    tots_els_tancs = ordre_atacs.copy()

    idx_atacant = 0
    num_ronda = 1

    while len(obtenir_faccions_vives(tots_els_tancs)) > 1:
        # Si el tanc esta mort, busquem el següent tanc viu per atacar
        while not ordre_atacs[idx_atacant].esta_viu():
            idx_atacant = (idx_atacant + 1) % len(ordre_atacs)

        # Seleccionem l'atacant, l'objectiu i projectil a utilitzar
        atacant: Tank = ordre_atacs[idx_atacant]
        idx_atacant = (idx_atacant + 1) % len(ordre_atacs)

        objectius_possibles = [
            t for t in obtenir_tancs_vius(tots_els_tancs) 
            if t.faction != atacant.faction
        ]
        objectiu: Tank = rd.choice(objectius_possibles)

        projectil: Projectil = atacant.seguent_projectil()

        # Inici de la ronda amb la informació de l'atacant, objectiu i projectil
        print(f"--- RONDA {num_ronda} ---")
        print(
            f"> El [{atacant.name}] de la facció [{atacant.faction}] es disposa a atacar "
            f"amb el projectil de tipus [{projectil.name}] al [{objectiu.name}] de la facció [{objectiu.faction}]"
        )

        # Casos d'impacte del projectil
        if rd.random() <= projectil.precision:
            print(f"  > El projectil es dirigeix al [{objectiu.name}]")
            fila = rd.randint(0, 1)
            col = rd.randint(0, 2)
            pos_str = f"({fila},{col})"

            res, dany = objectiu.rebre_impacte(projectil.damage)

            if res == "esquivat":
                print("      >> El projectil es esquivat!")
            elif res == "mitigat":
                objectiu.aplicar_dany(dany, fila, col)
                print(
                    f"      >> El [{objectiu.name}] aconsegueix mitigar els danys i reb "
                    f"[{dany}] punts d'impacte a la posició [{pos_str}]"
                )
            else:
                objectiu.aplicar_dany(dany, fila, col)
                print(f"      >> El projectil impacta a la posició [{pos_str}]")
        else:
            print("  > El projectil ha fallat!")

        # Resum de la ronda amb l'estat dels tancs
        print("\n> Resum final de la ronda:")
        for t in tots_els_tancs:
            estat = "RETIRAT" if not t.esta_viu() else "EN COMBAT"
            print(
                f"  > ({estat}) El [{t.name}] de la facció [{t.faction}] amb els blindatges superior {t.blindatge[0]}, inferior {t.blindatge[1]} "
            )
        print("-" * 50 + "\n")
        num_ronda += 1

    # Final de la batalla amb la facció guanyadora i els tancs supervivents de la facció
    faccio_guanyadora = list(obtenir_faccions_vives(tots_els_tancs))[0]
    tancs_supervivents = [t.name for t in obtenir_tancs_vius(tots_els_tancs)]

    print(
        f"🏆 LA BATALLA HA FINALITZAT! La facció guanyadora és [{faccio_guanyadora}] "
        f"amb els tancs supervivents: {', '.join(tancs_supervivents)}!"
    )


if __name__ == "__main__":
    main()