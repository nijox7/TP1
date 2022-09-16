###########################################################
##------------Affiche l'image d'un fichier PPM ----------##
###########################################################

f=open("guybrush3.p3", 'r', encoding="utf-8")

def affiche_p3(fichier):
    
    ligne=f.readline()
    x,y=0,0
    
    ## VERIFIE LE FORMAT DU FICHIER ##
    if form(fichier,ligne) != True:
        return ("Format invalide")
    
    ## DEFINIT LA TAILLE DE L'IMAGE ##
    print(taille(fichier,ligne))

    

## Fonction qui vérifie le format P3 du fichier ##

def form(fichier,ligne):
    c="" #parcourt le fichier
    
    p=False #booléen qui indique si un p précède le caractère désigné par c
    
    for c in ligne:
        if c == "P":
            p = True
        elif p == True:
            return c == "3"
        elif c=="#":
            ligne=f.readline()
 

def taille(fichier,ligne):
    p=False
    x=None
    
    for c in ligne:
        if c == "P":
             p=True
        elif c == "3" and p == True:
            p=False
        elif c == "#":
            ligne=f.readline()
        else:
            if x is None:
                x=c
            else:
                return x,c           
      
#def intens_max(fichier,l,i)    
#def intens(fichier,l,i):


print(affiche_p3(f))