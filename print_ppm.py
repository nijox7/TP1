###########################################################
##------------Affiche l'image d'un fichier PPM ----------##
###########################################################

f = open("Image PPM P3.txt", "r", encoding="utf-8")

def affiche_p3(fichier):
    
    ligne=f.readline()
    
    ## VERIFIE LE FORMAT DU FICHIER ##
    if forma(fichier,ligne) != True:
        return ("Format invalide")
    
    ## DEFINIT LA TAILLE DE L'IMAGE ##
    x,y=taille(fichier,ligne)

    

## Fonction qui vérifie le format P3 du fichier ##

def forma(fichier,ligne):
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
    xi=
    yi=
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
            else :
                if xi == False or xi == True and x != "":
                    xi=True
                    x+=c
                else:
                    if c=" ":
                        return int(x),int(y)
                    else:
                        
                             
      
#def intens_max(fichier,l,i)    
#def intens(fichier,l,i):


print(affiche_p3(f))

### ALGO POUR LECTURE ###

fichier=[["0","1","2","3","4"],["5","6","7","8","9"],["10","11","12","13"]]
f = open("Image PPM P3.txt", "r", encoding="utf-8")
num_ligne=0

def lecture(fichier,num_ligne):
    i=0
    texte=fichier[num_ligne]
    phrase=""
    
    for c in texte:
        phrase+=c
        i+=1
        if i == len(texte):
            if num_ligne+1 < len(fichier):
                return phrase+lecture(fichier,num_ligne+1)
            else:
                return phrase
            
            
print(lecture(f,num_ligne))