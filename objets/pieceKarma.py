from objet import ObjetRamassable
from objets.potion import Potion
from objets.regenerationPotion import RegenerationPotion


import random

class PieceKarma(ObjetRamassable):
    """ Représente une piece karma qui donne un objet aléatoirement quand on l'utilise. """

    def __init__(self, lvl):
        """ Arguments :
        - lvl : represente le niveau de la piece karma, plus le lvl et haut plus la piece drop dobj
        """
        self._lvl = lvl
        self.duration = 3 * lvl

    def utiliser(self, joueur):
        if (self.duration > 1):
            self.giveRandomItem(joueur)
            self.duration -= random.randint(1,3) #la résistance perd des point en fx de la chance
            joueur.mettreObjetDansLeSac(self)
        else:
            pass
        
    #mes dans le sac du joueur un objet aleatoire
    def giveRandomItem(self, joueur):
        rand = random.randint(1,2)
        if (rand == 1):
            potion = RegenerationPotion(random.randint(1,6), 3)
        elif rand == 2:
            potion = Potion(random.randint(1,11))
        joueur.mettreObjetDansLeSac(potion)



    def description(self):
        return "Piece du karma (lvl:"+str(self._lvl) + ", resistance:"+str(self.duration)