###########################################################
##------------Affiche l'image d'un fichier PPM ----------##
###########################################################
from fltk import*

f = open("Image PPM P3.txt", "r", encoding="utf-8")

def affiche_p3(fichier):
    # Chaque fonction appelée par "affiche_p3" renvoie un nombre de ligne (y) et de colonne (x)
    # afin de garder en sauvegarde la position de lecture dans le texte.
    fichier = list(fichier)
    
    ## VERIFIE LE FORMAT DU FICHIER ##
    form,x,y = lecture(fichier,0,0)
    if form != "P3":
        return ("Format invalide")
    
    ## DEFINIT LA TAILLE DE L'IMAGE ##
    taille_x,x,y = lecture(fichier,x,y)
    taille_y,x,y = lecture(fichier,x,y)
    taille_x,taille_y=int(taille_x),int(taille_y)
    
    ## DEFINIT L'INTENSITE MAXIMALE D'UNE COULEUR ##
    imax,x,y = lecture(fichier,x,y)
    cree_fenetre(taille_x,taille_y)
    
    ## DESSINE L'IMAGE ##
    for i in range(taille_y):
        for j in range(taille_x):
            color="#"
            for k in range(3):
                intens,x,y = lecture(fichier,x,y)
                color += str(hex(int(intens)))
            rectangle(i,j,i,j,couleur=color)
            
            
    
    
## Fonction qui vérifie le format P3 du fichier ##
                
def lecture(fichier,x,y):
    valeur = ""
    interrupteur = False
    texte = fichier[y]
    for i in range(x,len(texte)):
        c = texte[i]
        if interrupteur == True:
            if c == " " or i == len(texte)-1:
                return valeur,i,y
            else:
                valeur += c
        elif c == "#":
            return lecture(fichier,0,y+1)
        elif c != " ":
            valeur += c
            interrupteur = True

    return lecture(fichier,0,y+1)

    
print(affiche_p3(f))
