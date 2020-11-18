from action import Action
from joueur import Joueur
import random

class RegarderAction(Action):

    def __init__(self, joueur):
        self.joueur = joueur

    def execute(self, param):
        case = self.joueur.getCaseCourante()
        personnages = case.getPersonnages()
        objets = case.getObjets()
        if(len(personnages) == 0 and len(objets) == 0):
            print(random.choice([
                "Je vois une salle poussièreuse, sans rien de plus que quelques cailloux.",
                "Des toiles d'araignées un peu partout.",
                "C'ets déseperement vide..."
            ]))
        else:
            print("Je vois :")
            for objet in objets:
                print(" - " + objet.description())
            for personnage in personnages:
                print(" - " + personnage.description())
        input()

    def info(self):
        return "Regarde la case"

    def help(self):
        return """Affiche un document du catalogue
Paramètres : un entier qui correspond au numéro du document à afficher
Attention, ne pas taper autre chose qu'un entier sinon ça plante !
"""



