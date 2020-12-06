from personnage import Personnage
from objets.piece import Piece
from objets.pieceKarma import PieceKarma as PieceK
from objets.potion import Potion
from objets.regenerationPotion import RegenerationPotion
import random

class Pere_noel(Personnage):
    """ Cette classe représente un pere noël qui donne des cadeaux aleatoirement 1x """

    def __init__(self, nbCadeaux):
        """ Constructeur. Paramètres :
        - nbEnergies : int, nombre d'energie que le guerriseur soigne
        """
        self._nbCadeaux = nbCadeaux
        self._lock = False

    def description(self):
        """ Renvoie la description du pere Noël."""
        return "Le pere Noël donne " + self._nbCadeaux + " cadeaux"

    def rencontrer(self, joueur):
        """ Se presente au joueur
        """
        print("Je me suis perdu dans se labyrinth.. Moi le pere Noel..")
        input()

    def parler(self, joueur):
        """ Le pere noël donne des cadeaux aleatoirement """
        if self._lock == False:
            print("Un nouveau gaté! plein de cadeaux pour toi!")
            listCadeaux = [Potion(random.randint(4,15)),Piece(),PieceK(random.randint(3,5)),RegenerationPotion(random.randint(3,8), 3)]
            for i in range(self._nbCadeaux):
                choixCadeau = random.choice(listCadeaux)
                print("Ho ho ho!")
                print("+ 1 : "+ choixCadeau.description())
                joueur.mettreObjetDansLeSac(choixCadeau)
            self._lock = True
            input()
        else:
            print("Tu en veut encore? viens dans 1 ans!")
