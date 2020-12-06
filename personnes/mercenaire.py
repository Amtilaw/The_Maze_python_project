from personnage import Personnage
import random
#TODO : ecrire des bon commentaires.
class Mercenaire(Personnage):
    """ Cette classe représente le boss du labyrinth qui annonce la quete et vend la clef du labyrinth """

    def __init__(self, lvl):
        """ Constructeur. Paramètres :
        - prix_clef: le prix de la clef en $ ou € ou piece
        """
        self._lvl = lvl
        self._attaque = lvl *3
    #TODO : faire description Mercenaire
    def description(self):
        """ Renvoie la description du boss."""
        return "Le boss du labyrinth vend une clef a  " + self._prix_clef

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur et lui explique la quête.
        """

        print("Un mercenaire vous attaque! il vous as enlever "+ str(self._attaque) + " point de energie.")
        joueur.blesse(self._attaque)
        input()

    def parler(self, joueur):
        """ Le boss demande au joueur si il veut acheter la clef. Si le joueur a assez il peut et obtient la clef. """
        print("Tu veut acheter la clef? o/n")
