###########################################################
##------------Affiche l'image d'un fichier PPM ----------##
###########################################################

f = open("guybrush3.p3.ppm", "r", encoding="utf-8")

def affiche_p3(fichier):
    
    ligne=f.readline()
    
    ## VERIFIE LE FORMAT DU FICHIER ##
    if form(fichier,ligne) != True:
        return ("Format invalide")
    
    ## DEFINIT LA TAILLE DE L'IMAGE ##
    x,y=taille(fichier,ligne)

    

## Fonction qui vérifie le format P3 du fichier ##

def form(fichier,ligne):
    c="" #parcourt le fichier
    
    p=False #booléen qui indique si un p précède le caractère désigné par c
    
    for c in ligne:
        if c == "P":
            p = True
        elif p == True:
            return c == "3"
        elif c == "#":
            ligne=f.readline()
 

def taille(fichier,ligne):
    
    nx=False
    
    p=False
    x=""
    y=""
    
    for a in fichier:
        for c in a:
            if c == "P":
                p=True
            elif c == "3" and p == True:
                p=False
            elif c == "#":
                ligne=f.readline()
            elif c == " " and 
            else:
                if x == "":
                    x.append
                else:
                    return x,c           
      
#def intens_max(fichier,l,i)    
#def intens(fichier,l,i):


print(affiche_p3(f))