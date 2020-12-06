from action import Action
from joueur import Joueur

class RamasserAction(Action):

    def __init__(self, joueur):
        self.joueur = joueur

    def execute(self, param):
        case = self.joueur.getCaseCourante()
        if len(case.getObjets()) == 0:
            print("Mais... il n'y a rien à ramasser !")
        else:
            print("J'ai ramassé :")
            for objet in case.getObjets():
                print(" - " + objet.description())
                if objet.description() == "piece":
                    print("+ "+str(objet.value)+ " € !")
                    self.joueur.credite(objet.value)
                else:
                    objet.ramasser(self.joueur)
            case.getObjets().clear() # On est obliger de tout supprimer après avoir ramassé, car on ne peut pas modifier la liste sur laquelle on itere...
        input()

    def info(self):
        return "ramasse un objet"

    def help(self):
        return """Affiche un document du catalogue
Paramètres : un entier qui correspond au numéro du document à afficher
Attention, ne pas taper autre chose qu'un entier sinon ça plante !
"""



