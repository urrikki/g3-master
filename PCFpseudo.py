#DEBUT

#On admet que la fonction random existe et qu'elle retourne un nombre aleatoirement


#definir la fonction pierreFeuilleCiseau qui retourne si vous avez gagnez ou perdu contre l'IA par rapport a votre coup (joueurAction(string))

    #tableau iaCoup qui enregistre les differents coup possible pour l'IA(string) tableau = ["pierre","feuille","ciseau"]
    #variable iaAction qui recupere le retour de la fonction random.randrange(0,3) qui va recuperer une coup possible du tableau iaCoup

    #si joueurAction est égal à iaAction 
        #alors écrire joueurAction +"contre"+ iaAction +" , Egalité !"
    
    #sinon si joueurAction est égal à pierre et iaAction est égal à feuille
        #alors écrire pierre contre feuille , Perdu !
    
    #sinon si joueurAction est égal à feuille et iaAction est égal à ciseau
        #alors écrire feuille contre ciseau , Perdu !

    #sinon si joueurAction est égal à ciseau et iaAction est égal à pierre
        #alors écrire ciseau contre pierre , Perdu !

    #sinon si joueurAction est égal à pierre et iaAction est égal à ciseau
        #alors écrire pierre contre ciseau , Gagné !
    
    #sinon si joueurAction est égal à feuille et iaAction est égal à pierre
        #alors écrire feuille contre pierre , Gagné !
    
    #sinon si joueurAction est égal à ciseau et iaAction est égal à feuille
        #alors écrire ciseau contre feuille , Gagné !

#FIN



    
    
    
    
