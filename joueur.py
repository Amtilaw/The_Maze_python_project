from labyrinthe.labyrinthe import Case

class Joueur:

    def __init__(self, symbole,  energieInitiale):
        # La case sur laquelle se situe le joueur
        self.__caseCourante = Case()
        self.__symbole = symbole
        self.__energieMax = 70 # TODO: mettre le niveau d'énergie max en fonction du paramétrage du jeu
        self.__energie = 0
        self.__money = 0
        self._sac = [] # On commence avec un sac vide
        self.setEnergie(energieInitiale)
        self.regenDuree = [0, 0]
        self.__gagne = False

    def getEnergie(self):
        """ Renvoie le niveau d'énergie du joueur. """
        return self.__energie

    def getMoney(self):

        return self.__money

    def debite(self, valeur):

        self.__money -= valeur

    def credite(self, valeur):
        self.__money += valeur


    def setEnergie(self,valeur):
        """ Fise l'energie du joueur à une valeur donnée, sans pouvoir dépasser le maximum autorisé. """
        self.__energie = min(valeur, self.__energieMax)

    def perdreEnergie(self):
        """ Retire un point d'énergie au joueur. """
        self.__energie -= 1


    def gagnerEnergie(self, combien):
        """ Ajoute de l'énergie au joueur. Paramètres :
        - combien : le montant d'énergie ajouté
        """
        self.__energie = min(self.__energie + combien, self.__energieMax)

    def regenEnergi(self, combien, duree):
        """ Ajoute de l'énergie au joueur sur x tours Param:
        - combien : le montant d'énergie ajouté par tour
        - duree : le nb de tour
        """
        self.regenDuree[0] += duree
        self.regenDuree[1] += combien
        self.gagnerEnergie(combien)

    def getCaseCourante(self):
        return self.__caseCourante

    def setCaseCourante(self, case):
        # Enlève le joueur de la case sur laquelle il se trouve actuellement
        self.__caseCourante.supprimerJoueur()
        # Ajoute le joueur sur la nouvelle case
        self.__caseCourante = case
        case.ajouterJoueur(self)
        # Découvre les cases alentour
        self.decouvreAlentour()
        # Rencontre tous les personnages potentiellements présents sur la case
        for personnage in case.getPersonnages():
            personnage.rencontrer(self)

    def decouvreAlentour(self):
        self.__caseCourante.decouvrir()
        if self.__caseCourante.estOuvertNord(): self.__caseCourante.getCaseNord().decouvrir()
        if self.__caseCourante.estOuvertSud(): self.__caseCourante.getCaseSud().decouvrir()
        if self.__caseCourante.estOuvertEst(): self.__caseCourante.getCaseEst().decouvrir()
        if self.__caseCourante.estOuvertOuest(): self.__caseCourante.getCaseOuest().decouvrir()

    def getSymbole(self):
        return self.__symbole

    def avancerNord(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertNord(): self.setCaseCourante(caseCourante.getCaseNord())
        else: raise ValueError("Pas de passage par là...")

    def avancerSud(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertSud(): self.setCaseCourante(caseCourante.getCaseSud())
        else: raise ValueError("Pas de passage par là...")

    def avancerEst(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertEst(): self.setCaseCourante(caseCourante.getCaseEst())
        else: raise ValueError("Pas de passage par là...")

    def avancerOuest(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertOuest(): self.setCaseCourante(caseCourante.getCaseOuest())
        else: raise ValueError("Pas de passage par là...")

    def printEnergie(self):
        """ Petite fonction utilitaire pour afficher la jauge d'énergie sur la console. """
        print(" ENERGIE " + ">"*self.__energie + " "*(self.__energieMax-self.__energie) + "|")

    def getSac(self):
        return self._sac
        
    def mettreObjetDansLeSac(self,objet):
        """ Met l'objet passé en paramètre dans le sac du joueur."""
        self._sac.append(objet)

    # fait une mise a jour des processus
    def checkActions(self):
        self.checkRegen()

    # processus de regeneration si une potion de regen est en cour
    def checkRegen(self):
        if (self.regenDuree[0] > 0):
            self.gagnerEnergie(self.regenDuree[1])
            self.regenDuree[0] -= 1
            if (self.regenDuree[0] == 0):
                self.regenDuree[1] = 0
    def setGagne(self):
        if self.__gagne:
            self.__gagne = False
        else:
            self.__gagne = True

    def getGagne(self):
        return self.__gagne
