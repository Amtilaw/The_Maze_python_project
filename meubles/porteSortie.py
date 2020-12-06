from meuble import Meuble

class PorteSortie(Meuble):
    """ Représente une porte qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self):
        """ Arguments :

        """
        self._forme = "8"

    def interact(self, joueur):
        print("Cette porte est fermé, où est la clef?")
        for i in joueur.getSac():
            if i.description() == "Clef qui ouvre une porte":
                print("Vous avez trouver la sortie !!")
                joueur.setGagne()



    def description(self):
        return "Porte fermé menant à une destination inconue"

    def porteExist(self):
        return "porte"