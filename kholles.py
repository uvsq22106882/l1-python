a=int(input("entrer un nombre de plus de deux chiffres"))
print((a//100)%10)

b=float(input("entrer un nombre "))
print(b%100)



z=int(input("entrer un nombre positif ou negatif"))
c=int(input("entrer un nombre positif ou negatif"))
if z*c>0:
    print("le signe est positif")
elif z*c<0:
    print("le signe est negatif ")
else :
    print("le signe est nul")        



n=int(input("entrer un nombre "))   
for i in range(n+1):
    a=int(input("entrer un nombre"))
    if a>n:
     print("le minimum est ",n)
    else:
     print("le minimum est",a)    



