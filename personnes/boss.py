from personnage import Personnage
from objets.clef import Clef
import random

class Boss(Personnage):
    """ Cette classe représente le boss du labyrinth qui annonce la quete et vend la clef du labyrinth """

    def __init__(self, prix_clef):
        """ Constructeur. Paramètres :
        - prix_clef: le prix de la clef en $ ou € ou piece
        """
        self._prix_clef = prix_clef

    def description(self):
        """ Renvoie la description du boss."""
        return "Le boss du labyrinth vend une clef a  " + self._prix_clef

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        TODO: on pourrait avoir un message de salutation plus varié en le tirant aléatoirement ici, ou dans le constructeur pour qu'un même perroquet salue toujours de la même façon.
        """
        print("Je suis le Boss de se labyrinth, reviens vers moi quand tu as trouver "+ str(self._prix_clef) + " $")
        input()

    def parler(self, joueur):
        """ Le boss demande au joueur si il veut acheter la clef. Si le joueur a assez il peut et obtient la clef. """
        print("Tu veut acheter la clef? o/n")
        entree = input("#>")
        if (entree == "o" or entree == "0" or entree == "O") and joueur.getMoney() >= self._prix_clef:
            print("Tu as bien merite cette clef..")
            clef_sortie = Clef()
            joueur.debite(self._prix_clef)
            joueur.mettreObjetDansLeSac(clef_sortie)
            input()
