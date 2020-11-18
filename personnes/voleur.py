from personnage import Personnage
from objets.potion import Potion
import random

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Voleur(Personnage):
    """ Cette classe représente un Voleur qui salue le joueur et lui vole un objet """

    def __init__(self):
        """ Constructeur. Paramètres :
        - couleur : la couleur du perroquet (chaine de caractères)
        """

    def description(self):
        """ Renvoie la description du perroquet."""
        return "Un voleur"

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        TODO: on pourrait avoir un message de salutation plus varié en le tirant aléatoirement ici, ou dans le constructeur pour qu'un même perroquet salue toujours de la même façon.
        """
        print("Un voleur vous salue et tente de vous vole!")
        sac = joueur.getSac()
        if (len(sac)== 0) :
            print("Le voleur est partie bredouille")
        else :
            randomI = random.randint(1,len(sac))
            objet = sac[randomI-1]
            sac.remove(objet)
        print(objet.description() +",  a ete pris par le voleur!")
        input()

    def parler(self, joueur):
        """ Le voleur propose de mettre en jeu le double de se qui à était volé,le joueur choisi un nb entre 1 et 3 si se trompe un obj en moin """
        sac = joueur.getSac()
        potion = Potion(random.randint(5,10))
        print("Je suis pas vraiment un voleur! Tu peut gagner 3 "+ potion.description() + " Tu te sens chanceux? o/n")
        start = input("#>")
        
        if (start == "o"):
            print("Il ny a pas de triche, je met les 3 "+ potion.description() + " sous un des 3 pots. Si tu te trompe tu perd un objet sinon tu en gagne 2!")
            print("""
                 _      ___        _    _      ___        _    _      ___        _ 
                | |    |__ \      | |  | |    |__ \      | |  | |    |__ \      | |
                | |______ ) |_____| |  | |______ ) |_____| |  | |______ ) |_____| |
                | |______/ /______| |  | |______/ /______| |  | |______/ /______| |
                | |     |_|       | |  | |     |_|       | |  | |     |_|       | |
                | |     (_)       | |  | |     (_)       | |  | |     (_)       | |
                | |               | |  | |               | |  | |               | |
                |_|      1        |_|  |_|       2       |_|  |_|        3      |_|
                """)
            print("Tu choisi lequel? 1 - 2 - 3")
            choix = int(input("#>"))
            nb = random.randint(1,3)
            if (choix == nb):
                cls()
                if(nb == 1):
                    print(""" 
                     _                   _      _        _    _        _ 
                    | |                 | |    | |      | |  | |      | |
                    | | ___   ___   ___ | |    | |      | |  | |      | |
                    | |/ _ \ / _ \ / _ \| |    | |      | |  | |      | |
                    | | (_) | (_) | (_) | |    | |      | |  | |      | |
                    | |\___/ \___/ \___/| |    | |      | |  | |      | |
                    | |                 | |    | |      | |  | |      | |
                    |_|                 |_|    |_|      |_|  |_|      |_|

                    """)
                elif (nb == 2):
                    print("""              
                     _        _      _                   _    _        _ 
                    | |      | |    | |                 | |  | |      | |
                    | |      | |    | | ___   ___   ___ | |  | |      | |
                    | |      | |    | |/ _ \ / _ \ / _ \| |  | |      | |
                    | |      | |    | | (_) | (_) | (_) | |  | |      | |
                    | |      | |    | |\___/ \___/ \___/| |  | |      | |
                    | |      | |    | |                 | |  | |      | |
                    |_|      |_|    |_|                 |_|  |_|      |_|

                    """)
                elif (nb == 3):
                    print(""" 
                   
                     _        _      _        _    _                   _ 
                    | |      | |    | |      | |  | |                 | |
                    | |      | |    | |      | |  | | ___   ___   ___ | |
                    | |      | |    | |      | |  | |/ _ \ / _ \ / _ \| |
                    | |      | |    | |      | |  | | (_) | (_) | (_) | |
                    | |      | |    | |      | |  | |\___/ \___/ \___/| |
                    | |      | |    | |      | |  | |                 | |
                    |_|      |_|    |_|      |_|  |_|                 |_|

                    """)

                print("Tu a Gagne!")
                potion.ramasser(joueur)
                potion.ramasser(joueur)
                potion.ramasser(joueur)
            else :
                print("Perdu! je te prend ..")
                if (len(sac) == 0):
                    print("Tu essais de jouer au plus malin! Aucun objet!")
                else :
                    randomI = random.randint(1,len(sac))
                    objet = sac[randomI-1]
                    sac.remove(objet)
                    print(objet.description() +",  a ete pris par le voleur!")

        else :
            print("Merci encore!")