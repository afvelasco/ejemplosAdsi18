'''
Se trata de mostrar una interface gráfica donde se 
aprecie el avance de una competencia de 10 Atletas
'''
from random import randint
from tkinter import *
from atleta import Atleta

def avance():
    for i in range(10):
        x = randint(1,6)*10
        y = randint(1,6)*10
        competidores[i].irHasta(x,y)
        botones[i].place(x=20+competidores[i].distancia, y=20+i*35)
        if competidores[i].distancia >= 1000:
            avanzar["state"]=DISABLED
            mensaje["text"]=f"El ganador es el atleta: {i}"
            break
  

ventanita = Tk()
ventanita.geometry("1200x500")
ventanita.title("Competencia de atletismo")
avanzar = Button(text="Avanzar",command=avance)
avanzar.place(x=500, y=420)
competidores = [Atleta("") for x in range(10)]
botones = [Button() for x in range(10)]
for i in range(10):
    botones[i]["text"]=str(i)
    botones[i].place(x=20, y=20+i*35)
mensaje = Label(text="")
mensaje.place(x=480, y=380)
meta = Canvas(width=5, height=360, bg='black')
meta.place(x=1020,y=20)
meta.create_line(1,0,1,360)
ventanita.mainloop()