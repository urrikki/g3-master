#DEBUT
import random

def FirstExo ():
    x=int(input("Que vaux x ? :"))
    y=int(input("Que vaux y ? :"))
    sub = x+y
    multi = x*y
    div = x/y
    modulo = x%y
    return sub , multi , div , modulo

def salaire (brut , coef):
    return brut-(brut*(coef/100)) 

def info(salaireannee):
    mois = int(salaireannee/12)
    semaine = int(salaireannee/52)
    jour = int(salaireannee/365)
    heure = int(salaireannee/8760)
    minute = salaireannee/525600
    seconde = salaireannee/31536000
    return str(mois) +" par mois " + str(semaine) + " par semaine " + str(jour) + " par jour " + str(heure)  + " par heure " + str(minute) + " par minute " + str(seconde) +" par seconde "


#FIN

#definir une def minijeu
def minigame():
#cree une variable gagant
    caractereGagnant = str(input("Essaye de trouver la lettre caché :"))
    #cree un tant que input = gagant si resultat pas bon recommencer
    while caractereGagnant != input():
        caractereGagnant = str(input("Ce n'est pas ca essaye à nouveau :"))
    #annoncer la victoire
    print("felicitation la lettre gagnante etais le "+str(caractereGagnant))

