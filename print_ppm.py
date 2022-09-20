###########################################################
##------------Affiche l'image d'un fichier PPM ----------##
###########################################################

f = open("Image PPM P3.txt", "r", encoding="utf-8")

def affiche_p3(fichier):
    # Chaque fonction appelée par "affiche_p3" renvoie un nombre de ligne (l) et de colonne (i)
    # afin de garder en sauvegarde la position de lecture dans le texte.
    fichier = list(fichier)
    
    ## VERIFIE LE FORMAT DU FICHIER ##
    form,l,i = format_P3(fichier,0,0)
    if form != "P3":
        return ("Format invalide")
    
    ## DEFINIT LA TAILLE DE L'IMAGE ##
    x,y,l,i = taille(fichier,1,0)
    print(x,y)
    
    ## DEFINIT L'INTENSITE MAXIMALE D'UNE COULEUR ##
    imax,l,i = intens_max(fichier,l,i)
    print(imax)

    
## Fonction qui vérifie le format P3 du fichier ##

def format_P3(fichier,l,i):
    P3 = ""
    interrupteur = False
    texte = fichier[l]
    
    for j in range(i,len(texte)):
        c=texte[j]
        if interrupteur == True:
            if c == " " or i == len(texte)-1:
                return P3,l,i
            else:
                P3 += c
        elif c == "#" or j == len(texte)-1:
            return format_P3(fichier,l+1,0)
        else:
            P3 += c
            interrupteur = True

def intens_max(fichier,l,i):
    intens = ""
    interrupteur = False
    texte = fichier[l]
    
    for j in range(i,len(texte)):
        c=texte[j]
        if interrupteur == True:
            if c == " " or i == len(texte)-1:
                intens=int(intens)
                return int(intens),l,i
            else:
                intens += c
        elif c == "#" or j == len(texte)-1:
            return intens_max(fichier,l+1,0)
        else:
            intens += c
            interrupteur = True
            

def taille(fichier,l,i):
    taille=[]
    compteur=0
    
    while compteur!=2:
        
        c = fichier[l][i]
        if c == "#" or i == len(fichier[l])-1:
            i = 0
            l += 1
        elif c == " ":
            if i<len(fichier[l])-1:
                i += 1
            else:
                i = 0
                l += 1
        else:
            nombre = ""
            while c != " " and i != len(fichier[l])-1:
                c = fichier[l][i]
                nombre += c
                i += 1
            compteur += 1
            taille.append(nombre)
    
    return int(taille[0]),int(taille[1]),l,i
                
                
            
print(affiche_p3(f))