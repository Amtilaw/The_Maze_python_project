from objet import ObjetRamassable
from actions.interact import InteractAction

class Clef(ObjetRamassable):
    """ Représente une clef qui ouvre la porte de sortie. """

    def __init__(self):
        self.clefPorte ="clef_sortie"

    def utiliser(self, joueur):
        meubles = joueur.getCaseCourante().getMeubles()
        if (len(meubles) > 0):
                InteractAction(joueur)

    def description(self):
        return "Clef qui ouvre une porte"