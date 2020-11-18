from action import Action
from joueur import Joueur

class InteractAction(Action):

    def __init__(self, joueur):
        self.joueur = joueur

    def execute(self, param):
        meubles = self.joueur.getCaseCourante().getMeubles()
        if len(meubles) == 0:
            print("Il n'y a aucun meuble")
        else:
            for meuble in meubles:
                meuble.interact(self.joueur)
        input()

    def info(self):
        return "Parle avec un personnage"

    def help(self):
        return """Affiche un document du catalogue
Paramètres : un entier qui correspond au numéro du document à afficher
Attention, ne pas taper autre chose qu'un entier sinon ça plante !
"""



