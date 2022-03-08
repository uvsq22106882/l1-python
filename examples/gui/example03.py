x=150
y=150
r=50
x1=20
y1=15
import tkinter as tk
 
racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin") # ajoute un titre 
couleur="blue"
couleur=str(input("choisir une couleur "))
 
def cercle():
  canvas.create_oval(x-r, y+r, x+r, y-r, fill=couleur)
  return cercle 
 
def carré():
    canvas.create_rectangle(x, y, x1, y1, fill=couleur)
    return carré

def croix():
    canvas.create_line(50,150,150,50, fill=couleur)
    canvas.create_line(50,50,150,150, fill=couleur)  
    return croix 

def ChoisircCouleur():
   global couleur
   couleur = input("Choisir une couleur, soit :\n-white,\n-black,\n-red,\n-green,\n-blue,\n-cyan,\n-yellow")    




bouton1 = tk.Button(text="Choisir une couleur", activebackground="brown")
bouton1.grid(row=0, column=2)

bouton2 = tk.Button(text="Cercle", activebackground="green", command=cercle)
bouton2.grid(row=1, column=0)
 
bouton3 = tk.Button(text="Carré", activebackground="green" , command=carré)
bouton3.grid(row=2, column=0)
 
bouton4 = tk.Button(text="croix", activebackground="green", command=croix)
bouton4.grid(row=3, column=0)
 
canvas = tk.Canvas(background="black")
canvas.grid(row=1, column=1, rowspan=3, columnspan=4)
 
racine.mainloop() # Lancement de la boucle principale

