couleur =["blue", "green", "black", "yellow", "magenta", "red"]
x0=0
y0=600
x1=600
y1=0
n=int(input("entrer le nombre de cercle"))
couleur="red"
r=(y0-x0)/n/2
r1=(x1-y1)/n/2  
import tkinter as tk
CANVAS_WIDTH , CANVAS_HEIGHT =600, 600
racine=tk.Tk()
canvas = tk.Canvas(racine,width=CANVAS_WIDTH , height=CANVAS_HEIGHT , background="black")
def ChoisirCouleur():
      global couleur
      couleur = input("Choisir une couleur, soit :\n-white,\n-black,\n-red,\n-green,\n-blue,\n-cyan,\n-yellow")   
for i in range(0,n):
    ChoisirCouleur()
    canvas.create_oval(x0+r*i,y0-r*i,x1-r1*i,y1+r1*i,fill=couleur) 
canvas.grid()
racine.mainloop()