temps=(3,23,1,34)
def tempsEnSeconde (a):
    seconde = temps[0]*86400+temps[1]*3600+temps[2]*60+temps[3] 
    return seconde 
print(tempsEnSeconde(temps))     
print(type(temps))

def secondeEnTemps(t):
    jours = 0
    heures = 0
    minutes = 0
    while t > 86400:
        t = t - 86400
        jours = jours + 1
    while t > 3600:
        t = t - 3600
        heures = heures + 1
    while t > 60:
        t = t - 60
        minutes = minutes + 1
    Temps = (jours, heures, minutes,t)
    return Temps
Temps= secondeEnTemps (100000)
print(Temps)
print(type(Temps)) 

def affichageTemps(temps):
    if temps[0]==0 :
        print(end="")
    if temps[0]==1:
        print(" il y a un jour",end="")
    if temps[0]>1 :
        print(" il y a" ,temps[0],"jours",end="")
    if temps [1]==0:
        print(end="")
    if temps [1]==1 :
        print(" et  une heure ",end="")
    if temps[1]>1 :
        print(" et ",temps[1],"heures",end="")
    if temps [2]==0 :
        print(end="")
    if temps[2]==1 :
        print(" et il y a une minute", end="" )
    if temps[2]>1:
        print(" et ",temps[2],"minutes",end="")
    if temps[3]==0 :
        print(end="")
    if temps[3]==1 :
        print(" et il y a une seconde",end="")
    if temps[3]>1 :
        print(" et ",temps[3],"secondes",end="")                     
affichageTemps((1,0,14,23))

def demandeTemps(t):
    j=int(input("entrer une valeur"))
    h=int(input("entrer une valeur "))
    m=int(input("entrer une valeur"))
    s=int(input("entrer une valeur "))
    while (j>31)or(j<0) :
        print("entrer un nombre de jours entre 0 et 31")
    while (h>24)or(h<0):
        print("entrer un nombre de heures entre 0 et 31")
    while (m>60)or(m<0):
        print("entrer un nombre de minutes entre 0 et 60")
    while (s>60)or (m<0):
        print("entrer un nombre de seconde entre 0 et 60") 
               

