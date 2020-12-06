from objet import ObjetRamassable
import random

class Piece(ObjetRamassable):
    """ Représente une piece qui donne de l'argent au joueur. """

    def __init__(self):
        self.value = random.randint(1, 10)

    def utiliser(self, joueur):
        pass

    def description(self):
        return "piece"