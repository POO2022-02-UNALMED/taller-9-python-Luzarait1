from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("290x250")

#Funciones para la calculadora:

operacion_ant = "+"
numero_ant = 3.0
var = False

def num1():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), "1")

def num2():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), "2")

def num3():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), "3")

def num4():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), "4")

def num5():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), "5")

def num6():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), "6")

def num7():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), "7")

def num8():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), "8")

def num9():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), "9")

def punto():
    global var
    if(var):
        pantalla.delete(0,len(pantalla.get()))
        var = False
    pantalla.insert(len(pantalla.get()), ".")

def mult():
    global operacion_ant
    global numero_ant
    operacion_ant = "*"
    numero_ant = float(pantalla.get())
    pantalla.delete(0,len(pantalla.get()))

def suma():
    global operacion_ant
    global numero_ant
    operacion_ant = "+"
    numero_ant = float(pantalla.get())
    pantalla.delete(0,len(pantalla.get()))

def resta():
    global operacion_ant
    global numero_ant
    operacion_ant = "-"
    numero_ant = float(pantalla.get())
    pantalla.delete(0,len(pantalla.get()))

def div():
    global operacion_ant
    global numero_ant
    operacion_ant = "/"
    numero_ant = float(pantalla.get())
    pantalla.delete(0,len(pantalla.get()))

def igual():
    numero = float(pantalla.get())
    if (operacion_ant == "+"):
        result = numero + numero_ant
    if (operacion_ant == "*"):
        result = numero * numero_ant
    if (operacion_ant == "-"):
        result = numero - numero_ant
    if (operacion_ant == "/"):
        result = numero / numero_ant

    pantalla.delete(0,len(pantalla.get()))
    pantalla.insert(0,str(result))
    global var
    var = True
    


# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num1).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num2).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num3).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num4).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num5).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num6).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num7).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num8).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=num9).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=igual).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", command=punto, borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=suma).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=resta).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=mult).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=div).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
