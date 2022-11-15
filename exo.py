import random 
import string

# DEBUT
rh = 230 
r = 12000
e = 10
s = 1250

assertionGauche = (( (365 * 3 ) / (24 - (16 - 8 ))) * (rh) > r) 
assertionDroite = (e * s < r)

#assertionGauche2 = (( (365 * 3 ) / (4 - (12 - 8 ))) * (rh) > r)

assertionFinale = assertionGauche == assertionDroite
#assertionFinale2 = assertionGauche2 == assertionDroite

def print1():
    print (assertionGauche) #True
    print (assertionDroite) #False
    print (assertionFinale) #Gauche

#def print2():
    #print (assertionGauche2) #Error = False
    #print (assertionDroite) #False
    #print (assertionFinale2) #True


# FIN 

#Debut
def sum (x,y):
    return x+y

def sub (x,y):
    return x-y

def multi (x,y):
    return x*y

def div (x,y):
    if y==0 :
        print("on ne peut pas diviser par zero")
    else:
        return x/y

def modulo(x,y):
    return x%y

#FIN

#DEBUT

#definir une fonction withdraxfees en fonction qui retir un pourcentage a un total en fonction d'un total et d'un pourcentage
def withfrawFees(total,percent):
    #definir fees en fonction d'un total et d'un pourcentage
    fees = total * (percent/100)
    #soustraire fees au total
    result = total - fees
    #retourner la valeur obtenue 
    return result

#deifinir une fonction qu retourne le salaire net en fonction du salaire brut (float) et du secteur d'activite (isPublic > booleen)
def salaireNet(salaireBrut,isPublic):    
    #si je suis un travailleur du secteur public 
    if isPublic:
        #Alors je soustrais 15% de mon salaire
        salaireNet = withdrawFees(salaireBrut,15)
    #sinon travailleur privé
    else:
        #alors 23%
        salaireNet = withdrawFees(salaireBrut,23)
    #retourner salaire net
    return salaireNet

#FIN

#DEBUT

def gagnantInput():
    return random.choice(string.ascii_lowercase)
    
aTrouver = str(gagnantInput())
def minigameRecursive(compteur=0):
    compteur = compteur + 1
    rechercherInput = str(input("Qu'elle est ta lettre ? : "))
    if aTrouver == rechercherInput:
        print ("Felicitation la bonne lettre etais le " +str(aTrouver)+" en "+str(compteur)+" étapes")
    else:
        minigameRecursive(compteur)
#FIN

#DEBUT
#demande la lettre a trouver
#enlever le hashtag en dessous pour jouer
#recherche = str(input("qu'elle est ta lettre :"))

#definir la classe minigame avec un compteur a 0
def maxigame(compteur=0):
    #augmenter le compteur
    compteur = compteur + 1
    #importer les caractere aleatoire
    caractereGagnant = str(gagnantInput())
    #si cractere rechercher et cractere aleatoire sont pareil
    if recherche == caractereGagnant:
        #alors ecrire en combien d'etapes le robot la trouver
        print ("Ta lettre a etais trouvé en "+str(compteur)+ " étapes")
    #sinon on recommence
    else:
        maxigame(compteur)

#FIN


#Exercice 1
#Faire une fonction qui concatene 2 chaine de caractere, les separant par une virgule
def concatene(chaineA,chaineB):
    return f"{chaineA},{chaineB}"

#Excercice 2 
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere 
#avec l'ensembles des occurences d'un chiffre e.g.:
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau,0) doit renvoyer "0,4,7" n'hesitez pas a implementer la premiere fonction;
tableau=[0,0,0,0,0,3,2,3,5,4,8,5,0,1,4]
def fc(tab,number):
    L=[]
    compteur=0
    for i in tab:
        if i==number:
            L.append(compteur)
        compteur+=1
        
    return L
#Definir la fonction findIndex qui itere sur tableau, cherchant l'index
#des differentes occurences de x
    #definir i un index de départ
    #definir chaineRetour telle qu'une chaine de caractere vide
    #tant qui i est different du nombre d'elt dans le tableau
        #Alors j'attribue a une variable la valeur de tableau a l'index i
        #j'incremente i de 1
        #Si selected est egal à x 
            #Alors j'assigne le retour de concatWithComma tel que : concatWithComma(chaineRetour, i) à chaineReour
#Definir mon index
def wc(tab,number):
    i=0
    L=[]
    while i != len(tab):
        selected = tab[i]
        if selected == number:
            L.append(i)
        i=i+1
    return L
        


#Exercice 3 
#Renvoyez / Afficher un message


