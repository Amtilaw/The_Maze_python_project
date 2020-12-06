from personnage import Personnage

import random

class Guerisseur(Personnage):
    """ Cette classe représente un guerisseurqui qui soigne 1x le joueur """

    def __init__(self, nbEnergies):
        """ Constructeur. Paramètres :
        - nbEnergies : int, nombre d'energie que le guerriseur soigne
        """
        self._energie = nbEnergies
        self._lock = False

    def description(self):
        """ Renvoie la description du guerriseur."""
        return "Le guerriseur soigne pour " + self._energie

    def rencontrer(self, joueur):
        """ demande au joueur si il veut etre soigne
        """
        print("Coucou tu veut que je te soigne?")
        input()

    def parler(self, joueur):
        """ Le guerriseur le guerrie. """
        if self._lock == False:
            print(".. .. ..")
            joueur.gagnerEnergie(self._energie)
            print("+ " + str(self._energie) + " energies!")
            self._lock = True
            input()
        else:
            print("Je t'es deja soigne.")
