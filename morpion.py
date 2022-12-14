##-----Importation des Modules-----##
from tkinter import *
from tkinter.messagebox import *


##----- Définition des Variables globales -----##
cases=[ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
drapeau = True                              # True pour les croix, False pour les ronds
n = 1                                       # Numéro du tour de jeu


##----- Définition des Fonctions -----##
def afficher(event) :
    """ Entrées : Un événement de la souris
        Sortie : Affiche en temps réel les coordonnées de la case du clic de souris"""
    global drapeau, cases, n
    l = (event.y-2)//100                
    c = (event.x-2)//100                   

    if (n < 10) and (cases[l][c] == 0):
        if drapeau:                             
            dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = 'purple')
            dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = 'purple')
            cases[l][c] = 1
            message.configure(text='Aux tour des ronds :')
            drapeau = False
            

        else:
            dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = 'green')
            cases[l][c] = -1
            message.configure(text='Aux tour des croix :')
            drapeau = True

        
        if (n >= 5) and (n <= 9):
            v=verif(cases)
            if v == 1 or v == -1:
                n=gagner(v)
            elif v == 9:
                n=gagner(0)
        n += 1


def verif(tableau):
    test=0
    for i in range(3):
        for i2 in range(3):
            if tableau[i][i2] != 0:
                test+=1
    if test == 9:
        return 9
    else:
        if (tableau[0][0] + tableau[0][1] + tableau[0][2]) == 3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== 3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == 3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == 3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == 3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == 3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== 3:
            return 1
        elif (tableau[0][0] + tableau[0][1] + tableau[0][2]) == -3 or (tableau[1][0] + tableau[1][1] + tableau[1][2])== -3 or (tableau[2][0] + tableau[2][1] + tableau[2][2])==-3 or (tableau[0][0] + tableau[1][0] + tableau[2][0]) == -3 or (tableau[0][1] + tableau[1][1] + tableau[2][1]) == -3 or (tableau[0][2] + tableau[1][2] + tableau[2][2]) == -3 or (tableau[0][0] + tableau[1][1] + tableau[2][2]) == -3 or (tableau[0][2] + tableau[1][1] + tableau[2][0])== -3:
            return -1
    
    
        
    
    

def gagner(a):
    if a == 1:
        showinfo(title='Victoire',message='Les croix ont gagné !')
    elif a == -1:
        showinfo(title='Victoire',message='Les ronds ont gagné !')
    elif a == 0:
        showinfo(title='Egalité',message='Match nul !')



def reinit():
    
    global drapeau, cases, n
    cases = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    drapeau = True          
    n = 1

    message.configure(text='Aux tour des croix :')
    dessin.delete(ALL)      
    lignes = []
    for i in range(4):
      lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
      lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))


##-----Création de la fenêtre-----##
fen = Tk()
fen.title('Morpion')


##-----Création des zones de texte-----##
message=Label(fen, text='Aux tour des croix :')
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)


##-----Création des boutons-----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

bouton_reload = Button(fen, text='Recommencer', command=reinit)
bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)


##-----Création du canevas-----##
dessin=Canvas(fen, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)


##-----La grille-----##
lignes = []


##-----Evenements-----##
dessin.bind('<Button-1>', afficher)


##-----Programme principal-----##
reinit()
fen.mainloop()  

exit.onClick()