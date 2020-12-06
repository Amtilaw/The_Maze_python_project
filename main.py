from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur

from objets.potion import Potion
from objets.regenerationPotion import RegenerationPotion
from personnes.perroquet import Perroquet
from personnes.voleur import Voleur
from objets.pieceKarma import PieceKarma
from meubles.porteSortie import PorteSortie
from personnes.boss import Boss
from objets.piece import Piece

from action import ActionManager
from actions.parler import ParlerAction
from actions.regarder import RegarderAction
from actions.ramasser import RamasserAction
from actions.sac import SacAction
from actions.n import NAction
from actions.s import SAction
from actions.e import EAction
from actions.o import OAction
from actions.interact import InteractAction

import random


import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen

cls()

print("""

   .____                                                          
   |    |    ____                                                 
   |    |  _/ __ \                                                
   |    |__\  ___/                                                
   |_______ \___  >                                               
           \/   \/                                                
.____          ___.                 .__        __  .__            
|    |   _____ \_ |__ ___.__._______|__| _____/  |_|  |__   ____  
|    |   \__  \ | __ <   |  |\_  __ \  |/    \   __\  |  \_/ __ \ 
|    |___ / __ \| \_\ \___  | |  | \/  |   |  \  | |   Y  \  ___/ 
|_______ (____  /___  / ____| |__|  |__|___|  /__| |___|  /\___  >
        \/    \/    \/\/                    \/          \/     \/
        
         
""")
input("   Appuyer sur 'Entrée' pour entrer dans le labyrinthe")


cls()



# Création des objets
# TODO: récupérer les attributs via un menu de configuration

print("MENUE - \n \n Niveau du labyrinth \n faible \n moyen \n fort")
taille = input("#>")
if (taille == "faible"):
    l = Labyrinthe(10,5)
    nbPotion = 30
    nbPotionRegen = 10
    nbVoleur = 16
    nbPerro = 10
    nbPiece = 30
elif (taille == "moyen"):
    l = Labyrinthe(20,10)
    nbPotion = 60
    nbPotionRegen = 20
    nbVoleur = 30
    nbPerro = 35
    nbPiece = 60
elif (taille == "fort"):
    l = Labyrinthe(30,15)
    nbPotion = 70
    nbPotionRegen = 35
    nbVoleur = 45
    nbPerro = 47
    nbPiece = 80
else:
    l = Labyrinthe(20, 10)
    nbPotion = 30
    nbPotionRegen = 10
    nbVoleur = 16
    nbPerro = 16
    nbPiece = 30
joueur = Joueur("X",100)
l.deposerJoueurAleatoirement(joueur)
nbPieceKarma = 80
# Generation de 70 potions aléatoirement
for i in range(nbPotionRegen):
    potion = RegenerationPotion(random.randint(1,3), 3)
    l.deposerObjetAleatoirement(potion)

for i in range(nbPotion):
    potion = Potion(random.randint(1,3))
    l.deposerObjetAleatoirement(potion)

for i in range(nbPieceKarma):
    piece = PieceKarma(random.randint(1,3))
    l.deposerObjetAleatoirement(piece)

for i in range(nbPiece):
    piece = Piece()
    l.deposerObjetAleatoirement(piece)

for i in range(nbPerro):
    l.deposerPersonneAleatoirement(Perroquet(random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])))

l.deposerMeubleAleatoirement(PorteSortie())

l.deposerPersonneSurPersonnage(Boss(0))

# Ajouter des perroquets un peu partout
for i in range(nbVoleur):
    # l.deposerPersonneAleatoirement(Perroquet(random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])))
    l.deposerPersonneAleatoirement(Voleur())

actionManager = ActionManager()
actionManager.registerCommand("parler",ParlerAction(joueur))
actionManager.registerCommand("regarder",RegarderAction(joueur))
actionManager.registerCommand("n", NAction(joueur))
actionManager.registerCommand("s", SAction(joueur))
actionManager.registerCommand("e", EAction(joueur))
actionManager.registerCommand("o", OAction(joueur))
actionManager.registerCommand("sac", SacAction(joueur))
actionManager.registerCommand("ramasser", RamasserAction(joueur))
actionManager.registerCommand("interagir", InteractAction(joueur))

actionManager.afficherCommandesDispo()

input()
while True:
    cls()  # Effacer la console
    joueur.checkActions()
    joueur.printEnergie()
    print()
    l.afficher()
    print()


    # Récupérer entrée utilisateur
    choix = input("Votre choix ? #> ")

   # Exécuter la commande
    actionManager.executerEntreeUtilisateur(choix)

    joueur.perdreEnergie()
