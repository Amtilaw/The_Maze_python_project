from action import Action
from joueur import Joueur

class SacAction(Action):

    def __init__(self, joueur):
        self.joueur = joueur

    def execute(self, param):
        sac = self.joueur.getSac()
        if(len(sac)) == 0:
            print("Le sac est vide")
            input()
        else:
            print("Le sac contient: ")
            index = 0
            for obj in sac:
                print(str(index+1)+" - "+obj.description())
                index += 1
            choice = input("Pour utiliser un objet, taper son numéro, ou entrée pour ne rien faire. ")
            try:
                num = int(choice)
                obj = sac[num-1]
                sac.remove(obj)
                obj.utiliser(self.joueur)
            except:
                pass # En cas d'err

    def info(self):
        return "Ouvre le sac"

    def help(self):
        return """Affiche un document du catalogue
Paramètres : un entier qui correspond au numéro du document à afficher
Attention, ne pas taper autre chose qu'un entier sinon ça plante !
"""



