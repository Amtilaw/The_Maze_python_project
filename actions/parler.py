from action import Action
from joueur import Joueur

class ParlerAction(Action):

    def __init__(self, joueur):
        self.joueur = joueur

    def execute(self, param):
        personnages = self.joueur.getCaseCourante().getPersonnages()
        if len(personnages) == 0:
            print("Allo ? allo allo allo allo allo répète l'écho")
        else:
            for personnage in personnages:
                personnage.parler(self.joueur)
        input()

    def info(self):
        return "Parle avec un personnage"

    def help(self):
        return """Affiche un document du catalogue
Paramètres : un entier qui correspond au numéro du document à afficher
Attention, ne pas taper autre chose qu'un entier sinon ça plante !
"""



