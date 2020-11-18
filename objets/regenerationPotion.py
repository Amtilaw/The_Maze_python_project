from objet import ObjetRamassable

class RegenerationPotion(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self, energie, duree):
        """ Arguments :
        - energie : la quantité d'energie récupérée lorsque l'on utilise la potion
        """
        self._energie = energie
        self._duree = duree

    def utiliser(self, joueur):
        joueur.regenEnergi(self._energie, self._duree)

    def description(self):
        return "Potion de regeneration de "+str(self._energie) + "("+str(self._duree) + ")"