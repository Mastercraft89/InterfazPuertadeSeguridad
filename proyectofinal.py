from _tkinter import*
from tkinter import Button, Entry,Label, Tk
import serial, time
import pywhatkit

puerto = 'COM3'
ard = serial.Serial(puerto,9600,timeout=1)

ventana = Tk()
ventana.geometry("500x450")
ventana.title("Ventana de seguridad")

i=0

def reloj():
    horas=    time.strftime("%H")
    minutos=  time.strftime("%M")
    segundos= time.strftime("%S")

    #print(horas + ":" + minutos +":"+ segundos)
    miEtiqueta.config(text=horas + ":" + minutos +":"+ segundos)
    miEtiqueta.after(1000, reloj)
miEtiqueta = Label(ventana, text="  ", font=("Roboto", 28))
miEtiqueta.pack(pady=20)
reloj()
miEtiqueta.after(5000)


def iniciar_sesion():
    global i
    if  entrada_confirmacion.get() == "1234":
        print("Sesión iniciada")
        ventana.configure(bg="green")
        ard.write(b'o')
      
    else:
        i=i+1
        if (i < 3):
            print("Contraseña incorrecta")
            ventana.configure(bg="red")
            ard.write(b'x')
        
        if (i>=3):
            ard.write(b'y')
            print("Munchos errores, puerta asegurada")
            ventana.configure(bg="black")
            pywhatkit.sendwhatmsg("+52 7531651973", "Numero intentos excedidos",17,47,10)
    
lbl_confirmacion = Label(ventana, text="Confirmar Contraseña")
lbl_confirmacion.pack()
entrada_confirmacion = Entry(ventana, show="X")
entrada_confirmacion.pack()

boton_iniciar_sesion = Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar_sesion.pack()

ventana.mainloop()