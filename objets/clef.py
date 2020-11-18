from objet import ObjetRamassable

class Clef(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self):
        self.clefPorte ="Porte de sortie"

    def utiliser(self, joueur):
        meubles = joueur.getCaseCourante().getMeubles()
        if (len(meubles) > 0):
            for i in range(0, len(meubles)):
                if (meubles[i].description() == self.clefPorte):
                    print("Gagné!")

    def description(self):
        return "Potion de "+str(self._energie)