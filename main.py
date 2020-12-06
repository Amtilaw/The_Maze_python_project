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
from personnes.mercenaire import Mercenaire
from personnes.guerisseur import Guerisseur
from personnes.pere_noel import Pere_noel
from objets.vie import Vie

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
# TODO: récupérer les attributs via un menu de configuration FAIT

print("MENUE - \n \n Niveau du labyrinth \n facile \n moyen \n difficile")
taille = input("#>")

l = Labyrinthe(taille)
nbPotion = 30
nbPotionRegen = 10
nbVoleur = 3
nbPerro = 15
nbPiece = 45
nbPieceKarma = 5
nbMercenaire = 4
nbPere_noel = 3
nbGuerriseur = 5
nbVie = 2

joueur = Joueur("X",100)
l.deposerJoueurAleatoirement(joueur)

for i in range(nbPere_noel):
    pere_noel = Pere_noel(3)
    l.deposerPersonneAleatoirement(pere_noel)
for i in range(nbVie):
    vie = Vie()
    l.deposerObjetAleatoirement(vie)
for i in range(nbGuerriseur):
    guerisseur = Guerisseur(20)
    l.deposerPersonneAleatoirement(guerisseur)

for i in range(nbPotionRegen):
    potion = RegenerationPotion(random.randint(1,5), 3)
    l.deposerObjetAleatoirement(potion)

for i in range(nbPotion):
    potion = Potion(random.randint(2,7))
    l.deposerObjetAleatoirement(potion)

for i in range(nbPieceKarma):
    piece = PieceKarma(random.randint(1,3))
    l.deposerObjetAleatoirement(piece)

for i in range(nbPiece):
    piece = Piece()
    l.deposerObjetAleatoirement(piece)

for i in range(nbPerro):
    l.deposerPersonneAleatoirement(Perroquet(random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])))

for i in range(nbMercenaire):
    l.deposerPersonneAleatoirement(Mercenaire(random.randint(1,3)))

l.deposerMeubleAleatoirement(PorteSortie())

l.deposerPersonneSurPersonnage(Boss(0))

# Ajouter des perroquets un peu partout
for i in range(nbVoleur):
    # l.deposerPersonneAleatoirement(Perroquet(random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])))
    l.deposerPersonneAleatoirement(Voleur())
# TODO : factoryMaker Fait
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
    if joueur.getEnergie() <= 0:
        for obj in joueur.getSac():
            if obj.description() == "Vous ressusite quand vous mourez":
                joueur.setEnergie(30)
                joueur.getSac().remove(obj)
        if joueur.getEnergie() <= 0:
            print("Game Over!")
            break
    elif joueur.getGagne() == True:
        print("Vous avez Gagne!")
        break

