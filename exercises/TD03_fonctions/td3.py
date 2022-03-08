temps=(input("entrer une valeur"),input("entrer une valeur"),input("entrer une valuer"),input("entrer une valeur"))
def tempsEnSeconde (a):
     seconde = temps[0]*86400+temps[1]*3600+temps[2]*60+temps[3] 
     return seconde 
print(tempsEnSeconde(temps))     
print(type(temps))

def secondeEnTemps (t):
     jour=0
     heure=0
     minute=0
     while t>=86400 :
       t=t-86400
       jour=jour+1
     while t>=3600 :
        t=t-3600
        heure=heure+1 
     while t>=60 :
         t=t-60 
         minute=minute+1
     temps(jour,heure,minute,t) 
     return temps 
temps=secondeEnTemps(100000)
print(temps)
print(type(temps))  
