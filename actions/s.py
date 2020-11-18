from action import Action
from joueur import Joueur

class SAction(Action):

    def __init__(self, joueur):
        self.joueur = joueur

    def execute(self, param):
        try:
            self.joueur.avancerSud()
        except:
            print("Ouch, ce mur fait mal...")
            input()

    def info(self):
        return "Fait avancer le perssonage en bas"

    def help(self):
        return """Affiche un document du catalogue
Paramètres : un entier qui correspond au numéro du document à afficher
Attention, ne pas taper autre chose qu'un entier sinon ça plante !
"""



