import random
liste0=[]
liste1=[]
n=int(input("entrer une valeur "))
b=int(input("entrer une valeur "))
for i in range(n):
    liste0.append(random.randint(0,99))
print(liste0)
for i in range(b):
    liste1.append(random.randint(0,99))
print(liste1)

def liste(liste0,liste1) :
    liste=[]
    if len(liste0)==len(liste1):
        for i in range(len(liste0)):
            liste=liste.append(liste0[i]+liste1[i]) 
        print(liste) 
    else :
        print("les listes ne sont pas de la meme longeur on ne peut pas sommer")    
liste(liste0,liste1) 

listevisite=[]
m=int(input("entrer le nombre de fois"))
for i in range(m):
     listeviste.append(a)

listevisite=[[2,4,5],[],[2,3],[1],[2,4]]
list_tot = sum(listevisite,start=[])
listelieux=[]
def lieux_trop_visiter():
       for i in range (n):
           somme=0
           a=listevisite[i]
           somme=somme+1
           if somme>1:  
             listelieux.append(a)

            for i in range (5):
                 list.count(i)
print(listelieux) 
lieux_trop_visiter(listelieux)


listelieux1=[]
def lieux_jamais_visiter():
       for i in range (n):
           somme=0
           a=listepasvisite[i]
           somme=somme+1
           if somme<1:  
             listelieux1.append(a)
print(listelieux1) 
lieux_trop_visiter(listelieux1)

list=[]
def echangeable():
    for i in range(len(listevisite):
        if (listevisite[i]>=1):
            print("true")
        elif(listevisite[i]>):
            print("false")
        else:
            print("false")