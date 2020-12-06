from objet import ObjetRamassable
import random

class Vie(ObjetRamassable):
    """ Représente une vie en plus si le joueur meurt. """

    def __init__(self):
        self._vie = 1

    def utiliser(self, joueur):
        print("garder cette objet dans votre inventaire au cas ou.")
        joueur.mettreObjetDansLeSac(self)


    def description(self):
        return "Vous ressusite quand vous mourez"