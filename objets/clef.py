from objet import ObjetRamassable

class Clef(ObjetRamassable):
    """ Représente une clef qui ouvre la porte de sortie. """

    def __init__(self):
        self.clefPorte ="clef_sortie"

    def utiliser(self, joueur):
        meubles = joueur.getCaseCourante().getMeubles()
        if (len(meubles) > 0):
            for i in range(0, len(meubles)):
                if (meubles[i].description() == "Porte fermé menant à une destination inconue"):
                    print("Gagné!")

    def description(self):
        return "Clef qui ouvre une porte"