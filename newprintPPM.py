###########################################################
##------------Affiche l'image d'un fichier PPM ----------##
###########################################################

from fltk import*

#f = open("Image PPM P3.txt", "r", encoding="utf-8")
f2 = open("iimage.txt", "r", encoding="utf-8")

## FONCTION QUI AFFICHE UNE IMAGE EN FORMAT P3 A L'AIDE DE LA BIBLIOTHEQUE DE DESSIN FLTK ##

def affiche_p3(fichier):
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
    cree_fenetre(taille_x*2,taille_y*5)
    
    ## DESSINE L'IMAGE ##
    for i in range(taille_y):
        for j in range(taille_x):
            color="#"
            for k in range(3):
                intens,x,y = lecture(fichier,x,y)
                color += hexadecimal(int(int(intens)*(255/int(imax))))
            print(color)
            rectangle(i,j,i,j,couleur=color)
            

    
## FONCTION QUI LIT UN ELEMENT DANS UN FICHIER TEXTE ET LE RENVOIE ##
                
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
    
def hexadecimal (n):
    t=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    return t[n//16]+t[n-16*(n//16)]

### PROGRAMME PRINCIPAL ###
print(affiche_p3(f2))