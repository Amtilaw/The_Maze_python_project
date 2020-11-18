from exceptions import AbstractMethodCallException

class Meuble:
    """ Cette interface représente un meuble interractif"""

    def interact(self, joueur):
        """ Cette méthode est appelée lorsque le joueur interragi avec un meuble.
        En fonction du meuble, celui-ci peut """
        raise AbstractMethodCallException() # Méthode abstraite

    def description(self):
        """ Renvoie une description de l'objet, pour pouvoir l'afficher. """
        raise AbstractMethodCallException() # Méthode abstraite


class MeubleInteraction(Meuble):
    """ Cette classe abstraite représente tout objet que l'on peut ramasser. La méthode ramasser implémente le code
    qui permet de mettre l'objet dans le sac du joueur. Il reste à définir la méthode utiliser().
    """

    def interact(self, joueur):
        raise AbstractMethodCallException() # Méthode abstraite

    def description(self):
        raise AbstractMethodCallException() # Méthode abstraite

