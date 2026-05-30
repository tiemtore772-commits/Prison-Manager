# cells.py
# Gestion des cellules — BIT Prison Manager

from detainees import Detenu, detenus


# ──────────────────────────────────────────
#  CLASSE CELLULE
# ──────────────────────────────────────────

class Cellule:
    """
    Représente une cellule de la prison.
    Gère l'affectation et le retrait des détenus.
    """

    def __init__(self, numero: str, capacite_max: int):
        """
        Initialise une cellule.

        Args:
            numero       : Numéro identifiant la cellule (ex: 'A01')
            capacite_max : Nombre maximum de détenus
        """
        self.__numero        = numero
        self.__capacite_max  = capacite_max
        self.__liste_detenus = []   # liste des IDs des détenus affectés

    # ── Getters ──────────────────────────

    def get_numero(self) -> str:
        """Retourne le numéro de la cellule."""
        return self.__numero

    def get_capacite_max(self) -> int:
        """Retourne la capacité maximale."""
        return self.__capacite_max

    def get_liste_detenus(self) -> list:
        """Retourne la liste des IDs des détenus."""
        return self.__liste_detenus

    def get_nb_occupants(self) -> int:
        """Retourne le nombre actuel d'occupants."""
        return len(self.__liste_detenus)

    # ── Méthodes principales ─────────────

    def est_pleine(self) -> bool:
        """
        Vérifie si la cellule a atteint sa capacité maximale.

        Returns:
            bool : True si pleine, False sinon
        """
        return len(self.__liste_detenus) >= self.__capacite_max

    def ajouter_detenu(self, id_detenu: str) -> bool:
        """
        Affecte un détenu à la cellule si elle n'est pas pleine.

        Args:
            id_detenu : ID du détenu à affecter

        Returns:
            bool : True si ajout réussi, False sinon
        """
        if self.est_pleine():
            print(f"❌ Cellule {self.__numero} pleine.")
            return False

        if id_detenu in self.__liste_detenus:
            print(f"❌ Détenu {id_detenu} déjà dans cette cellule.")
            return False

        self.__liste_detenus.append(id_detenu)
        print(f"✅ Détenu {id_detenu} affecté à la cellule {self.__numero}.")
        return True

    def retirer_detenu(self, id_detenu: str) -> bool:
        """
        Retire un détenu de la cellule.

        Args:
            id_detenu : ID du détenu à retirer

        Returns:
            bool : True si retrait réussi, False sinon
        """
        if id_detenu in self.__liste_detenus:
            self.__liste_detenus.remove(id_detenu)
            print(f"✅ Détenu {id_detenu} retiré de la cellule {self.__numero}.")
            return True

        print(f"❌ Détenu {id_detenu} introuvable dans cette cellule.")
        return False

    def afficher_occupants(self) -> None:
        """Affiche les détails de la cellule et ses occupants."""
        print("\n" + "═" * 40)
        print(f"   CELLULE {self.__numero}")
        print("═" * 40)
        print(f"  Capacité   : {self.get_nb_occupants()} / {self.__capacite_max}")
        print(f"  Statut     : {'🔴 Pleine' if self.est_pleine() else '🟢 Disponible'}")
        print("  Occupants  :")

        if not self.__liste_detenus:
            print("    Aucun détenu affecté.")
        else:
            # Boucle for pour afficher chaque occupant
            for id_det in self.__liste_detenus:
                if id_det in detenus:
                    d = detenus[id_det]
                    print(f"    • [{id_det}] "
                          f"{d.get_prenom()} {d.get_nom()}")
                else:
                    print(f"    • [{id_det}] (introuvable)")
        print("═" * 40)

    def to_dict(self) -> dict:
        """
        Convertit la cellule en dictionnaire pour la sauvegarde JSON.

        Returns:
            dict : Données de la cellule
        """
        return {
            "numero"        : self.__numero,
            "capacite_max"  : self.__capacite_max,
            "liste_detenus" : self.__liste_detenus
        }


# ──────────────────────────────────────────
#  STOCKAGE EN MÉMOIRE
# ──────────────────────────────────────────

