#-*- coding: utf-8 -*-
import random as rd
print("Bienvenu dans le jeu hangman\n#####################################")
avertissement = 3
essais = 6
start = 0
end = ""
bon_essai = 0
b = 0
ancien_score = 0
caractere = list(end)
voyelle = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonne = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
          'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
position = 0
pendaison = ['''
        +---+
        |   |
            |
            |
            |
            |
    ===========''','''
        +---+
        |   |
        O   |
            |
            |
            |
    ===========''' , '''
        +---+
        |   |
        O   |
       /    |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    ===========
    ''',
    '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    ===========
    ''']
print("Vous avez 3 ponit-erreur\n#####################################")
print("Vous avez 6 tentatives\n##########################################")
print(pendaison[position])

#Choix du niveau
n = 0
def niveau():
    global n
    while n<1 or n>3:
        while True:
            try:
                n = int(input(" Choisir un niveau de 1 a 3: "))
                break
            except:
                print(" Error: Entrer un nombre")
                pass
        #n=int(input("Error: Choisir un niveau de 1 a 3: "))
    return n
print("###################################\nVous avez choisi le niveau ",niveau())
num = niveau()

#Choix des mots
def debut(n):
    if n == 1:
        fichier = open('mots5.txt', 'r')
    elif n == 2:
        fichier = open('mots8.txt', 'r')
    else:
        fichier = open('mots10p.txt', 'r')
    texte = fichier.readlines()
    mot = rd.choice(texte)
    print("Chargement de fichier...")
    print(len(texte), "mots chargés")
    #Affichage mot pour vérifier
    #print(mot)
    return mot.lower()
niv = debut(num)
start = len(niv)-1
trouve = []
print("Je vous propose un mot de ",start," lettres. Devinez de quel mot s'agit il\n################################")
for char in range(len(niv)-1):
    end = end+"-"
print(end)
#Saisir lettre
def saisie_lettre():
    a = input("Saisir une lettre: ")
    return a.lower()
#Si la lettre avait été déjà saisie
def dejaSaisie(a):
    global trouve
    if a in trouve:
        global avertissement
        global position
        global pendaison
        position += 1
        print("Lettre déjà trouvé.\n##################################")
        global essais
        avertissement -= 1
        if avertissement < 0:
            essais -= 1
            avertissement = 0
            print("Il vous reste plus d'avertissement")
        else:print("Il vous reste ", avertissement, " avertissements\n#################################")
        #essais-=1
        print("Il vous reste ", essais, " tentatives\n#################################")
        print(pendaison[6 - essais])
        print(end)
    return (a)
#Si la lettre est une consonne qui n'est pas dans le mot
def Cnsne(a):
    global consonne
    if (a in niv) == False and a in consonne:
        global position
        global pendaison
        position += 1
        print("vous avez saisi une consonne qui n'est pas dans le mot.\nVous perdez une tentative.\n#################################")
        global essais
        essais -= 1
        print("Il vous reste ",essais," tentatives\n########################################")
        print(pendaison[6 - essais])
        global end
        print(end)
    return (a)
#Si la lettre est une voyelle qui n'est pas dans le mot
def Vyl(a):
    global essais
    global voyelle
    global end
    if (a in niv) == False and (a in voyelle):
        global position
        global pendaison
        position += 1
        print("vous avez saisi une voyelle qui n'est pas dans le mot.\nVous perdez deux tentatives.\n#######################################")
        essais -= 2
        print("Il vous reste ",essais," tentatives\n###########################################")
        print(pendaison[6 - essais])
        print(end)
    return(a)
#Si elle n'est pas un caractère de l'alphabet
def alpha(a):
    global essais
    global consonne
    global voyelle
    global end
    global avertissement
    if (a in consonne) == False and (a in voyelle) == False or (len(a) > 1):
        global position
        global pendaison
        position += 1
        print("Vous ne pouvez saisir que les lettres de l'alphabet(ni mot, ni caractère).\n##################################")
        #essais-=1
        avertissement -= 1
        if avertissement < 0:
            essais -= 1
            avertissement = 0
            print("Il ne vous reste plus d'avertissement")
            print(pendaison[6-essais])
            print(end)
        else:
            print("Il vous reste ", avertissement, " avertissements\n#################################")
            print("Il vous reste ", essais, " tentatives\n#################################")
        
    return (a)    
#Si la lettre saisie est correcte
def Correcte(a):
    global essais
    global end
    global niv
    global trouve
    global bon_essai
    global caractere
    #global b
    if (a in niv) and (a in trouve) == False and (len(a) == 1):
        trouve.append(a)
        b = 0
        while (b < len(niv)):
            if niv[b] == a:
                caractere = list(end)
                x = b
                caractere[x] = a
                end = "".join(caractere)
            b += 1
        print(end)
        print("Bravo, lettre correcte")
        #print(niv)
        bon_essai += 1
        if essais > 6:
            essais = 6
            print("Il vous reste ", essais, " tentatives")
    return (a)

#Continuer la partie
continuer = 1

while continuer == 1:
    
#Controle and Affichage
    while essais > 0:
        
        lettre = saisie_lettre()
        dejaSaisie(lettre)
        Cnsne(lettre)
        Vyl(lettre)
        alpha(lettre)
        Correcte(lettre)
        if essais <= 0:
            print("_______________________________________________________\n\nVous êtes pendu.")
            print(pendaison[6])
            print("Le mot était : "+str(niv))
        if niv.rfind(end) == False:
            score=essais*bon_essai
            print("_______________________________________________________\n\nFélicitation: Vous avez deviné le mot; Votre score: "+str(score)+"")                
            if(ancien_score < score):
                #ancien_score = score
                print("Vous avez battu votre score qui est passé de", ancien_score, " à ", score)
                ancien_score = score
            break
    continuer = int(input('Saisir 1 pour continuer ou une autre touche pour quitter: '))
    if continuer==1:
        niv = debut(num)
        start = 0
        avertissement = 3
        essais = 6
        
        position = 0
        end = ""
        for char in range(len(niv) - 1):
            end = end + "-"
        caractere = list(end)
        bon_essai = 0
        trouve = []
        start = len(niv) - 1
        trouve = list(end)
        b = 0
        
        print("Je vous propose un mot de ", start, " lettres. Devinez de quel mot s'agit il\n################################")
        
        