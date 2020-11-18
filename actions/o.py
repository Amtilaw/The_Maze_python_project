from action import Action
from joueur import Joueur

class OAction(Action):

    def __init__(self, joueur):
        self.joueur = joueur

    def execute(self, param):
        try:
            self.joueur.avancerOuest()
        except:
            print("Ouch, ce mur fait mal...")
            input()

    def info(self):
        return "Fait avancer le perssonage à gauche"

    def help(self):
        return """Affiche un document du catalogue
Paramètres : un entier qui correspond au numéro du document à afficher
Attention, ne pas taper autre chose qu'un entier sinon ça plante !
"""



