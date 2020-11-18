from meuble import Meuble

class PorteSortie(Meuble):
    """ Représente une porte qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self):
        """ Arguments :
        - energie : la quantité d'energie récupérée lorsque l'on utilise la potion
        """
        self._forme = "8"

    def interact(self, joueur):
        print("Cette porte est fermé, où est la clef?")


    def description(self):
        return "Porte fermé menant à une destination inconue"