# Dictionnaire {numero_cellule : objet Cellule}
cellules: dict = {}


# ──────────────────────────────────────────
#  FONCTIONS DE GESTION
# ──────────────────────────────────────────

def creer_cellule() -> None:
    """Saisit les informations et crée une nouvelle cellule."""
    print("\n── CRÉER UNE CELLULE ──")
    numero      = input("Numéro de cellule (ex: A01) : ").strip().upper()
    capacite    = int(input("Capacité maximale          : "))

    if numero in cellules:
        print(f"❌ La cellule {numero} existe déjà.")
        return

    nouvelle = Cellule(numero, capacite)
    cellules[numero] = nouvelle
    print(f"✅ Cellule {numero} créée avec une capacité de {capacite}.")


def affecter_detenu() -> None:
    """Affecte un détenu existant à une cellule disponible."""
    print("\n── AFFECTER UN DÉTENU À UNE CELLULE ──")

    if not detenus:
        print("❌ Aucun détenu enregistré.")
        return

    if not cellules:
        print("❌ Aucune cellule créée.")
        return

    id_detenu = input("ID du détenu  : ").strip()
    num_cell  = input("Numéro cellule : ").strip().upper()

    # Vérifications
    if id_detenu not in detenus:
        print("❌ Détenu introuvable.")
        return

    if num_cell not in cellules:
        print("❌ Cellule introuvable.")
        return

    cellule = cellules[num_cell]
    detenu  = detenus[id_detenu]

    # Affectation
    succes = cellule.ajouter_detenu(id_detenu)

    if succes:
        # Mise à jour du côté du détenu aussi
        detenu.set_cellule(num_cell)


def retirer_detenu_cellule() -> None:
    """Retire un détenu d'une cellule."""
    print("\n── RETIRER UN DÉTENU D'UNE CELLULE ──")

    num_cell  = input("Numéro cellule : ").strip().upper()
    id_detenu = input("ID du détenu   : ").strip()

    if num_cell not in cellules:
        print("❌ Cellule introuvable.")
        return

    cellule = cellules[num_cell]
    succes  = cellule.retirer_detenu(id_detenu)

    if succes and id_detenu in detenus:
        detenus[id_detenu].set_cellule("Non assignée")


def lister_cellules() -> None:
    """Affiche l'état de toutes les cellules."""
    print("\n── LISTE DES CELLULES ──")

    if not cellules:
        print("Aucune cellule enregistrée.")
        return

    for cellule in cellules.values():
        statut = "🔴 Pleine" if cellule.est_pleine() else "🟢 Disponible"
        print(f"  Cellule {cellule.get_numero()} "
              f"— {cellule.get_nb_occupants()}/"
              f"{cellule.get_capacite_max()} "
              f"— {statut}")


def voir_cellule() -> None:
    """Affiche les détails et occupants d'une cellule précise."""
    print("\n── VOIR UNE CELLULE ──")
    num_cell = input("Numéro de cellule : ").strip().upper()

    if num_cell not in cellules:
        print("❌ Cellule introuvable.")
        return

    cellules[num_cell].afficher_occupants()


def menu_cellules() -> None:
    """Affiche le menu de gestion des cellules."""
    continuer: bool = True

    while continuer:
        print("\n╔══════════════════════════════════╗")
        print("║       GESTION DES CELLULES       ║")
        print("╠══════════════════════════════════╣")
        print("║  1. Créer une cellule            ║")
        print("║  2. Affecter un détenu           ║")
        print("║  3. Retirer un détenu            ║")
        print("║  4. Lister toutes les cellules   ║")
        print("║  5. Voir détails d'une cellule   ║")
        print("║  0. Retour au menu principal     ║")
        print("╚══════════════════════════════════╝")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            creer_cellule()
        elif choix == "2":
            affecter_detenu()
        elif choix == "3":
            retirer_detenu_cellule()
        elif choix == "4":
            lister_cellules()
        elif choix == "5":
            voir_cellule()
        elif choix == "0":
            continuer = False
        else:
            print("❌ Choix invalide. Réessayez.")
